from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return '''<h1 class="text-center mx-auto mt-4 text-4xl">Netflix says hi</h1>'''

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("helloworld.html",name=name.capitalize())

@app.route("/test")
def test():
    return render_template("test2.html")