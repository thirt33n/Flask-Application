from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_sqlalchemy.model import camel_to_snake_case
from sqlalchemy.sql.expression import true
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_required, login_user, logout_user, current_user

from website.models import User


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user1 = User.query.filter_by(username=username).first()
        # print(user1.username)

        if user1:
            if check_password_hash(user1.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user1, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Wrong password try again !', category='error')
        else:
            flash('User does not exist, sign-up now !', category='error')
    return render_template("login.html", user=current_user)


@ auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@ auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(username=username).first()

        if user:
            flash("User already exists!", category='error')
        elif len(username) < 5:
            flash('Username must be more than 5 characters', category="error")
        elif len(name) < 3:
            flash('Name  must be more than 3 characters', category="error")
        elif password1 != password2:
            flash('Your passwords do not match!', category="error")
        elif len(password1) < 7:
            flash('Password must be atleast 8 characters long', category="error")
        else:
            newUser = User(username=username, name=name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(newUser)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account successfully created!', category="success")
            return redirect(url_for("views.home"))

    return render_template("signup.html", user=current_user)
