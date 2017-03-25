from flask import Flask, render_template

app = Flask(__name__)

name = "Zui"

@app.route("/")
def index():
    return render_template("index.html", blah={
        'h': "Hello, " + name,
        'y': "and beyond",
        't': "Orochimaru"
    })

@app.route("/blah/")
def blah():
    return "Blah"

if __name__ == "__main__":
    app.run(debug=True)