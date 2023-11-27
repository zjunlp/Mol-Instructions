import os
import sys

import json
from typing import Union
from tqdm import tqdm


import torch
import transformers
from transformers import set_seed
from transformers import GenerationConfig, LlamaForCausalLM, LlamaTokenizer

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"


class Prompter(object):
    __slots__ = ("template", "_verbose")

    def __init__(self, data_dir, template_name: str = "", verbose: bool = False):
        self._verbose = verbose
        if not template_name:
            # Enforce the default here, so the constructor can be called with '' and will not break.
            template_name = "alpaca"
        file_name = os.path.join(data_dir, f"{template_name}.json")
        if not os.path.exists(file_name):
            raise ValueError(f"Can't read {file_name}")
        with open(file_name) as fp:
            self.template = json.load(fp)
        if self._verbose:
            print(
                f"Using prompt template {template_name}: {self.template['description']}"
            )

    def generate_prompt(
        self,
        instruction: str,
        input: Union[None, str] = None,
        label: Union[None, str] = None,
    ) -> str:
        # returns the full prompt from instruction and optional input
        # if a label (=response, =output) is provided, it's also appended.
        if input:
            res = self.template["prompt_input"].format(
                instruction=instruction, input=input
            )
        else:
            res = self.template["prompt_no_input"].format(
                instruction=instruction
            )
        if label:
            res = f"{res}{label}"
        if self._verbose:
            print(res)
        return res

    def get_response(self, output: str) -> str:
        return output.split(self.template["response_split"])[1].strip()


@torch.inference_mode()
def evaluate(
    model,
    prompter,
    tokenizer,
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
    input_ids = inputs["input_ids"].to(model.device)
    print(prompt)
    generation_config = GenerationConfig(
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        num_beams=num_beams,
        repetition_penalty=repetition_penalty,
        **kwargs,
    )

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
    # remove the last ']' or ‘#’
    last_bracket_index = re.find('#')
    if last_bracket_index != -1:
        re = re[:last_bracket_index ]
        
    last_bracket_index = re.rfind(']')
    if last_bracket_index != -1:
        re = re[:last_bracket_index + 1]
    
    return re


def main(
    task: str = 'test',
    protein: bool = True,
    load_8bit: bool = False,
    base_model: str = "data/model_data/llama-molinst-protein-7b-recover",
    lora_weights: str = "data/model_data/alpaca_lora",
    prompt_template: str = "data/templates",
):
    set_seed(2023)

    prompter = Prompter(prompt_template, template_name="alpaca")
    if protein:
        tokenizer = LlamaTokenizer.from_pretrained(base_model, bos_token='<s>', eos_token='</s>', add_bos_token=True, add_eos_token=False)
    else:
        tokenizer = LlamaTokenizer.from_pretrained(base_model)

    model = LlamaForCausalLM.from_pretrained(
        base_model,
        torch_dtype=torch.float16,
        device_map={"": 2}
    )

    model.eval()

    model.config.pad_token_id = tokenizer.pad_token_id = 0  # unk
    model.config.bos_token_id = 1
    model.config.eos_token_id = 2

    
    with open(f'data/eval_data/{task}.json', 'r') as f:
        examples = json.load(f)

    examples = examples[:1000]
    records = []

    for example in tqdm(examples):
        task = example['metadata']['task']
        if task == 'protein_design':
            continue
        
        response = evaluate(model=model, prompter=prompter, tokenizer=tokenizer, instruction=example['instruction'], input=example['input'], temperature=0.95, top_p=0.7, max_new_tokens=300)
        
        target = example['output']
        
        records.append(
            {
                'task': task,
                'response': response,
                'target': target
            }
        )

    with open(f'output/{task}_result.json', 'w') as f:
        json.dump(records, f, ensure_ascii=True, indent=4)

if __name__ == "__main__":

    main()
