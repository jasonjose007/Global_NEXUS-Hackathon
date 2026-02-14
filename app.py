from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# ====================== DATABASE ======================
def init_db():
    conn = sqlite3.connect('medical.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            weight REAL,
            height REAL,
            conditions TEXT,
            allergies TEXT,
            medications TEXT,
            entry_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()   # create table on first run

# ====================== ROUTES ======================

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            conn = sqlite3.connect('medical.db')
            c = conn.cursor()
            
            c.execute('''
                INSERT INTO patients 
                (name, age, gender, weight, height, conditions, allergies, medications, entry_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                request.form['name'],
                request.form.get('age'),
                request.form.get('gender'),
                request.form.get('weight'),
                request.form.get('height'),
                request.form.get('conditions', ''),
                request.form.get('allergies', ''),
                request.form.get('medications', ''),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ))
            conn.commit()
            conn.close()
            return redirect(url_for('success'))
        except Exception as e:
            return f"Error: {str(e)}"
    
    return render_template('index.html')


@app.route('/success')
def success():
    return '''
    <h2 style="color:green; text-align:center; margin-top:50px;">
        Thank you! Your data has been saved successfully.
    </h2>
    <p style="text-align:center;">
        <a href="/">← Submit another entry</a>
    </p>
    '''


@app.route('/view', methods=['GET', 'POST'])
def view_records():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'admin2026':          # ← CHANGE THIS PASSWORD!
            conn = sqlite3.connect('medical.db')
            c = conn.cursor()
            c.execute("SELECT * FROM patients ORDER BY entry_date DESC")
            data = c.fetchall()
            conn.close()
            return render_template('view.html', data=data)
        else:
            return "Wrong password!", 401
    
    return render_template('login.html')


@app.route('/edit/<int:patient_id>', methods=['GET', 'POST'])
def edit_record(patient_id):
    if request.method == 'POST':
        try:
            conn = sqlite3.connect('medical.db')
            c = conn.cursor()
            
            c.execute('''
                UPDATE patients 
                SET name=?, age=?, gender=?, weight=?, height=?, conditions=?, allergies=?, medications=?
                WHERE id=?
            ''', (
                request.form['name'],
                request.form.get('age'),
                request.form.get('gender'),
                request.form.get('weight'),
                request.form.get('height'),
                request.form.get('conditions', ''),
                request.form.get('allergies', ''),
                request.form.get('medications', ''),
                patient_id
            ))
            conn.commit()
            conn.close()
            return redirect(url_for('view_records'))
        except Exception as e:
            return f"Error: {str(e)}"
    
    # GET request - fetch the record
    conn = sqlite3.connect('medical.db')
    c = conn.cursor()
    c.execute("SELECT * FROM patients WHERE id=?", (patient_id,))
    record = c.fetchone()
    conn.close()
    
    if record is None:
        return "Record not found!", 404
    
    return render_template('edit.html', record=record)


if __name__ == '__main__':
    print("Medical Data Portal running at http://127.0.0.1:5000")
    app.run(debug=False)