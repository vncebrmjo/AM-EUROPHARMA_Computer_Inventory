import pyodbc as odbcconn

connect = odbcconn.connect("Driver={ODBC Driver 13 for SQL Server};"
                        "Server=ICT_LAPTOP02S;"
                        "Database=eDevInventoy;"
                        "Trusted_Connection=yes;")

def main_page_db():
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM Computers')
    rows = cursor.fetchall()
    cursor.close()
    return rows
