import json
from sklearn.metrics import precision_recall_fscore_support

def calculate_accuracy(question_data):
    x,y,z=0,0,0
    correct_count = 0
    total_count = len(question_data)
    for i,question in enumerate(question_data):
        correct_answer = question["output"]
        my_answer = question["my_output"]
        correct_first_word = correct_answer.split(',')[0].strip().lower()
        my_first_word = my_answer.split(',')[0].strip().lower()
        if correct_first_word=="no" and my_first_word=="no":
            x+=1
        if correct_first_word=="no":
            y+=1
        if my_first_word=="no":
            z+=1
        if correct_first_word == my_first_word:
            correct_count += 1
    accuracy = (correct_count / total_count) * 100
    return accuracy

def calculate_macro_f1(question_data):
    correct_answers = [question["output"].split(',')[0].strip().lower() for question in question_data]
    my_answers = [question["my_output"].split(',')[0].strip().lower() for question in question_data]
    # Compute precision, recall, and F1-score for each class
    precision, recall, f1, _ = precision_recall_fscore_support(correct_answers, my_answers, labels=["yes", "no", "maybe"], average=None)
    # Calculate macro F1 by averaging F1-scores for all classes
    macro_f1 = sum(f1) / len(f1)

    return macro_f1

output_dir=''
with open(output_dir, "r") as json_file:
    json_data = json.load(json_file)

accuracy = calculate_accuracy(json_data)
print(f"Accuracy: {accuracy/100:.3f}%")

macro_f1 = calculate_macro_f1(json_data)
print(f"Macro F1: {macro_f1:.3f}")
