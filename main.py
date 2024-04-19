from flask import Flask, render_template
import pyodbc as odbccon
from database import main_page_db

app = Flask(__name__)

conn = odbccon.connect( "Driver={ODBC Driver 13 for SQL Server};"
                        "Server=ICT_LAPTOP02S;"
                        "Database=eDevInventoy;"
                        "Trusted_Connection=yes;")

@app.route('/')
def main_page():
    main_page = main_page_db
    return render_template('main_page.html', main_page_db =  main_page)



if __name__ == "__main__":
    app.run(debug=True)