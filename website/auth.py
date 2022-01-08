from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(username) < 5:
            flash('Username must be more than 5 characters', category="error")
        elif len(name) < 3:
            flash('Name  must be more than 3 characters', category="error")
        elif password1 != password2:
            flash('Your passwords do not match!', category="error")
        elif len(password1) < 7:
            flash('Password must be atleast 8 characters long', category="error")
        else:

            flash('Account successfully created!', category="success")

    return render_template("signup.html")
