import psycopg2
import psycopg2.extras
from werkzeug.exceptions import abort


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="mysecretpassword")
    return conn


def get_post(post_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM posts WHERE id = %s',
                (post_id,))

    post_l = cur.fetchone()
    cur.close()
    conn.close()
    if post_l is None:
        abort(404)
    return post_l

