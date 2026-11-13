

from flask import Flask, render_template, request, session
import json
import random

app = Flask(__name__)
app.secret_key = "japan_quiz_lab13"

with open("questions.json", "r") as file:
    questions = json.load(file)


@app.route("/")
def home():
    return render_template("quiz_home.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        answer = request.form.get("answer")
        correct_answer = session.get("correct_answer")
        explanation = session.get("explanation")

        if answer == correct_answer:
            result = "Correct!"
        else:
            result = f"Incorrect! The correct answer is {correct_answer}."

        return render_template(
            "result.html",
            result=result,
            explanation=explanation
        )

    question, data = random.choice(list(questions.items()))
    answers = random.sample(data["answers"], len(data["answers"]))

    session["correct_answer"] = data["answers"][0]
    session["explanation"] = data["explanation"]

    return render_template(
        "quiz.html",
        question=question,
        answers=answers
    )


if __name__ == "__main__":
    app.run(debug=True, port=5003)
