from flask import render_template, request, url_for, flash, redirect, Blueprint
from .extensions import db
from .models import Post

bp = Blueprint('posts', __name__)


@bp.route('/')
def index():
    posts = db.session.query(Post).all()
    return render_template('index.html', posts=posts)


@bp.route('/<int:post_id>')
def post(post_id):
    post_x = db.session.query(Post).get(post_id)
    return render_template('post.html', post=post_x)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            db.session.add(Post(title=title,content=content))
            db.session.commit()
            return redirect(url_for('posts.index'))
    return render_template('create.html')


@bp.route('/<int:post_id>/edit', methods=('GET', 'POST'))
def edit(post_id):
    post = db.session.query(Post).get(post_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required!')
        else:
            post.title = title
            post.content = content
            db.session.commit()
            return redirect(url_for('posts.index'))
    return render_template('edit.html', post=post)


@bp.route('/<int:post_id>/delete', methods=('POST',))
def delete(post_id):
    post = db.session.query(Post).get(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('"{}" was successfully deleted!'.format(post.title))
    return redirect(url_for('posts.index'))



