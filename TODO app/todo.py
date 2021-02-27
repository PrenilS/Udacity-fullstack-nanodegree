from flask import Flask, render_template, request, url_for, redirect, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class TODO(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=True)

    def __repr__(selfself):
        return f'<Todo {self.id} {self.description}>'

#db.create_all()

@app.route('/todos/create', methods = ['POST'])
def create():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = TODO(description=description, completed=False)
        db.session.add(todo)
        db.session.commit()
        body = {
            'description': todo.description
        }
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify(body)

@app.route('/todos/<todo_id>set-completed', methods = ['POST'])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        todo = TODO.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))



@app.route('/')
def index():
    return render_template('index.html', data=TODO.query.order_by('id').all())

