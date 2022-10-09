from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.secret_key = "mysecret123456"

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/hello")
def index():
    flash("What's your name")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
   flash("Hi " + str(request.form['name_input']) + ", Great to see you!")
   return render_template("index.html")


if __name__ == '__main__':
    app.run()