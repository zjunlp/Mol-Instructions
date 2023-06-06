### Web Demo

Step 1, install Gradio by running：`pip install gradio`. 

Step 2, specify the parameters in the [generate.sh](generate.sh) file.

```shell
CUDA_VISIBLE_DEVICES=0 python generate.py \
    --protein False\
    --load_8bit \
    --base_model $BASE_MODEL_PATH \
    --share_gradio True\
    --lora_weights $FINETUNED_MODEL_PATH \
```

Step 3, run the [generate.sh](generate.sh) file in the repository： 

```shell
sh generate.sh
```

The program will run a web server and output an address. Open the output address in a browser to use it.

<p align="center">
  <img alt="Demo" src=../gradio_interface_gif.gif style="width: 700px; height: 340px;"/>
</p>