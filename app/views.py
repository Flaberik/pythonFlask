from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    user:{'nick':'xyi'}
    return render_template("index.html", titile = "home", user = user)
