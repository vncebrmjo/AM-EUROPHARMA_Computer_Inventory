import pyodbc as odbcconn


connect = odbcconn.connect("Driver={ODBC Driver 13 for SQL Server};"
                        "Server=ICT_LAPTOP02S;"
                        "Database=eDevInventoy;"
                        "Trusted_Connection=yes;")

def main_page_db(department):
    cursor = connect.cursor()
    if department:
        cursor.execute("SELECT * FROM Computers WHERE Department = ?",
                       ( department,))
    else:
        cursor.execute("SELECT * FROM Computers")

    department = cursor.fetchall()
    cursor.close()
    return department

def details_db():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Computers")

    details = cursor.fetchall()
    cursor.close()
    return details

