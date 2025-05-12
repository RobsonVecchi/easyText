from flask import Flask, render_template, request, redirect, url_for
from models import db, Frase
import webbrowser
from time import sleep
from markupsafe import Markup, escape
import json
import os

app = Flask(__name__)
import os
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frases.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.template_filter('escapejs')
def escapejs_filter(value):
    # Converte para JSON string, o que escapa corretamente pro JavaScript
    return Markup(json.dumps(value)[1:-1])


@app.route('/')
def index():
    frases = Frase.query.all()
    return render_template('index.html', frases=frases)

@app.route('/add', methods=['POST'])
def add():
    titulo = request.form['titulo']
    texto = request.form['texto']
    nova_frase = Frase(titulo=titulo, texto=texto)
    db.session.add(nova_frase)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    frase = Frase.query.get_or_404(id)
    if request.method == 'POST':
        frase.titulo = request.form['titulo']
        frase.texto = request.form['texto']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', frase=frase)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    frase = Frase.query.get_or_404(id)
    db.session.delete(frase)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    sleep(3)
    webbrowser.open("http://127.0.0.1:5000/")
    app.run()
