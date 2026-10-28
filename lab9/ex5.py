import json

with open("questions.json", "r") as file:
    quiz_questions = json.load(file)

with open("quiz_questions.json", "w") as file:
    json.dump(quiz_questions, file, indent=4)

print("Quiz questions saved successfully!")