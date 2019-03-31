from flask import Flask, render_template,request

import time


app = Flask(__name__)

@app.route("/")
def index():
    result=""
    return render_template("index.html", result=result)

@app.route("/guess", methods=["POST"])
def guess():
    result=""
    answer="Paris"
    guess=request.form.get("guess")
    if guess==answer:
        result="Correct, the answer is " + answer
    else:
        result="Inorrect, the answer is not " + guess + " - it is " + answer

    return render_template("index.html", result=result)






