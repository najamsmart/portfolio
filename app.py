from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Database initialization
conn = sqlite3.connect('user.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
              (name text, email text, phone text)''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    # Store user details in the database
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    conn.close()

    return 'User details submitted successfully.'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True, port=5555)
