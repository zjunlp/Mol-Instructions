from rouge import Rouge
import json

output_dir=''

with open(output_dir, 'r') as f:
    data = json.load(f)

predictions = [entry['my_output'] for entry in data]
references = [entry['output'] for entry in data]
rouge = Rouge()
total_rouge = 0.0 
for pred, ref in zip(predictions, references):
    scores = rouge.get_scores(pred, ref)
    total_rouge+=scores[0]['rouge-1']['f']
average_rouge = total_rouge / len(predictions)

print(f"rouge score: {average_rouge:.3f}")
