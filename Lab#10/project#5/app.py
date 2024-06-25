from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@app.route('/note/<int:note_id>')
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    return render_template('view_note.html', note=note)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        content = request.form['content']
        
        new_note = Note(title=title, description=description, content=content)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('add_note.html')

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
