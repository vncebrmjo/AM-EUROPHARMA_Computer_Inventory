import pyodbc as odbcconn
from flask import request

connect = odbcconn.connect("Driver={ODBC Driver 13 for SQL Server};"
                        "Server=ICT_LAPTOP02S;"
                        "Database=eDevInventoy;"
                        "Trusted_Connection=yes;")



def main_page_db():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Computers")
    tbl_computers = cursor.fetchall()
    cursor.close()
    return tbl_computers
