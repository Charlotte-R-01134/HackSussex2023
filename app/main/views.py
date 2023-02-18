from . import main
from flask import render_template, flash
from flask_login import login_required, current_user, logout_user
from .. import db
from ..models import User

@main.route('/')
def index():
    flash('hi')
    return render_template('index.html')