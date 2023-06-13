import os
import sys

import fire
import gradio as gr
import torch
import transformers
from peft import PeftModel
from transformers import GenerationConfig, LlamaForCausalLM, LlamaTokenizer

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

def main(
    CLI: bool = False,
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
            #device_map="auto",
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

    def evaluate(
        instruction,
        input=None,
        temperature=0.1,
        top_p=0.75,
        top_k=40,
        num_beams=4,
        repetition_penalty=1,
        max_new_tokens=128,
        **kwargs,
    ):
        
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
            repetition_penalty=repetition_penalty,
            **kwargs,
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
        # 下面三行代码是修改过后的，代表把最后一个']'，‘#’字符的全部删除
        last_bracket_index = re.find('#')
        if last_bracket_index != -1:
            re = re[:last_bracket_index ]
            
        last_bracket_index = re.rfind(']')
        if last_bracket_index != -1:
            re = re[:last_bracket_index + 1]
        
        return re
    if CLI:
        while True:

            # get instruction from user
            instruction = input("Enter instruction: ")
            
            # get user input
            input_text = input("Enter input text: ")

            # evaluate the instruction with input_text
            if protein == False:
                output = evaluate(instruction, input=input_text, temperature=0.1, top_p=0.75, top_k=40, num_beams=4, repetition_penalty=1, max_new_tokens=128)
            else:
                output = evaluate(instruction, input=input_text, temperature=0.9, top_p=0.9, top_k=8, num_beams=1, repetition_penalty=1.2, max_new_tokens=1024)

            # print the output
            print(output)

            # ask if the user wants to continue or exit
            choice = input("Do you want to continue? (y/n): ")
            if choice.lower() != "y":
                break

        
    else:
        mytheme = gr.themes.Default().set(
        slider_color="#0000FF",
        )
        gr.Interface(
            theme=mytheme,
            title="Mol-Instruction",
            fn=evaluate,
            inputs=[
                gr.components.Textbox(
                    lines=2,
                    label="Instruction",
                ),
                gr.components.Textbox(lines=2, label="Input"),
                gr.components.Slider(
                    minimum=0, maximum=1, value=0.1, label="Temperature"
                ),
                gr.components.Slider(
                    minimum=0, maximum=1, value=0.75, label="Top p"
                ),
                gr.components.Slider(
                    minimum=0, maximum=100, step=1, value=40, label="Top k"
                ),
                gr.components.Slider(
                    minimum=1, maximum=4, step=1, value=4, label="Beams"
                ),
                gr.components.Slider(
                    minimum=1, maximum=5, value=1, label="Repetition penalty"
                ),
                gr.components.Slider(
                    minimum=1, maximum=2000, step=1, value=128, label="Max tokens"
                ),
            ],
            outputs=[
                gr.inputs.Textbox(
                    lines=5,
                    label="Output",
                )
            ],
        ).launch(server_name="0.0.0.0", share=share_gradio)

if __name__ == "__main__":
    fire.Fire(main)
