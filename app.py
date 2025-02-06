from flask import Flask, render_template
app = Flask(__name__)

@app.route("/maggie")
def hello():
    return render_template("maggie.html")


@app.route("/hello")
def html():
    return render_template("hello.html")