import json
import re

def calculate_f1_score(true_entities, predicted_entities):
    pattern = r'\(.*?\)'
    true_entities = re.findall(pattern, true_entities)
    predicted_entities = re.findall(pattern, predicted_entities)

    true_entities = set(true_entities)
    predicted_entities = set(predicted_entities)
    true_positive = len(true_entities & predicted_entities)
    precision = true_positive / len(predicted_entities) if len(predicted_entities) > 0 else 0
    recall = true_positive / len(true_entities) if len(true_entities) > 0 else 0
    
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    # print(true_entities,predicted_entities,f1_score)
    return f1_score

def calculate_accuracy(question_data):
    correct_count = 0
    total_count = len(question_data)
    for i,question in enumerate(question_data):
        true_output = question['output'].lower()
        my_output = question['my_output'].lower()
        f1_score = calculate_f1_score(true_output, my_output)
        # print(f1_score)
        correct_count+=f1_score

    return correct_count/total_count




output_dir=''
with open(output_dir, "r") as json_file:
    json_data = json.load(json_file)
accuracy = calculate_accuracy(json_data)
print(f"F1: {accuracy:.3f}")


