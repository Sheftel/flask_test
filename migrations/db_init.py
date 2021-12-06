from db_handling import get_connection


conn = get_connection()
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS posts;
    CREATE TABLE posts (
        id SERIAL PRIMARY KEY,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    );""")

cur.execute("INSERT INTO posts (title, content) VALUES (%s,%s)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (%s,%s)",
            ('Second Post', 'Content for the second post')
            )

conn.commit()
cur.close()
conn.close()
