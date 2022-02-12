from flask import Flask, render_template, request



app = Flask(__name__)


from .xssreflejado import xssreflejado

def create_app():
    app.register_blueprint(xssreflejado)
    return  app