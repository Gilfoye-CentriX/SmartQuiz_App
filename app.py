from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

# Load questions from JSON files
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

@app.route('/python_quiz')
def python_quiz():
    return render_template('python_quiz.html')
    
@app.route('/javascript_quiz')
def javascript_quiz():
    return render_template('javascript_quiz.html')
    
@app.route('/cpp_quiz')
def cpp_quiz():
    return render_template('cpp_quiz.html')

@app.route('/api/questions')
def api_python_questions():
    questions = load_python_questions()
    random.shuffle(questions)  # Shuffle the questions
    return jsonify(questions)

@app.route('/api/javascript_questions')
def api_javascript_questions():
    questions = load_javascript_questions()
    random.shuffle(questions)  # Shuffle the questions
    return jsonify(questions)

@app.route('/api/cpp_questions')
def api_cpp_questions():
    questions = load_cpp_questions()
    random.shuffle(questions)  # Shuffle the questions
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)
