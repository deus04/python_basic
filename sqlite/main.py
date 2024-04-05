import sqlite3


with sqlite3.connect('database.db') as conn:
    coursor = conn.cursor()
    coursor.execute('SELECT * FROM students;')
    print(coursor.fetchall())
    conn.commit()
