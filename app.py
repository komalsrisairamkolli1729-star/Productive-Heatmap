from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productivity (
            day_id INTEGER PRIMARY KEY,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/log_productivity', methods=['POST'])
def log_productivity():
    data = request.json
    day_id = data.get('day_id')
    status = data.get('status')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO productivity (day_id, status) VALUES (?, ?)', (day_id, status))
    conn.commit()
    conn.close()
    return jsonify({"message": "Saved!"})

@app.route('/get_data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productivity WHERE status="productive"')
    rows = cursor.fetchall()
    conn.close()
    # Convert SQL rows to a simple list of day IDs
    return jsonify([row[0] for row in rows])

if __name__ == '__main__':
    app.run(debug=True)