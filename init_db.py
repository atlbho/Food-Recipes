import sqlite3

DATABASE = 'database.db'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

# Insert sample data
cursor.execute('INSERT INTO recipes (name) VALUES (?)', ('pho',))
cursor.execute('INSERT INTO recipes (name) VALUES (?)', ('tacos',))

conn.commit()
conn.close()
