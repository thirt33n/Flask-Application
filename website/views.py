from flask import Blueprint,render_template



views = Blueprint('views',__name__)

@views.route('/')                               #@ should be succeeded by the variable of the Blueprint() func
def home():
    return render_template("home.html")
    