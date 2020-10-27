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
    # where the folders with the pictures live
    pic_folders = os.path.join(app.root_path, 'static')
    # all directories with current dates
    directories_current_dates = [r for r in os.listdir(pic_folders) if r.startswith('20')]
    # build dictionary with date as key and pictures as values
    pic_dic = {}
    for item in directories_current_dates:
        pic_dic[item] = os.listdir(os.path.join(pic_folders, item))

    print(pic_dic)

    return render_template('camera.html', pic_dic=pic_dic)
