# -*- coding: UTF-8 -*-

from form import SearchForm, LoginForm, ReviewForm
from db import BookDatabase

import os

from flask import Flask, request, sessions, redirect, url_for, render_template, send_from_directory
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user, current_user

import six

if six.PY2:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')


app = Flask(__name__)
app.secret_key = b'\xfd_W9\xd6_\xee\x0e\x18l\x88\x1fl>=\x97'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return '<{}, {}, {}>'.format(self.id, self.username, self.password)

    def is_authenticated(self):
        return True


@app.route('/home', methods=['GET'])
@login_required
def home():
    searchForm = SearchForm()
    db = BookDatabase()
    reviews_list = db.get_reviews_by_user_id(current_user.id)
    book_list = db.get_book_list_by_like_user_id(current_user.id)
    return render_template('home.html', user=current_user, reviews_list=reviews_list, book_list=book_list, form=searchForm, active='home')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search', book_name=form.book_name.data))
    return render_template('index.html', form=form, active='index')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='favicon.icon')


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    searchForm = SearchForm()
    state = True
    if loginForm.validate_on_submit():
        submit_form = request.form
        username = submit_form['username']
        password = submit_form['password']
        # ========================================
        #          validate user's login
        # ========================================        
        db = BookDatabase()
        state = db.validate_login(username, password)
        # print(username)
        if state == True:
            user_id, _, _ = db.get_user_info_by_username(username)
            # print(user_id)
            user = User(user_id, username, password)
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html', loginform=loginForm, form=searchForm, state=state, active='login')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@login_manager.user_loader
def load_user(id):
    db = BookDatabase()
    result = db.get_user_info_by_id(id)
    if type(result) == tuple:
        user_id, username, password = result
        return User(user_id, username, password)


@app.route('/search', methods=['GET', 'POST'])
def search_front():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search', book_name=form.book_name.data))
    return render_template('search.html', form=form, active="search")


@app.route('/search?book_name=<book_name>')
def search(book_name):
    db = BookDatabase()
    searchKey = book_name
    book_list = db.search_with_book_name(book_name)
    form = SearchForm()
    return render_template('search.html', title='Search Result', form=form, book_list=book_list, searchKey=searchKey,
                           active="search")


@app.route('/book')
def book_list():
    db = BookDatabase()
    book_list = db.get_book_list(0)
    form = SearchForm()
    return render_template('search.html', title='Book', form=form, book_list=book_list, searchKey=None, active="book")


@app.route('/book?book_id=<book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    db = BookDatabase()
    searchKey = book_id
    book_list = db.get_book_detail(book_id)
    reviews_list = db.get_reviews_by_book_id(book_id)
    like_list = []
    if current_user.is_authenticated:
        like_list = db.get_like_list_by_user_id(current_user.id)
    form = SearchForm()
    reviewForm = ReviewForm()
    if reviewForm.validate_on_submit():
        db.insert_reivews(current_user.id, book_id, reviewForm.review_content.data)
        return redirect('/book%3Fbook_id%3D{}'.format(book_id))
    return render_template('book.html', form=form, reviewForm = reviewForm, book_list=book_list, like_list=like_list, reviews_list=reviews_list, searchKey=searchKey, book_id=book_id,
                           active="book")


@app.route('/serie')
def serie_list():
    db = BookDatabase()
    serie_list = db.get_serie_list(0)
    form = SearchForm()
    return render_template('serie.html', title='Serie', form=form, serie_list=serie_list, searchKey=None,
                           active="serie")


@app.route('/serie?serie_id=<serie_id>')
def serie_detail(serie_id):
    db = BookDatabase()
    serie_list = db.get_serie_detail(serie_id)
    searchKey = serie_list[0][2]
    volumes = (len(serie_list), serie_list[0][5])
    form = SearchForm()
    return render_template('serie_detail.html', form=form, serie_list=serie_list, searchKey=searchKey, volumes=volumes,
                           active="serie")


@app.route('/author')
def author_list():
    db = BookDatabase()
    author_list = db.get_author_list(0)
    form = SearchForm()
    return render_template('author.html', title='Author', form=form, author_list=author_list, searchKey=None,
                           active="author")


@app.route('/author?author_id=<author_id>')
def author_detail(author_id):
    db = BookDatabase()
    author_list = db.get_author_detail(author_id)
    book_list = db.get_book_list_by_author_id(author_id)
    searchKey = author_list[0][1]
    form = SearchForm()
    return render_template('author_detail.html', form=form, author_list=author_list, book_list=book_list,
                           searchKey=searchKey, active="author")


@app.route('/publisher')
def publisher_list():
    db = BookDatabase()
    publisher_list = db.get_publisher_list(0)
    form = SearchForm()
    return render_template('publisher.html', title='Author', form=form, publisher_list=publisher_list, searchKey=None,
                           active="publisher")


@app.route('/publisher?publisher_id=<publisher_id>')
def publisher_detail(publisher_id):
    db = BookDatabase()
    publisher_list = db.get_publisher_detail(publisher_id)
    book_list = db.get_book_list_by_publisher_id(publisher_id)
    searchKey = publisher_list[0][1]
    form = SearchForm()
    return render_template('publisher_detail.html', form=form, publisher_list=publisher_list, book_list=book_list,
                           searchKey=searchKey, active="publisher")


@app.route('/reviews')
def reviews():
    db = BookDatabase()
    review_list = db.get_reviews()
    like_list = []
    if current_user.is_authenticated:
        like_list = db.get_like_list_by_user_id(current_user.id)
    form = SearchForm()
    return render_template('reviews.html', form=form, review_list=review_list, like_list=like_list, active="reviews")

@app.route('/delete?review_id=<review_id>&next=<origin_url>')
@login_required
def delete_review(review_id,origin_url):
    db = BookDatabase()
    db.delete_review(review_id,current_user.id)
    print(origin_url)
    return redirect(origin_url)

@app.route('/like?like_type=<like_type>&review_id=<review_id>')
@login_required
def likes_review(like_type, review_id):
    db = BookDatabase()
    if like_type == 'add':
        db.add_like_review(review_id,current_user.id)
    elif like_type == 'del':
        db.del_like_review(review_id,current_user.id)
    return redirect('/empty')

@app.route('/empty')
def redic():
    return render_template('empty.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
