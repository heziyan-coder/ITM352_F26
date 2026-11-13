from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://meme-api.com/gimme/wholesomememes"
    response = requests.request("GET", url)
    meme = response.json()

    return render_template(
        "meme.html",
        meme_url=meme["url"],
        subreddit=meme["subreddit"]
    )

if __name__ == '__main__':
    app.run(debug=True, port=5002)