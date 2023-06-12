<h1 align="center">  🧪 Mol-Instructions  </h1>
<h3 align="center"> An open, large-scale biomolecular instruction dataset for large language models. </h3>

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/zjunlp/cama/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg)](https://github.com/zjunlp/cama/blob/main/DATA_LICENSE)


## Overview

### 📊 Dataset Stats
**Mol-Instructions** comprises three cardinal components:
- 🔬 *Molecule-oriented instructions:* This component delves into the world of small molecules, emphasizing their inherent properties and behaviors. It sheds light on the fundamental challenges of diverse chemical reactions and molecular design, with 148,4K instructions across six tasks.
- 🧬 *Protein-oriented instructions:* Rooted in the biosciences, this component presents 505K instructions across five distinct categories of tasks. These tasks aim to predict the structure, function, and activity of proteins, and facilitate protein design based on textual directives.
- 🥼 *Biomolecular text instructions:* Predominantly designed to cater to NLP tasks within the fields of bioinformatics and chemoinformatics, this part encapsulates six information extraction and Q\&A tasks represented through 53K instructions.

<!-- <p align="center" width="100%">
<a href="" target="_blank"><img src="./fig/stat-all.pdf" alt="IE" style="width: 90%; min-width: 90px; display: block; margin: auto;"></a>
</p> -->

<div align=center><img src="fig/stat-all.pdf" width="100%" height="100%" /></div>

### Model Release
- adapter weights (huggingface link)
- quantized model (huggingface link)

### Data Release
- molecular instructions (website?)

## ⚙ Demo

We have provided a web version demo based on [Gradio](https://gradio.app). To use it, you first need to download this repository:

```shell
git clone https://github.com/zjunlp/Mol-Instruction
cd Demo
```

Step 1, install Gradio by running：`pip install gradio`. 

Step 2, specify the parameters in the [generate.sh](./Demo/generate.sh) file.

```shell
CUDA_VISIBLE_DEVICES=0 python generate.py \
    --interactive False\
    --protein False\
    --load_8bit \
    --base_model $BASE_MODEL_PATH \
    --share_gradio True\
    --lora_weights $FINETUNED_MODEL_PATH \
```

Step 3, run the [generate.sh](./Demo/generate.sh) file in the repository： 

```shell
sh generate.sh
```

**web-based interaction**
```shell
--interactive False\
```
The program will run a web server and output an address. Open the output address in a browser to use it.

**command-line interaction:**
```shell
--interactive True\
```
The disadvantage is the inability to dynamically change decoding parameters.


### Task descriptions

- **Mol2Text**: *text description generation based on the given molecule*.

```txt
🧑🏻‍🔬: Provide a description of this molecule. [C][C][/C][=C][\C][/C][=C][\C][C@H1][Branch1][C][O][C@@H1][Branch1][P][/C][=C][/C][=C][/C][=C][\C][/C][=C][\C][C][C][=Branch1][C][=O][O-1][S][C][C@H1][Branch1][C][NH3+1][C][=Branch1][C][=O][N][C][C][=Branch1][C][=O][O-1]

🦄️: The molecule is an docosanoid anion that is the conjugate base of (7R,17S)-dihydroxy-(4Z,7Z,11E,13E,16Z,19Z)-docosahexaenoic acid, formed via deprotonation of the carboxy group; major species at pH 7.3. It is an omega-hydroxy-polyunsaturated fatty acid anion and a docosanoid anion.
```

- **Text2Mol**: *molecule generation based on the given text description*.

```txt
🧑🏻‍🔬: Create a molecule that satisfies the conditions outlined in the description. The molecule is a Glu-Cys-Gly tripeptide derivative of glutathione containing a 2-hydroxyethyl substituent on the S of the Cys residue. It derives from a glutathione. 

🦄️: [N][C@@H1][Branch1][#C][C][C][C][N][C@@H1][Branch1][Ring1][C][S][C][C][C][C@H1][N][C][=Branch1][C][=O][O][C][=Branch1][C][=O][O][C][=Branch1][C][=O][O]
```

- **Forward Reaction Prediction**: *predict the outcome of a chemical reaction when given the reactants and reaction reagents*.

```txt
🧑🏻‍🔬: What product could potentially form from the reaction of the given reactants and reagents? [O][=N+1][Branch1][C][O-1][C][=C][C][Branch1][C][Cl][=C][Branch2][Ring1][Ring1][O][C][=C][C][=C][Branch1][C][Cl][C][=C][C][=C][C][=C][Ring1][O][Ring1][=Branch1][C][Branch1][C][Cl][=C][Ring2][Ring1][Ring2].[C][C][=C][C][=C][C][=C][Ring1][=Branch1]

🦄️: [N][C][=C][C][Branch1][C][Cl][=C][Branch2][Ring1][Ring1][O][C][=C][C][=C][Branch1][C][Cl][C][=C][C][=C][C][=C][Ring1][O][Ring1][=Branch1][C][Branch1][C][Cl][=C][Ring2][Ring1][C]
```

- **Retrosynthesis**: *deconstruct a target molecule into simpler precursor molecules*.

```txt
🧑🏻‍🔬: With the given product, suggest some likely reactants that were used in its synthesis. [C][S][=Branch1][C][=O][=Branch1][C][=O][N][C][=C][C][=C][Branch1][=Branch1][N+1][=Branch1][C][=O][O-1][C][Branch1][C][Cl][=C][Ring1][#Branch2]

🦄️: [C][S][=Branch1][C][=O][=Branch1][C][=O][Cl].[N][C][=C][C][=C][Branch1][=Branch1][N+1][=Branch1][C][=O][O-1][C][Branch1][C][Cl][=C][Ring1][#Branch2]
```

- **Reagent Prediction**: *predict the most likely reagents that can be used to carry out a chemical reaction or transformation*.

```txt
🧑🏻‍🔬: Given this chemical reaction, what are some reagents that could have been used? [C][O][C][=Branch1][C][=O][/C][=C][Branch1][O][/C][#C][C][=C][C][=C][C][=C][Ring1][=Branch1][C][=C][C][=C][C][=C][Ring1][=Branch1]>>[O][=C][Branch1][C][O][/C][=C][Branch1][O][/C][#C][C][=C][C][=C][C][=C][Ring1][=Branch1][C][=C][C][=C][C][=C][Ring1][=Branch1]

🦄️: C1CCOC1.[Na+].[OH-]
```

- **Property Prediction**: *predict various properties of molecules*.

```txt
🧑🏻‍🔬: I would like to know the HOMO-LUMO gap of this molecule, can you provide it? [N][=C][O][C][C][Branch1][Ring2][C][C][#C][=C][Ring1][Branch2]

🦄️: 0.2136
```

### Example Demonstration

<p align="center">
  <img alt="Demo" src=gradio_interface_gif.gif style="width: 700px; height: 340px;"/>
</p>


## 🚀 Quick Start 

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

The screencast below is not sped up and running on an M1 Macbook Pro:

cpp gif


## 🚨 Usage and License Notices
Please note that all model weights and data of MoLAMA is exclusively licensed for research purposes. The accompanying dataset is licensed under CC BY NC 4.0, which permits solely non-commercial usage. Commercial use is strictly **prohibited**.

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
