from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Configuration for MS SQL Server
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Establishing connection to the database
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    # Check if username and password are correct (Example query)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user:
        # If credentials are correct, redirect to a dashboard or home page
        return redirect(url_for('dashboard'))
    else:
        # If credentials are incorrect, return to login page with a message
        return render_template('login.html', message='Invalid username or password.')

@app.route('/dashboard')
def dashboard():
    return "Welcome to the Dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
