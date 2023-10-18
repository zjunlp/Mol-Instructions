import evaluate
import json


rouge = evaluate.load("rouge")

with open('general_functions.json', 'r') as f:
    examples = json.load(f)


target_list = [example['target'] for example in examples]
response_list = [example['response'] for example in examples]

results = rouge.compute(predictions=response_list, references=target_list)
print(results)