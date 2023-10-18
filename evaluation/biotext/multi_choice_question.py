import json

def calculate_accuracy(question_data):
    correct_count = 0
    total_count = len(question_data)
    for i,question in enumerate(question_data):
        correct_answer = question["output"].split("(")[1].split(")")[0]
        my_answer=question["my_output"][0]
        if '(A' in question["my_output"] or 'A)' in question["my_output"] or ' A ' in question["my_output"]:
            my_answer = 'A'
        elif '(B' in question["my_output"] or 'B)' in question["my_output"] or ' B ' in question["my_output"]:
            my_answer = 'B'
        elif '(C' in question["my_output"] or 'C)' in question["my_output"] or ' C ' in question["my_output"]:
            my_answer = 'C'
        elif '(D' in question["my_output"] or 'D)' in question["my_output"] or ' D ' in question["my_output"]:
            my_answer = 'D'
        if correct_answer == my_answer:
                correct_count += 1
    accuracy = (correct_count / total_count) * 100

    return accuracy



output_dir=''
with open(output_dir, "r") as json_file:
    json_data = json.load(json_file)

accuracy = calculate_accuracy(json_data)
print(f"Accuracy: {accuracy/100:.3f}%")

