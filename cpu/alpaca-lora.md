## How to run Alpaca.cpp on your own macbook?



The steps are as follows:

1  git clone https://github.com/antimatter15/alpaca.cpp

2  cd alpaca.cpp

3  make chat

4 Download [ggml-alpaca-7b-q4.bin](https://huggingface.co/Sosaka/Alpaca-native-4bit-ggml/blob/main/ggml-alpaca-7b-q4.bin) and place it in the same folder as the chat executable in the file

5 ./chat  



The screencast below is not sped up and running on an M1 MacBook Pro.





Here is the text version of the Q&A

```
Tell me about alpacas.
Alpacas are small, domesticated camelids from South America and were first bred in Peru around 5000 years ago. They have a long neck, two humps on their backs, and can weigh up to 240 kg (300 lb). Alpacas produce cashmere wool which is softer than silk and warmer than down. Their fleece comes in more than 15 natural colors including white, brown, black, grey, silver, and gold. They are also very social animals that live together in herds with a dominant male leader. Alpacas have become increasingly popular as pets or for their fiber production around the world due to their gentle nature, low maintenance requirements, and ability to thrive on minimal resources.
> Tell me about the president of Mexico in 2019.
In 2019, Andres Manuel Lopez Obrador was elected President of Mexico after having served as a federal legislator since 2006 and previously serving two terms as mayor of Mexico City from 2000 to 2005. He is the first left-leaning president in recent Mexican history, promising an end to corruption and impunity while pushing for economic reforms that would benefit low income citizens through increased social spending.
> Write a Python program that prints the first 10 Fibonacci numbers.
def Fibonacci(n):  
    if n<0 : print("Incorrect input") #If negative, output incorrect input message    
      
    elif n==1: return 0
     
    elseif n ==2:return 1
          
print('The first ', end='')#Prints the Fibonacci numbers as a sequence  
for i in range(3): #Start from third number, since it is zero based.    
    print(Fibonacci(i),end = ' ')
```

You can see that the first and 2nd questions were answered pretty well, and the third code question was a bit poor. Overall the model is not very bad.
