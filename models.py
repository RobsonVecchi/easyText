from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Frase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    texto = db.Column(db.Text, nullable=False)
