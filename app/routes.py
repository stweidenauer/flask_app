import os, random
from flask import render_template, flash, url_for, redirect
from flask_login import login_user, login_required, logout_user
from app import app, db, bcrypt
from app.forms import LoginForm, RegisterForm, WordBookForm, VocTestForm
from app.models import User, WordBook


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check Data!')
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account has been created', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


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
@login_required
def camera():
    pic_dic = make_dic_pic()
    sor_key_list = sorted(pic_dic)
    return render_template('camera.html', pic_dic=pic_dic, sor_key_list=sor_key_list)


@app.route('/camera/<date_key>')
def camera_oneday(date_key):
    pic_dic = make_dic_pic()
    return render_template('camera_one.html', pic_dic=pic_dic, date_key=date_key)


@app.route('/wordbook', methods=['GET', 'POST'])
def wordbook():
    form = WordBookForm()
    if form.validate_on_submit():
        entry = WordBook(engl=form.engl.data, german=form.german.data)
        db.session.add(entry)
        db.session.commit()
        form.engl.data = " "
        form.german.data = " "
        flash(f'Your Words are stored', 'success')
    return render_template('wordbook.html', form=form)


@app.route('/allwords', methods=['GET', 'POST'])
def allwords():
    content = WordBook.query.order_by(WordBook.engl.desc())  # desc
    return render_template('allwords.html', content=content)


@app.route('/delete_word/<string:word>')
def delete_word(word):
    entry = WordBook.query.filter_by(engl=word).first()
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('allwords'))


@app.route('/voc_test', methods=['GET', 'POST'])
def voc_test():
    content = WordBook.query.all()
    check_word = random.choice(content)
    word_id = check_word.id
    print(id)
    return redirect(url_for("voc_test_2", word_id=word_id))


@app.route('/voc_test_2/int:<word_id>', methods=['GET', 'POST'])
def voc_test_2(word_id):
    form = VocTestForm()
    test_word = WordBook.query.filter_by(id=word_id).first()
    print(test_word.german)
    if form.validate_on_submit():
        print(F"Testword deutsch = {test_word.german}")
        print(F"Testword english = {test_word.engl}")
        print(F"Data = {form.data}")
        print(test_word.german == form.data)
        if form.german.data == str(test_word.german):
            return redirect(url_for('answer', word="Correct"))
        else:
            return redirect(url_for('answer', word="Wrong"))
    return render_template('voc_test_2.html', form=form, test_word=test_word)


@app.route('/answer/<string:word>', methods=['GET', 'POST'])
def answer(word):
    return render_template('answer.html', word=word)
