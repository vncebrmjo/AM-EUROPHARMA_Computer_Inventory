import pyodbc as odbcconn
from flask import request

connect = odbcconn.connect("Driver={ODBC Driver 13 for SQL Server};"
                        "Server=ICT_LAPTOP02S;"
                        "Database=eDevInventoy;"
                        "Trusted_Connection=yes;")

def main_page_limit():
    Total_Pages = 5
    page = request.args.get('page', 1, type=int)
    page = max(page, 1)
    offset = (page - 1) * Total_Pages
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Computers WHERE ORDER BY Department DESC LIMIT %s, %s",
    (offset, Total_Pages))
    page_limit = cursor.fetchall()
    cursor.close()
    return page_limit


def main_page_db():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Computers")
    tbl_computers = cursor.fetchall()
    cursor.close()
    return tbl_computers
