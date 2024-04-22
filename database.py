import pyodbc as odbccon
from main import render_template
conn = odbccon.connect( "Driver={ODBC Driver 13 for SQL Server};"
                        "Server=ICT_LAPTOP02S;"
                        "Database=eDevInventoy;"
                        "Trusted_Connection=yes;")

cursor = conn.cursor()
cursor.execute('Select * from Computers')
for row in cursor:
    print(row)

'''
def main_page_db():

    return render_template('main_page.html')
'''