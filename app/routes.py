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
    # pic_directory = os.path.join(app.root_path, 'static')
    # all directories with current dates = [r for r in os.listdir(pic_directory) if r.startswith('20')]
    # Idee Dictonary mit Date als schlüssel und eine liste der Bilder als data
    # for item in directory with current dates:
    #     dicy[item] = os.listdir(os.path.join(item))
    pic_directory = os.path.join(app.root_path, 'static')
    pic_names = os.listdir(pic_directory)
    pic_names.sort()
    print(pic_names)
    return render_template('camera.html', pic_names=pic_names)
