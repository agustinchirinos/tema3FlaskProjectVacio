from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route("/reflejado1/", methods=["GET","POST"])
def reflejado1():
    return render_template("xssreflejado/reflejado1.html")


if __name__ == '__main__':
    app.run()
