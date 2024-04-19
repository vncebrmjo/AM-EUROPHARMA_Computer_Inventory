import pyodbc as odbccon
from main import render_template
connect = odbccon.connect( "Driver={ODBC Driver 13 for SQL Server};"
                        "Server=ICT_LAPTOP02S;"
                        "Database=eDevInventoy;"
                        "Trusted_Connection=yes;")
'''
cursor = conn.cursor()
cursor.execute('Select * from Computers')
for row in cursor:
    print(row)
'''

def main_page_db():
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM Computers')
    for row in cursor:
        print(row)

