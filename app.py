from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import json
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = '8427356'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    full_name = db.Column(db.String(150), nullable=False, default='anonymous')
    email = db.Column(db.String(150), nullable=False, unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def load_python_questions():
    with open('python_questions.json') as file:
        return json.load(file)

def load_javascript_questions():
    with open('javascript_questions.json') as file:
        return json.load(file)

def load_cpp_questions():
    with open('cpp_questions.json') as file:
        return json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password)
        new_user = User(full_name=full_name, email=email, username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_id = request.form.get('username') or request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter((User.username == login_id) | (User.email == login_id)).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username/email and password', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', full_name=current_user.full_name)

@app.route('/python_quiz')
@login_required
def python_quiz():
    return render_template('python_quiz.html')

@app.route('/javascript_quiz')
@login_required
def javascript_quiz():
    return render_template('javascript_quiz.html')

@app.route('/cpp_quiz')
@login_required
def cpp_quiz():
    return render_template('cpp_quiz.html')

@app.route('/results')
@login_required
def results():
    return render_template('results.html', full_name=current_user.full_name)

@app.route('/api/python_questions')
@login_required
def api_python_questions():
    questions = load_python_questions()
    random.shuffle(questions)
    return jsonify(questions)

@app.route('/api/javascript_questions')
@login_required
def api_javascript_questions():
    questions = load_javascript_questions()
    random.shuffle(questions)
    return jsonify(questions)

@app.route('/api/cpp_questions')
@login_required
def api_cpp_questions():
    questions = load_cpp_questions()
    random.shuffle(questions)
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)
