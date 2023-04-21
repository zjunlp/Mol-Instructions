# molama

⚗️ Welcome to the MoLAMA project repository! MoLAMA is a large-scale molecular language model that possesses the ability to understand 🧑🏻‍🔬human language and 🔬molecular language, which can assist communities in conducting research in the field of molecular science.

🚨 **Usage and License Notices**: Please note that MoLAMA is exclusively licensed for research purposes. The accompanying dataset is licensed under CC BY NC 4.0, which permits solely non-commercial usage. Commercial use is strictly **prohibited**.

## Overview


### Model Release
huggingface link (7B)

## Demo

gif

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
Then run
```sh
>> ./chat
```

