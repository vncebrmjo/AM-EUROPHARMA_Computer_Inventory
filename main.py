from flask import Flask, render_template, request, url_for
from db_utils import main_page_db, details_db
import pyodbc as odbcconn

app = Flask(__name__)

Total_Pages = 5

connect = odbcconn.connect("Driver={ODBC Driver 13 for SQL Server};"
                        "Server=ICT_LAPTOP02S;"
                        "Database=eDevInventoy;"
                        "Trusted_Connection=yes;")

@app.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        selected_department = request.form.get('department')
    else:
        selected_department = None

    data = main_page_db(selected_department)

    return render_template('main_page.html', data=data)

@app.route('/details')
def details():
    fetch = details_db()
    return render_template('details.html', fetch=fetch)

@app.route('/Add_Inventory')
def Add_Inventory():

    return render_template('Add_Inventory.html')

if __name__ == "__main__":
    app.run(debug=True)