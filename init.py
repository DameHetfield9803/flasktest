from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("helloworld.html",name=name)

@app.route("/test")
def test():
    return render_template("test2.html")

@app.route("/karl")
def karl():
    return render_template("index.html")