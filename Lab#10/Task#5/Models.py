from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
