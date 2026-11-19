# Assignment 3 – Japan Travel Challenge

## Project Description
Japan Travel Challenge is a quiz website built with Python and Flask. Players can answer questions about Japan and test their knowledge.

## How to Run
1. Open the Assit3 folder in VS Code.
2. Make sure Flask is installed.
3. Run `python3 webapp.py` in the terminal.
4. Open `http://127.0.0.1:5003` in a browser.

## Features
- The quiz randomly selects questions and shuffles the answers.
- Players answer 5 questions in each game.
- The website shows if an answer is correct or incorrect.
- Players can see explanations after answering.
- The final page shows the score, correct answers, incorrect answers, time taken, and travel rank.
- Scores are stored in `scores.txt`.
- The website has a GET API for questions and a POST API for scores.
- The website checks for invalid score data.

## Individual Requirement #4: Difficulty Levels
Players can choose Easy, Medium, or Hard. The quiz selects questions based on the chosen difficulty.

## Individual Requirement #5: Hint System
Players can click the Show Hint button to get help with a question.

## Testing
I tested the quiz by playing several games. I checked the scores, answers, hints, difficulty levels, and final results.

I also tested the question API in my browser and the score API using the terminal.

## AI Usage
I used AI to help me understand Flask, create some code, and fix errors. I tested the website myself and made changes when something did not work.

Example prompts:
- "Help me turn my Python quiz into a Flask website."
- "How can I add difficulty levels?"
- "How can I show hints for quiz questions?"
- "How do I test my Flask API?"

## Files
- `webapp.py` – Flask application
- `questions.json` – Quiz questions and answers
- `scores.txt` – Saved scores
- `templates/index.html` – Home page
- `templates/quiz.html` – Quiz page
- `templates/result.html` – Answer feedback
- `templates/final.html` – Final results