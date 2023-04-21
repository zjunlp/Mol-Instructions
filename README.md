 # 🦄️ MoLAMA

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/zjunlp/cama/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg)](https://github.com/zjunlp/cama/blob/main/DATA_LICENSE)

⚗️ Welcome to the MoLAMA project repository! MoLAMA is a large-scale molecular language model that possesses the ability to understand 🧑🏻‍🔬*human language* and 🔬*molecular language*, which can assist communities in conducting research in the field of molecular science.



## 💡 Overview


### Model Release
huggingface link (7B)

## ⚙ Step-by-step guidelines

Gradio interface gif

You can execute our model natively on your local device. Here we included detailed guidelines to facilitate implementation.

### Step 1
Run the following command to compile the [`alpaca.cpp`](https://github.com/antimatter15/alpaca.cpp) project:

```sh
>> git clone https://github.com/antimatter15/alpaca.cpp
>> cd alpaca.cpp

>> make chat
```

### Step 2
Download xxx.bin(model link) and place it in the same folder as the `chat` executable. The files should be organized in the following hierarchy:

```
├── alpaca.cpp                  
│   ├── chat                    
│   ├── xxx.bin                 
│   ├── ...
```

### Step 3
After downloading the model weights and putting them in the right folder, please run:

```sh
>> ./chat
```

The screencast below is not sped up and running on an M1 Macbook Air.

cpp gif

## 🚨 Usage and License Notices
Please note that MoLAMA is exclusively licensed for research purposes. The accompanying dataset is licensed under CC BY NC 4.0, which permits solely non-commercial usage. Commercial use is strictly **prohibited**.

## 🧑🏻‍💻 Authors
All authors below contributed equally and the order is determined by random draw.
- Yin Fang
- Rui Huang
- Kangwei Liu
- **Ningyu Zhang**
- Huajun Chen

## 📚 References
Please cite the repository if you use the `data` or `code` of our work.

```
@misc{molama,
  author = {Yin Fang, Rui Huang, Kangwei Liu, Ningyu Zhang, Huajun Chen},
  title = {MoLAMA},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/}},
}
```

## 🫱🏻‍🫲🏾 Acknowledgements

We appreciate [LLaMA](https://github.com/facebookresearch/llama), [Huggingface Transformers Llama](https://github.com/huggingface/transformers/tree/main/src/transformers/models/llama), [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html), [Alpaca-LoRA](https://github.com/tloen/alpaca-lora), [Alpaca.cpp](https://github.com/antimatter15/alpaca.cpp), [Chatbot Service](https://github.com/deep-diver/LLM-As-Chatbot) and many other related works for their open-source contributions.
