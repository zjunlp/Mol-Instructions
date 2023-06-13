
# Demo
## ⚙️ Environment Configuration
Configure the environment with the following commands:
```shell
conda create -n lora python=3.9 -y
conda activate lora
pip install torch==1.12.0+cu116 torchvision==0.13.0+cu116 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu116
pip install -r requirements.txt
```
## 🚀 Instruction tuning (LoRA)
Our code is based on [alpaca-lora](https://github.com/tloen/alpaca-lora) with modifications made only to the training hyperparameters. We trained the model on a single node with 8 V100(32GB) GPUs. All the training hyperparameters are already reflected in the training code. Please modify the training parameters, including `warmup_steps`, `micro_batch_size`, etc., according to your hardware setup. To start the training, use the following command:
```shell
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 accelerate launch finetune.py --data_path $DATA_PATH --base_model $BASE_MODEL_PATH
```
If you want to modify the training hyperparameters in the command line, you can simply add the corresponding parameters after the command.

Please download [llama-7b-hf](https://huggingface.co/decapoda-research/llama-7b-hf/tree/main) to obtain the pre-training weights of LLaMA-7B, refine the `base_model` to point towards the location where the model weights are saved.


## Inference

### Recovering Weights

You can conveniently recover the model weights we trained through the following command. You could replace `{LLAMA_WEIGHT}` with the directory of LLaMA model weights you own and replace `{DIFF_WEIGHT}` with the directory of diff weights we provided and replace `{RECOVER_WEIGHT}` with the path you want to save the recovering weights. 
```shell
python weight_diff.py recover \
  --path_raw {LLAMA_WEIGHT} \
  --path_diff {DIFF_WEIGHT} \
  --path_tuned {RECOVER_WEIGHT}
```

### Generation

We provide a example to perform generation.

```Shell
python src/generate.py \
    --model_name_or_path {MODEL_NAME} \
    --model_type {MODEL_TYPE} \
    --prompt_template_dir {TEMPLATE_PATH} \
    --prompt_template_name {TEMPLATE_NAME} \
    --top_k 8 \
    --repetition_penalty 1.2
```
