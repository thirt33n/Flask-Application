from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Notes
from . import db

import json

views = Blueprint('views', __name__)

# @ should be succeeded by the variable of the Blueprint() func

SQLALCHEMY_TRACK_MODIFICATIONS = False


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        new_note = Notes(text_data=note, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)  # can be text_data
    noteId = note['noteId']
    note = Notes.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
