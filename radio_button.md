<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Radio Button Form</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h2>Select your option:</h2>
        <form action="/submit" method="post">
            <div class="btn-group btn-group-toggle" data-toggle="buttons">
                <label class="btn btn-primary">
                    <input type="radio" name="option" id="option1" autocomplete="off" value="Option 1"> Option 1
                </label>
                <label class="btn btn-primary">
                    <input type="radio" name="option" id="option2" autocomplete="off" value="Option 2"> Option 2
                </label>
            </div>
            <button type="submit" class="btn btn-primary mt-3">Submit</button>
        </form>
    </div>
</body>
</html>


from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Database configuration
server = 'your_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        option = request.form['option']
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Options (option_value) VALUES (?)", option)
        cnxn.commit()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

