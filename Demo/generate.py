from __future__ import annotations
import os
import sys

import fire
import gradio as gr
import torch
import transformers
from peft import PeftModel
from transformers import GenerationConfig, LlamaForCausalLM, LlamaTokenizer
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes
from typing import Iterable
from utils.prompter import Prompter

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

try:
    if torch.backends.mps.is_available():
        device = "mps"
except:  # noqa: E722
    pass

PARENT_BLOCK_CSS = """
#col_container {
    width: 90%; 
    margin-left: auto; 
    margin-right: auto;
}

#chatbot {
    height: 600px; 
    overflow: auto;
    background-color: white;
}

.chat_wrap_space {
    margin-left: 0.5em
}
"""
ABSTRACT = """

NOTE: too long input (input, instruction) will not be allowed. Please keep input < 500 and instruction < 150
"""
BOTTOM_LINE = """
This demo currently runs 7B version on a RTX 3090 instance.
"""
html_code = '''
<div style="display: flex; justify-content: space-between; align-items: center;">
  <div style="order: 1;">
    <h1 style="font-size: 6em; font-family: SimHei;">{title}</h1>
  </div>
</div>
'''

class Seafoam(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = colors.vxgreen,
        secondary_hue: colors.Color | str = colors.red,
        neutral_hue: colors.Color | str = colors.gray,
        spacing_size: sizes.Size | str = sizes.spacing_lg,
        radius_size: sizes.Size | str = sizes.radius_none,
        text_size: sizes.Size | str = sizes.text_sm,
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
        )
        super().set(
            button_primary_background_fill="linear-gradient(90deg, *primary_300, *secondary_400)",
            button_primary_background_fill_hover="linear-gradient(90deg, *primary_200, *secondary_300)",
            button_primary_text_color="white",
            button_primary_background_fill_dark="linear-gradient(90deg, *primary_600, *secondary_800)",
            slider_color="*secondary_300",
            slider_color_dark="*secondary_600",
            block_title_text_weight="600",
            block_border_width="3px",
            block_shadow="*shadow_drop_lg",
            button_shadow="*shadow_drop_lg",
            button_large_padding="32px",
        )
seafoam = Seafoam()

