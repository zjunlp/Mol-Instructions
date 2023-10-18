import json
from bert_score import score

output_dir=''

with open(output_dir, 'r') as f:
    data = json.load(f)

predictions = [entry['my_output'] for entry in data]
references = [entry['output'] for entry in data]

P, R, F1 = score(predictions, references, lang="en", verbose=True)
print(f"{sum(F1)/len(F1):.3f}")
