# Japan Travel Challenge
# A travel quiz game about Japan
# Make a dictionary with the questions and correct answers
# Allow the user to choose the option by its label
# Improve the look and usability. Keep track of correct answers.
# Randomize the order of the questions and the order of the answers for each question.
# Refactor the code to use functions.

from string import ascii_lowercase
import random
import json

question_file = open("questions.json", "r")
questions = json.load(question_file)


NUM_QUESTIONS_PER_QUIZ = 5

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def get_answer(question, alternatives):
    labeled_answers = dict(zip(ascii_lowercase, alternatives))

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")
        
    while (answer_label := input("Choice? ").lower()) not in labeled_answers:
        print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}.")

    answer = labeled_answers.get(answer_label)
    return labeled_answers[answer_label]


def ask_question(question, data):
    alternatives = data["answers"] 
    correct_answer = alternatives[0]
    explanation = data["explanation"]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))
    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("Correct!")
        print(f"Explanation: {explanation}")
        return 1
    else:
        print(f"The correct answer is {correct_answer}, not {answer}.")
        print(f"Explanation: {explanation}")
        return 0


# Main program logic starts here
print("Welcome to Japan Travel Challenge!")

questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)

num_correct = 0

# Main Loop
for num, (question, answers) in enumerate(questions, start=1):
    print(f"\nQuestion {num}: {question}")
    num_correct += ask_question(question, answers)

print(f"\nYou got {num_correct} correct.")
if num_correct == 5:
    print("Travel Rank: Japan Expert!")
elif num_correct >= 3:
    print("Travel Rank: Smart Traveler!")
else:
    print("Travel Rank: Beginner Traveler!")

score_file = open("scores.txt", "r")
scores = score_file.readlines()
score_file.close()

high_score = 0

for score in scores:
    points = int(score.split("/")[0])
    if points > high_score:
        high_score = points

if num_correct > high_score:
    print("New High Score!")

score_file = open("scores.txt", "a")
score_file.write(f"{num_correct}/5\n")
score_file.close()