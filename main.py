from flask import Flask, render_template
import pyodbc as odbccon

app = Flask(__name__)


@app.route('/')
def main_page_form():
#    cursor = conn.cursor()
#    cursor.execute('Select * from Computers')
#    for row in cursor:
#        print(row)
    return render_template('main_page.html')

if __name__ == "__main__":
    app.run(debug=True)