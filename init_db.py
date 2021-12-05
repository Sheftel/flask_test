import psycopg2 as psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="mysecretpassword")

cur = conn.cursor()
cur.execute("INSERT INTO posts (title, content) VALUES (%s,%s)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (%s,%s)",
            ('Second Post', 'Content for the second post')
            )

conn.commit()
cur.close()

