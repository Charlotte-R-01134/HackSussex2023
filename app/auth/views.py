from flask import render_template, url_for, redirect, flash, request
from . import auth
from .. import db
from ..models import User
from .forms import RegistrationForm, LoginForm, ChangePasswordForm
from flask_login import login_user, logout_user, login_required, current_user

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in.')
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data): # if the user exists and the password is correct
            login_user(user) # login the user
            next = request.args.get('next') # get the next page
            if next is None or not next.startswith('/'): # if the next page is not valid
                next = url_for('main.index') # redirect to the index page
            return redirect(next) # redirect to the next page
        flash('Invalid username or password.') # flash a message
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    if current_user.is_anonymous:
        flash('You must be logged in to change your password.')
        return redirect(url_for('auth.login'))
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            db.session.commit()
            flash('Your password has been updated.')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid password.')
    return render_template("auth/change_password.html", form=form)
