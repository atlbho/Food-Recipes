import sqlite3

DATABASE = 'database.db'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()



#cursor.execute('''
# CREATE TABLE IF NOT EXISTS recipes (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL
# )
# ''')


# cursor.execute('''
# CREATE TABLE IF NOT EXISTS comments (
#     comment_id INTEGER PRIMARY KEY,
#     comment TEXT NOT NULL,
#     recipe_id INTEGER,
#     FOREIGN KEY(recipe_id) REFERENCES recipes(id)
# )
# ''')


cursor.execute('INSERT INTO recipes (name) VALUES (?)', ('pho',))
cursor.execute('INSERT INTO recipes (name) VALUES (?)', ('tacos',))



cursor.execute('INSERT INTO comments (comment, recipe_id) VALUES (?, ?)', ('Delicious!', 1))
cursor.execute('INSERT INTO comments (comment, recipe_id) VALUES (?, ?)', ('Could use more spice.', 2))

conn.commit()
conn.close()
