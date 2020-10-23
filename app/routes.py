import os
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
    pic_directory = os.path.join(app.root_path, 'static/2020-10-20')
    pic_names = os.listdir(pic_directory)
    print(pic_names)
    return render_template('camera.html', pic_names=pic_names)
