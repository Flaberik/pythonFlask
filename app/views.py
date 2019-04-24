from flask import render_template, flash, redirect

import hashlib
from app.dbController import dbCon
from app.forms import *

from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from app.models import User, ROLE_USER, ROLE_ADMIN

from app import app

#---------------------------------------------------------------------#
@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
  if g.user is not None and g.user.is_authenticated():
      return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
      session['remember_me'] = form.remember_me.data
      return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
  return render_template('login.html',
      title = 'Sign In',
      form = form,
      providers = app.config['OPENID_PROVIDERS'])

#---------------------------------------------------------------------#
@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))
#---------------------------------------------------------------------#
@app.before_request
def before_request():
    g.user = current_user
    
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