def main(
    protein: bool = False,
    load_8bit: bool = False,
    base_model: str = "",
    lora_weights: str = "tloen/alpaca-lora-7b",
    prompt_template: str = "",  # The prompt template to use, will default to alpaca.
    server_name: str = "0.0.0.0",  # Allows to listen on all interfaces by providing '0.
    share_gradio: bool = False,
):
    base_model = base_model or os.environ.get("BASE_MODEL", "")
    assert (
        base_model
    ), "Please specify a --base_model, e.g. --base_model='decapoda-research/llama-7b-hf'"

    prompter = Prompter(prompt_template)
    if protein == False:
        tokenizer = LlamaTokenizer.from_pretrained(base_model)
    else:
        tokenizer = LlamaTokenizer.from_pretrained(base_model, bos_token='<s>', eos_token='</s>', add_bos_token=True, add_eos_token=False)
        
    if device == "cuda":
        model = LlamaForCausalLM.from_pretrained(
            base_model,
            load_in_8bit=load_8bit,
            torch_dtype=torch.float16,
            device_map={"": 0}
        )
        if protein == False:
            model = PeftModel.from_pretrained(
                model,
                lora_weights,
                torch_dtype=torch.float16,
                device_map={"": 0},
            )

    elif device == "mps":
        model = LlamaForCausalLM.from_pretrained(
            base_model,
            device_map={"": device},
            torch_dtype=torch.float16,
        )
        if protein == False:
            model = PeftModel.from_pretrained(
                model,
                lora_weights,
                device_map={"": device},
                torch_dtype=torch.float16,
            )
    else:
        model = LlamaForCausalLM.from_pretrained(
            base_model, device_map={"": device}, low_cpu_mem_usage=True
        )
        if protein == False:
            model = PeftModel.from_pretrained(
                model,
                lora_weights,
                device_map={"": device},
            )

    # unwind broken decapoda-research config
    model.config.pad_token_id = tokenizer.pad_token_id = 0  # unk
    model.config.bos_token_id = 1
    model.config.eos_token_id = 2

    if not load_8bit:
        model.half()  # seems to fix bugs for some users.

    model.eval()
    if torch.__version__ >= "2" and sys.platform != "win32":
        model = torch.compile(model)
        
    def add_text(history, instructions, inputs):
        history = history + [(instructions+"   \n"+inputs,None)]
        return history, gr.update(value="", interactive=False)
    
    def evaluate(
        instruction,
        input,
        temperature=0.1,
        top_p=0.75,
        top_k=40,
        num_beams=4,
        repetition_penalty=1.0,
        max_new_tokens=128,
    ):
        print(instruction)
        print(input)
        print(temperature,top_p,top_k,num_beams,repetition_penalty,max_new_tokens)
        
        prompt = prompter.generate_prompt(instruction, input)
        inputs = tokenizer(prompt, return_tensors="pt")
        input_ids = inputs["input_ids"].to(device)
        if protein == False:
            do_sample=False
        else:
            do_sample=True
        generation_config = GenerationConfig(
            do_sample=do_sample,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            num_beams=num_beams,
            repetition_penalty=repetition_penalty
        )
        with torch.no_grad():
            generation_output = model.generate(
                input_ids=input_ids,
                generation_config=generation_config,
                return_dict_in_generate=True,
                output_scores=True,
                max_new_tokens=max_new_tokens,
            )
        s = generation_output.sequences[0]
        output = tokenizer.decode(s)
        re=prompter.get_response(output)
        last_bracket_index = re.find('#')
        if last_bracket_index != -1:
            re = re[:last_bracket_index ]
            
        last_bracket_index = re.rfind(']')
        if last_bracket_index != -1:
            re = re[:last_bracket_index + 1]
        re=re.replace("<br>", "")
        return re
    
    def bot(history,
        temperature,
        top_p,
        top_k,
        num_beams,
        repetition_penalty,
        max_new_tokens):
        instruction=history[-1][0].split("   <br>")[0]
        input=history[-1][0].split("   <br>")[1].replace("<br>", "")
        response = evaluate(instruction, input, temperature, top_p, top_k, num_beams, repetition_penalty, max_new_tokens)
        history[-1][1] = response
        return history
    
    with gr.Blocks(css=PARENT_BLOCK_CSS, theme=seafoam) as demo:
        state_chatbot = gr.State([])

        with gr.Column(elem_id='col_container'):
            gr.HTML(html_code)
            with gr.Row():
                with gr.Column(variant="panel", scale=4):
                    chatbot = gr.Chatbot(elem_id='chatbot', label=' ')

                with gr.Column(variant="panel", scale=1):
                    instruction_txtbox = gr.Textbox(placeholder="What do you want to say to AI?", label="Instruction")
                    input_txtbox = gr.Textbox(placeholder="Surrounding information to AI", label="Input")
                    hidden_txtbox = gr.Textbox(placeholder="", label="Order", visible=False)
                    submit_btn = gr.Button(value="Submit",variant="primary").style(size="sm")
                    Temperature=gr.components.Slider(minimum=0, maximum=1, value=0.1, label="Temperature").style(container=False)
                    Top_p=gr.components.Slider(minimum=0, maximum=1, value=0.75, label="Top p").style(container=False)
                    Top_k=gr.components.Slider(minimum=0, maximum=100, step=1, value=40, label="Top k").style(container=False)
                    Beams=gr.components.Slider(minimum=1, maximum=4, step=1, value=4, label="Beams").style(container=False)
                    Repetition_penalty=gr.components.Slider(minimum=1, maximum=5, value=1, label="Repetition_penalty").style(container=False)
                    Max_tokens=gr.components.Slider(minimum=1, maximum=2000, step=1, value=128, label="Max tokens").style(container=False)
            
            gr.Markdown(f"{ABSTRACT}")
            gr.Markdown(f"{BOTTOM_LINE}")

        send_event = submit_btn.click(add_text, [chatbot, instruction_txtbox, input_txtbox], [chatbot, input_txtbox], queue=False).then(
            bot, [chatbot, Temperature, Top_p, Top_k, Beams, Repetition_penalty, Max_tokens], chatbot
        )
        send_event.then(lambda: gr.update(interactive=True), None, [instruction_txtbox], queue=False)
        send_event.then(lambda: gr.update(interactive=True), None, [input_txtbox], queue=False)

    demo.queue(
        concurrency_count=4,
        max_size=100,
    ).launch(
        max_threads=10,
        share=share_gradio,
        # server_port=args.port,
        server_name="0.0.0.0",
    )

if __name__ == "__main__":
    fire.Fire(main)