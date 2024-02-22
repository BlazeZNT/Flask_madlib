from flask import Flask,render_template,request
app = Flask(__name__)

from stories import story

@app.route("/")
def madlib():
    required = story.prompts
    return render_template ("homepage.html",ask = required)

# @app.route("/story")
# def print_story():
#     return render_template ("story.html")