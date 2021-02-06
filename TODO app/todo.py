from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class TODO(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(selfself):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/todos/create', methods = ['POST'])
def create():
    description = request.form.get('description')
    todo = TODO(description = description)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))



@app.route('/')
def index():
    return render_template('index.html', data=TODO.query.all())

