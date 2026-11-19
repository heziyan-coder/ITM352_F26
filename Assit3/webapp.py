# Assignment 3 - Japan Travel Challenge
# I used AI to help me understand Flask, create routes,
# add difficulty levels and hints, and test the APIs.
# I tested the website and fixed errors myself.
from flask import Flask, render_template, request, session, jsonify, redirect
import json
import random
import time

app = Flask(__name__)
app.secret_key = "japan_quiz_assignment3"

with open("questions.json", "r") as file:
    questions = json.load(file)

@app.route("/")
def index():
    session["score"] = 0
    session["question_number"] = 0
    session["selected_questions"] = []
    session["score_saved"] = False
    session["start_time"] = time.time()
    
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if "selected_questions" not in session:
        return redirect("/")    
    difficulty = request.args.get("difficulty", session.get("difficulty", "easy"))

    if not session.get("selected_questions"):
        available_questions = [
            question for question, data in questions.items()
            if data.get("difficulty") == difficulty
        ]

        if not available_questions:
            return "No questions available for this difficulty."

        session["selected_questions"] = random.sample(
            available_questions,
            min(5, len(available_questions))
        )
        session["difficulty"] = difficulty

    if request.method == "POST":
        answer = request.form.get("answer")
        correct_answer = session.get("correct_answer")
        explanation = session.get("explanation")
        session["question_number"] += 1

        if answer == correct_answer:
            session["score"] += 1
            result = "Correct!"
        else:
            result = f"Incorrect! The correct answer is {correct_answer}."

        return render_template(
            "result.html",
            result=result,
            explanation=explanation
)
    if session["question_number"] >= len(session["selected_questions"]):
        score = session["score"]
        total = len(session["selected_questions"])
        time_taken = round(time.time() - session["start_time"], 1)

        if not session.get("score_saved", False):
            with open("scores.txt", "a") as file:
                file.write(f"{score}/{total}\n")
            session["score_saved"] = True

        return render_template(
            "final.html",
            score=score,
            total=total,
            time_taken=time_taken
)

    question = session["selected_questions"][session["question_number"]]
    data = questions[question]    
    answers = random.sample(data["answers"], len(data["answers"]))

    session["correct_answer"] = data["answers"][0]
    session["explanation"] = data["explanation"]

    return render_template(
        "quiz.html",
        question=question,
        answers=answers,
        difficulty=difficulty,
        hint=data.get("hint", "No hint available.")
    )

@app.route("/api/questions", methods=["GET"])
def get_questions():
    question_list = list(questions.keys())
    return jsonify(question_list)

@app.route("/api/scores", methods=["POST"])
def save_score():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid data"}), 400

    score = data.get("score")
    total = data.get("total")

    if type(score) is not int or type(total) is not int or total <= 0 or score < 0 or score > total:
        return jsonify({"error": "Invalid score"}), 400

    with open("scores.txt", "a") as file:
        file.write(f"{score}/{total}\n")

    return jsonify({"message": "Score saved successfully!"}), 201
if __name__ == "__main__":
    app.run(debug=True, port=5003)
