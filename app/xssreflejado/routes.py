from flask import render_template

from . import xssreflejado


@xssreflejado.route('/')
def index():  # put application's code here
    return render_template('index.html')

@xssreflejado.route("/reflejado1/", methods=["GET","POST"])
def reflejado1():
    return render_template("reflejado1.html")