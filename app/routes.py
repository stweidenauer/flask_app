from flask import render_template
from app import app


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/camera')
def camera():
    return render_template('camera.html')
