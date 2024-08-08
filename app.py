from flask import Flask, g, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    db = get_db()
    cursor = db.execute('SELECT * FROM recipes')
    rows = cursor.fetchall()
    return render_template('index.html', rows=rows)

@app.route('/api')
def api():
    db = get_db()
    cursor = db.execute('SELECT * FROM recipes')
    rows = cursor.fetchall()
    result = [{'id': row[0], 'name': row[1], 'description': row[2] , 'image': row[3]} for row in rows]

    return jsonify(result)

@app.route('/comments')
def comments():
    db = get_db()
    cursor = db.execute('SELECT * FROM comments')
    rows = cursor.fetchall()
    result = [{'comment_id': row[0], 'comment': row[1], 'recipe_id': row[2]} for row in rows]
    return jsonify(result)

@app.route('/add-comment', methods=['POST'])
def add_comment():
    try:
        data = request.get_json()
        comment = data["comment"]
        recipeId = data["id"]

        print(comment)
        print(recipeId)

        conn = get_db()
        cursor = conn.cursor()     
        cursor.execute('''
        INSERT INTO comments (comment, recipe_id) 
        VALUES (?, ?)
        ''', (comment, recipeId))
        
        conn.commit()
        
        return "Comment added successfully"
    except Exception as e:
        return f"error occurred: {e}"
@app.route('/delete-comment', methods=['DELETE'])
def delete_comment():
    try:
        data = request.get_json()
        comment_id = data["id"]
        conn = get_db()
        cursor = conn.cursor()
        
        cursor.execute('''
        DELETE FROM comments 
        WHERE comment_id = ?
        ''', (comment_id,))
        
        conn.commit()
        
        return "Comment deleted successfully"
    except Exception as e:
        return f"error occurred: {e}"
    



if __name__ == '__main__':
    app.run(debug=True)
