
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

Please download [llama-7b-hf](https://huggingface.co/decapoda-research/llama-7b-hf/tree/main) to obtain the pre-training weights of LLaMA-7B, refine the `--base_model` to point towards the location where the model weights are saved.


## 💻 Inference

### Generation

We provide an example to perform generation. 

```shell
# run LoRA model (Molecule & Text)
>> python generate.py \
    --CLI True \
    --protein False\
    --load_8bit \
    --base_model $BASE_MODEL_PATH \
    --lora_weights $FINETUNED_MODEL_PATH \
```

For models fine-tuned on **molecule-oriented** and **biomolecular text** instructions, set `$FINETUNED_MODEL_PATH` to `'zjunlp/llama-molinst-molecule-7b'` or `'zjunlp/llama-molinst-biotext-7b'`.

If you want to use our model fine-tuned on **protein-oriented** instructions, please set `--protein` True and supply `--base_model` with the path of your restored LLaMA model weights (see the following section) while no need to set `--lora_weights`.

### How to recover Weights

For full fine-tuned (**protein-oriented**) LLaMA model, you can conveniently recover the model weights we trained through the following command.

Please replace `$BASE_MODEL_PATH` with the directory of your own LLaMA model weights, replace `$DIFF_WEIGHT_PATH` with the path of our provided [diff weights](https://huggingface.co/zjunlp/llama-molinst-protein-7b), and replace `$RECOVER_WEIGHT_PATH` with the desired path to save the recovered weights. If the directory of recovered weights lacks required files (e.g., tokenizer configuration files), you can copy from `$DIFF_WEIGHT_PATH`.

```shell
python weight_diff.py recover \
  --path_raw $BASE_MODEL_PATH \
  --path_diff $DIFF_WEIGHT_PATH \
  --path_tuned $RECOVER_WEIGHT_PATH
```

After that, you can execute the following command to generate outputs with the fine-tuned LLaMA model.

```shell
# run fine-tuned model (Protein)
>> python generate.py \
    --CLI True \
    --protein True \
    --base_model $RECOVER_WEIGHT_PATH \
```
