<h1 align="center">  🧪 Mol-Instructions  </h1>
<h3 align="center"> An open, large-scale biomolecular instruction dataset for large language models. </h3>

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/zjunlp/cama/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg)](https://github.com/zjunlp/cama/blob/main/DATA_LICENSE)


<div align=center><img src="fig/abs.png" width="100%" height="100%" /></div>

## 🆕 News
- \[**June 2023**\] Release the first version (v1) of datasets and model weights.


## 📌 Contents
- [Overview](#1)
  - [Data Stats](#1-1)
  - [Data Construction](#1-2)
  - [Data Release](#1-3)
- [Tasks](#2)
  - [Molecule-oriented](#2-1)
  - [Protein-oriented](#2-2)
  - [Biomolecule text](#2-3) 
- [Demo](#3)
  - [Model Weight Release](#3-1)
  - [Model Usage Guide](#3-2)
  - [FAQ](#3-3)
- [Notices](#4)
  - [Usage and License](#4-1) 
  - [Limitations](#4-2)  
- [About](#5)
  - [References](#5-1)
  - [Acknowledgements](#5-2)


<h2 id="1">1. Overview</h2>

<h3 id="1-1"> 📊 1.1 Data Stats</h3>

<div align=center><img src="fig/stat.png" width="90%" height="90%" /></div>

**Mol-Instructions** comprises three cardinal components:
- 🔬 *Molecule-oriented instructions:* This component delves into the world of small molecules, emphasizing their inherent properties and behaviors. It sheds light on the fundamental challenges of diverse chemical reactions and molecular design, with 148,4K instructions across six tasks.
- 🧬 *Protein-oriented instructions:* Rooted in the biosciences, this component presents 505K instructions across five distinct categories of tasks. These tasks aim to predict the structure, function, and activity of proteins, and facilitate protein design based on textual directives.
- 🥼 *Biomolecular text instructions:* Predominantly designed to cater to NLP tasks within the fields of bioinformatics and chemoinformatics, this part encapsulates six information extraction and Q\&A tasks represented through 53K instructions.

<h3 id="1-2"> 🛠️ 1.2 Data Construction</h3>

<h3 id="1-3"> 🤗 1.3 Data Release</h3>

We release the dataset on Hugging Face at [zjunlp/Mol-Instructions](https://huggingface.co/datasets/zjunlp/Mol-Instructions).


<h2 id="2">2. Tasks</h2>

<h3 id="2-1"> 2.1 🔬 Molecule-oriented</h3>


<details>
  <summary><b>Molecule description generation</b></summary>
  
- *Please give me some details about this molecule:*
 [C][C][C][C][C][C][C][C][C][C][C][C][C][C][C][C][C][C][=Branch1][C][=O][O][C@H1][Branch2][Ring1][=Branch1][C][O][C][=Branch1][C][=O][C][C][C][C][C][C][C][C][C][C][C][C][C][C][C][C][O][P][=Branch1][C][=O][Branch1][C][O][O][C][C@@H1][Branch1][=Branch1][C][=Branch1][C][=O][O][N]

  ```
  The molecule is a 3-sn-phosphatidyl-L-serine in which the phosphatidyl acyl groups at positions 1 and 2 are specified as stearoyl and arachidonoyl respectively. 
  It is functionally related to an arachidonic acid and an octadecanoic acid.
  ```
</details>

<details>
  <summary><b>Description-guided molecule design</b></summary>
  
- *Create a molecule with the structure as the one described:*
  The molecule is a primary arylamine in which an amino functional group is substituted for one of the benzene hydrogens. It is a primary arylamine and a member of anilines.
  
  ```
  [N][C][=C][C][=C][C][=C][Ring1][=Branch1]
  ```
</details>

<details>
  <summary><b>Forward reaction prediction</b></summary>
  
- *With the provided reactants and reagents, propose a potential product:*
  [O][=N+1][Branch1][C][O-1][C][=C][N][=C][Branch1][C][Cl][C][Branch1][C][I][=C][Ring1][Branch2].[Fe]
  
   ```
  [N][C][=C][N][=C][Branch1][C][Cl][C][Branch1][C][I][=C][Ring1][Branch2]
  ```
</details>

<details>
  <summary><b>Retrosynthesis</b></summary>
  
- *Please suggest potential reactants used in the synthesis of the provided product:*
  [C][=C][C][C][N][C][=Branch1][C][=O][O][C][Branch1][C][C][Branch1][C][C][C]
  
  ```
  [C][=C][C][C][N].[C][C][Branch1][C][C][Branch1][C][C][O][C][=Branch1][C][=O][O][C][=Branch1][C][=O][O][C][Branch1][C][C][Branch1][C][C][C]
  ```
</details>


<details>
  <summary><b>Reagent prediction</b></summary>
  
- *From the provided chemical reaction, propose some possible reagents that could have been used:*
  [C][C][=C][C][Branch1][=Branch2][S][Branch1][C][C][=Branch1][C][=O][=O][=C][C][Branch1][C][C][=C][Ring1][O][C][=Branch1][C][=O][C][Br].[N][C][Branch1][C][N][=S]>>[C][C][=C][C][Branch1][=Branch2][S][Branch1][C][C][=Branch1][C][=O][=O][=C][C][Branch1][C][C][=C][Ring1][O][C][=C][S][C][Branch1][C][N][=N][Ring1][=Branch1]

  ```
  [C][C][O]
  ```
</details>

<details>
  <summary><b>Property prediction</b></summary>
  
- *Please provide the HOMO energy value for this molecule:*
  [C][C][O][C][C][Branch1][C][C][C][Branch1][C][C][C]

  ```
  -0.2482
  ```
</details>


<h3 id="2-2"> 🧬 2.2 Protein-oriented</h3>

<details>
  <summary><b>Protein design</b></summary>
  
- *Design a protein sequence that exhibits the desired activity and specificity.*
1. The presence of Mg(2+) is necessary for the protein to function in the desired environment. 
2. The AMP, (6S)-NADPHX binding site should be located in a region of the protein that is accessible to the ligand. 
3. The designed protein should have ATP binding, NADPHX epimerase activity, metal ion binding, ADP-dependent NAD(P)H-hydrate dehydratase activity to facilitate nicotinamide nucleotide metabolic process. 
4. For general function, the protein need meet that Catalyzes the epimerization of the S- and R-forms of NAD(P)HX, a damaged form of NAD(P)H that is a result of enzymatic or heat-dependent hydration 

  ```
  MSNELVLSREQVRRVDQRAIEAYGVPGIVLMENAGRGAAEIIRAACPSAQRVLIACGPGNNGGDGFVIARHLANAGWMVELLLACPADRITGDAQGNHEIIRRMNLPCAVMADARDLEAANDRFATADVIVDALLGTGASGPPREPIASLIRAINEAHRRVSAQPAPSVFAVDIPSGLDCDTGEAANPTVRADHTITFVARKIGFRNPAARDLLGRVHVVDIGAPRAAIQDALTGKSG
  ```
</details>


<details>
  <summary><b>Catalytic activity prediction</b></summary>
  
- *Please evaluate the following protein sequence and provide an explanation of the enzyme's catalytic activity, including the chemical reaction it facilitates:* MDKVAVAGFLPEELCASLSLSPSFRGNQIFQWIGKGVDSFDAMTNLSAELRASLAEKAILRSTRVSDVLKADDGTVKLQIQTEDDLAVETVLLTDKAARKTACVSCQAGCAMGCAFCKTGTLGLARNLSAAEIVEQFLYLEKHAGALDNIVFMGMGEPLLNLDALRKAIAVLTDKRGRNLSSRRITVSTVGIVSGIYDLANNGPDVRLAVSLTTADETLRRELMPASLTNPLSDLRQAISYYIEKTGKRVTLEAVLLSGKNTSEKNADSLIAFAKGLDVHVNLIPWNPVEGLSFVTPDPEETAQFVSRLEKGGLNVTLRMHRGKSISGACGQLGKTNPYA

  ```
  Based on the provided protein sequence, the enzyme appears to facilitate the chemical reaction: adenosine(37) in tRNA + 2 reduced [2Fe-2S]-[ferredoxin] + 2 S- adenosyl-L-methionine = 2-methyladenosine(37) in tRNA + 5'-   deoxyadenosine + L-methionine + 2 oxidized [2Fe-2S]-[ferredoxin] + S- adenosyl-L-homocysteine.
  ```
</details>


<details>
  <summary><b>Protein function prediction</b></summary>
  
- *Analyze the following amino acid sequence, and determine the function of the resulting protein, its subcellular localization, and any biological processes it may be part of:*
MNGTVNASAPSKMSEVAVERLSNDKALKVIFVLGGPGSGKGTQCAKIAKHFGFTHLSVGDLLRAEINSGSKNGTMIESMINEGKIVRSEVTIKLLQRAMHESGNDKFLIDGFPRNEENRAAFENLEKIEPEFVLFFDCPMEEMERRILNRNQGRDDDKMETIRKRFKVFIESTLPVIEFYNLKGKLYKIDACKPADEVFEDVKAIFSRFRAKEDSSQQTNICTAKRFELVMCLIKRLFREIKRMWSSFFCKAL

  ```
  The protein characterized by the amino acid sequence demonstrates ATP binding, cytidylate kinase activity, uridylate kinase activity and is implicated in the 'de novo' pyrimidine nucleobase biosynthetic process, phosphorylation, pyrimidine nucleotide biosynthetic process. Its subcellular localization is primarily within the cytoplasm, nucleus.
  ```
</details>


<details>
  <summary><b>Functional description generation</b></summary>
  
- *Examine the given protein sequence and share a brief overview of its attributes:*
MKIVLASNNQGKLAELKAMLAPLGVQLLRQAELGIPEAAEPFRTFVENALAKARHASALSGLPALADDAGLCVEAFGGLPGVDTAFYAVQFGYAKGDANNVKALLAQMAGITDRRAALVSTLVAVRSAEDPEPLIACGRVAGEVALEPMGSNGFGFDPVMFIPEFGQTFAQLPVEVKNANSHRGKATRQMMALMRERWIT

  ```
  A concise description of the protein with the specified amino acid sequence includes: Pyrophosphatase that catalyzes the hydrolysis of nucleoside triphosphates to their monophosphate derivatives, with a high preference for the non-canonical purine nucleotides XTP (xanthosine triphosphate), dITP (deoxyinosine triphosphate) and ITP. Seems to function as a house-cleaning enzyme that removes non-canonical purine nucleotides from the nucleotide pool, thus preventing their incorporation into DNA/RNA and avoiding chromosomal lesions.
  ```
</details>

<details>
  <summary><b>Domain/Motif prediction</b></summary>
  
- *Given this protein sequence, can you identify any common protein motifs or domains that it may contain?*
MANTKYIFITGGVVSSLGKGIAAASIGALLESRGLSVSLIKVDPYINVDPGTMSPFQHGEVFVTEDGTETDLDLGHYERFVRFKASKKNNFTAGKVYETVIRNERKGNYLGGTVQVIPHITNEIKKRIKKGGQNKDIAIVEVGGTVGDIESQPFVEALRQMALELPNSSWAFVHLTLVPFINASGELKTKPTQHSVKELRSLGISPDVLVCRSEQELPKDEKNKIALFCSVPAKSVISMHDVDTVYSIPILLNKQKVDDTILKKLNLKIKKPNLNDWKRVVKAKLLPEKEVNVSFVGKYTELKDSYKSINEALEHAGIQNKAKVNINFVEAEQITSQNVRKVLKKSDAILVPGGFGERGIEGMILACKYARENNVPYLGICLGMQIAIIEYARNVLKLKSANSTEFDSSTKFPVIGLITEWSDISGKKEKRTKNSDLGGTMRLGGQVCKLKKKSNSYKMYKKSEIIERHRHRYEVNPNYKDKMIEQGLDVVGTSIDGKLVEMIELPSHKWFLACQFHPEFTSNPRDGHPIFNSYIKSTITK

  ```
  Our predictive analysis of the given protein sequence reveals possible domains or motifs. These include: Glutamine amidotransferase, CTP synthase N-terminal domains.
  ```
</details>


<h3 id="2-3"> 2.3 🥼 Biomolecule text</h3>

<details>
  <summary><b>Chemical entity recognition</b></summary>
  
- *Find and list all the instances of the chemical entities in the following content:*
"Both the control and caramiphen groups with double cannulas had significantly shorter latencies to seizure onset than the corresponding groups with single cannula."
  
  ```
  caramiphen
  ```
</details>


<details>
  <summary><b>Chemical-disease interaction extraction</b></summary>
  
- *You are provided with a set of clinical trial summaries. Extract the chemical-disease relations from the summaries and present your findings in the format of (Subject, Object):*
"Eating disorders and the associated behavioural problems and drug abuse are uncommon in pregnancy. When they do occur they are often unrecognized because of denial but when significant may pose a risk to both the mother and her fetus. This case illustrates a number of problems that may be encountered in women with eating disorders in pregnancy, including prolonged and recurrent metabolic disturbances and diuretic abuse. In particular it illustrates the derangements of thyroid function seen in pregnant women with eating disorders and reminds us that when a cause for thyrotoxicosis remains obscure, thyroxine abuse should be considered and explored."

  ```
  (thyroxine, thyrotoxicosis) 
  ```
</details>


<details>
  <summary><b>Chemical-protein interaction extraction</b></summary>
  
- *Your task is to extract the subject and object entities from the provided text and establish the corresponding relation triples. Please format your answers as (Subject, Relation, Object):*
"Opioid receptors are the membrane proteins that mediate the pain-relieving effect of opioid drugs, such as morphine and fentanyl as well as endogenous opioid peptides enkephalins and endorphins. Using cDNAs for the mu and the kappa opioid receptors, we mapped the chromosomal locations of their genes in mouse. Multilocus cross analysis located the mu receptor gene Oprm on Chr 10 and the kappa receptor gene Oprk1 on Chr 1. Both genes are near centromere, with no markers more centromeric. These data indicate that the two opioid receptors are different gene products, ruling out the possibility that they may be differential splicing products from the same gene."

  ```
  (morphine, regulator, Opioid receptors), (fentanyl, regulator, Opioid receptors)
  ```
</details>


<details>
  <summary><b>Multiple-choice question</b></summary>
  
- *Which of the following conditions does not show multifactorial inheritance? What of the following is the right choice?*
  (A) Pyloric stenosis (B) Schizophrenia (C) Spina bifida (neural tube defects) (D) Marfan syndrome

  ```
  The final answer is (D).
  ```
</details>


<details>
  <summary><b>True or False question</b></summary>
  
- *Does feeding tube insertion and its timing improve survival?*

  ```
  No, neither insertion of PEG tubes nor timing of insertion affect survival.
  ```
</details>


<details>
  <summary><b>Open question</b></summary>
  
- *What virus causes chronic disease?*

  ```
  Hepatitis C virus (HCV).
  ```
</details>


<h2 id="3">3. Demo</h2>

<h3 id="3-1"> 🤗 3.1 Model Weight Release</h3>

We release the model weights on Hugging Face at:

- 🔬 *Molecule-oriented instructions:* [zjunlp/llama-molinst-molecule-7b](https://huggingface.co/zjunlp/llama-molinst-molecule-7b)
- 🧬 *Protein-oriented instructions:* [zjunlp/llama-molinst-protein-7b](https://huggingface.co/zjunlp/llama-molinst-protein-7b)
- 🥼 *Biomolecular text instructions:* [zjunlp/llama-molinst-biotext-7b](https://huggingface.co/zjunlp/llama-molinst-biotext-7b)

<h3 id="3-2"> 📝 3.2 Model Usage Guide</h3>

We have provided a web version demo based on [Gradio](https://gradio.app). To use it, you first need to download this repository:

```shell
>> git clone https://github.com/zjunlp/Mol-Instruction
>> cd Demo
```

Step 1, install Gradio by running：`pip install gradio`. 

Step 2, specify the parameters in the [generate.sh](./Demo/generate.sh) file.

```shell
>> CUDA_VISIBLE_DEVICES=0 python generate.py \
    --interactive False\
    --protein False\
    --load_8bit \
    --base_model $BASE_MODEL_PATH \
    --share_gradio True\
    --lora_weights $FINETUNED_MODEL_PATH \
```

Step 3, run the [generate.sh](./Demo/generate.sh) file in the repository： 

```shell
>> sh generate.sh
```

We offer two methods: the first one is command-line interaction, and the second one is web-based interaction, which provides greater flexibility. 

1. Use the following command to enter **web-based interaction**:
```shell
python generate.py --interactive False
```
  The program will run a web server and output an address. Open the output address in a browser to use it.

2. Use the following command to enter **command-line interaction**:
```shell
python generate.py --interactive True
```
  The disadvantage is the inability to dynamically change decoding parameters.

<p align="center">
  <img alt="Demo" src=gradio_interface_gif.gif style="width: 700px; height: 340px;"/>
</p>

<h3 id="3-3"> 💡 3.3 FAQ</h3>

- Question: What should I do if the model encounters � during decoding?

  Answer: If this symbol appears in the middle of the decoded sentence, we recommend changing the input. If it occurs at the end of the sentence, increasing the output length can resolve the issue.

- Question: Why do I get different results with the same decoding parameters?

  Answer: It is possible that you have enabled `do_sample=True`. It could also be due to the order of execution. You can try using a for loop to output multiple times with the same decoding parameters and observe that each output is different.
  
- Question: Why is the extraction or answer quality not good?

  Answer: Please try changing the decoding parameters.



<h2 id="4">4. Notices</h2>


<h3 id="4-1"> 🚨 4.1. Usage and License</h3>

Please note that all model weights and data of MoLAMA is exclusively licensed for research purposes. The accompanying dataset is licensed under CC BY NC 4.0, which permits solely non-commercial usage. Commercial use is strictly **prohibited**.

<h3 id="4-2"> ⚠️ 4.2. Limitations</h3>


<h2 id="5">5. About</h2>

<h3 id="5-1"> 📚 5.1 References</h3>
If you use our repository, please cite the following related papers:

```
@article{molinst,
  author = {Yin Fang, Xiaozhuan Liang, Ningyu Zhang, Kangwei Liu, Rui Huang, Zhuo Chen, Xiaohui Fan and Huajun Chen},
  title = {Mol-Instructions: A Large-Scale Biomolecular Instruction Dataset for Large Language Models},
  journal = {arXiv preprint}
  year = {2023},
}
```
            
<h3 id="5-2"> 🫱🏻‍🫲🏾 5.2 Acknowledgements</h3>
We appreciate [LLaMA](https://github.com/facebookresearch/llama), [Huggingface Transformers Llama](https://github.com/huggingface/transformers/tree/main/src/transformers/models/llama), [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html), [Alpaca-LoRA](https://github.com/tloen/alpaca-lora), [Chatbot Service](https://github.com/deep-diver/LLM-As-Chatbot) and many other related works for their open-source contributions.
