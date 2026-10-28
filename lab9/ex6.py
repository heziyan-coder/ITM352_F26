import json

with open("quiz_questions.json", "r") as file:
    quiz_questions = json.load(file)

print(quiz_questions)