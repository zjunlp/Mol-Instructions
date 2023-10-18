import json
import nltk
from nltk.translate.bleu_score import sentence_bleu

output_dir=''
with open(output_dir, 'r') as f:
    data = json.load(f)

predictions = [entry['my_output'] for entry in data]
references = [entry['output'] for entry in data]

total_bleu = 0.0
for pred, ref in zip(predictions, references):
    pred_tokens = pred.lower().split()
    ref_tokens = ref.lower().split()
    bleu = sentence_bleu([ref_tokens], pred_tokens)
   
    total_bleu += bleu

average_bleu = total_bleu / len(predictions)

print(f"BLEU score: {average_bleu:.3f}")
