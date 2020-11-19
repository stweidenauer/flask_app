import os
from flask import render_template
from app import app
from flask_sqlalchemy import SQLAlchemy



@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


def make_dic_pic():
    # where the folders with the pictures live
    pic_folders = os.path.join(app.root_path, 'static')
    # all directories with current dates
    directories_current_dates = [r for r in os.listdir(pic_folders) if r.startswith('20')]
    # build dictionary with date as key and pictures as values
    pic_dic = {}
    for item in directories_current_dates:
        pic_dic[item] = os.listdir(os.path.join(pic_folders, item))
        pic_dic[item].sort()
    return pic_dic


@app.route('/camera')
def camera():
    pic_dic = make_dic_pic()
    sor_key_list = sorted(pic_dic)
    return render_template('camera.html', pic_dic=pic_dic, sor_key_list=sor_key_list)


@app.route('/camera/<date_key>')
def camera_oneday(date_key):
    pic_dic = make_dic_pic()
    return render_template('camera_one.html', pic_dic=pic_dic, date_key=date_key)