from flask import Flask, render_template, request

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


@app.route("/data")
def data():
    return request.args.get('name') or "Nothing here"

if __name__ == "__main__":
    app.run(debug=True)