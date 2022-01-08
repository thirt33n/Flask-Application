# Database models are created here  MOdels are like templates or classes

from datetime import timezone
from enum import unique
from . import db
from sqlalchemy.sql import func

from flask_login import UserMixin  # flask in built func used for login purposes


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_data = db.Column(db.String(6969))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 'user' refers to tehe User class , since SQLAlchemy refers to classes in lowercase while in ForeignKey method


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(169))
    notes = db.relationship('Notes')
    # SQLALchemy needs the exact class name when using relationship() method
