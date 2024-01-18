from flask import Flask, request, render_template
from stories import stories
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "password"
app.debug=True

debug = DebugToolbarExtension(app)

@app.route("/")
def display_stories():
    return render_template("stories.html", stories=stories.values())

@app.route("/forms")
def display_forms():
    story = stories[request.args["story_id"]]
    return render_template("forms.html", prompts=story.prompts, story_id=request.args["story_id"])

@app.route("/madlib")
def display_madlib():
    story = stories[request.args["story_id"]]
    words = story.generate(request.args)
    return render_template("madlib.html", words=words)