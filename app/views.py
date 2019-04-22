from flask import render_template, flash, redirect

import hashlib
<<<<<<< HEAD
import app.dbController

=======
from app.dbController import dbCon
>>>>>>> 79208a8d644f46b9927ccca0617149744ad14c1f
from app.forms import *

from app import app

#---------------------------------------------------------------------#
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form)

#---------------------------------------------------------------------#
@app.route('/signup', methods = ['GET', 'POST'])
def signin():
    form = SignUp()
    db = dbCon()
    if form.validate_on_submit():
        if str(form.pass_one.data) == str(form.pass_two.data):
            dbController.sign_up(form.login, hashlib.md5(form.pass_one.data))
            flash('registration complite')
            return redirect('/index')
    return render_template('signup.html', title = 'Sign Up', form = form)

#---------------------------------------------------------------------#
@app.route('/')
@app.route('/index')
def index():

    user = {'name':'xyi'}

    posts = [
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]


    return render_template("index.html", title = "home", posts = posts, user = user)
