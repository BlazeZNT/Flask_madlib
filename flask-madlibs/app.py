from flask import Flask,render_template,request
app = Flask(__name__)

from stories import story

@app.route("/")
def madlib():
    required = story.prompts
    return render_template ("homepage.html",ask = required)

@app.route("/story")
def print_story():
    new_dict = {}
    for val in story.prompts:
        new_dict[val] = request.args[val]
    final_story = story.generate(new_dict)
    return render_template("story.html",final_story = final_story)
        

