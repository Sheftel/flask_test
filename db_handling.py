import psycopg2
import psycopg2.extras
from werkzeug.exceptions import abort


def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="mysecretpassword")
    return conn

def get_post_all():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM posts')
    posts = cur.fetchall()
    cur.close()
    conn.close()
    return posts

def get_post(post_id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM posts WHERE id = %s',
                (post_id,))
    post_l = cur.fetchone()
    cur.close()
    conn.close()
    if post_l is None:
        abort(404)
    return post_l


def set_post(title, content):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('INSERT INTO posts (title, content) VALUES (%s, %s)',
                (title, content))
    conn.commit()
    conn.close()


def edit_post(title, content, post_id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('UPDATE posts SET title = %s, content = %s'
                ' WHERE id = %s',
                (title, content, post_id))
    conn.commit()
    conn.close()


def delete_post(post_id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('DELETE FROM posts WHERE id = %s', (post_id,))
    conn.commit()
    conn.close()
