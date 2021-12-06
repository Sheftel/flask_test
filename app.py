import psycopg2
import psycopg2.extras

import db_handling
from configmodule import *
from flask import Flask, render_template, request, url_for, flash, redirect
from db_handling import *
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config.from_object(DevelopmentConfig())


@app.route('/')
def index():
    posts = db_handling.get_post_all()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post_l = get_post(post_id)
    return render_template('post.html', post=post_l)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            db_handling.set_post(title, content)
            return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/<int:post_id>/edit', methods=('GET', 'POST'))
def edit(post_id):
    post = get_post(post_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required!')
        else:
            db_handling.edit_post(title, content, post_id)
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)


@app.route('/<int:post_id>/delete', methods=('POST',))
def delete(post_id):
    post = get_post(post_id)
    db_handling.delete_post(post_id)
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))
