from flask import Flask, render_template
import os
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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))