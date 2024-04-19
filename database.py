import pyodbc as odbccon
conn = odbccon.connect("DRIVER = {SQL Server Native Client 11.0};"
                       "SERVER = ICT_LAPTOP02S;"
                       "DATABASE = eDevInventoy;"
                       "Trusted_Connection=yes;")
cursor = conn.cursor()
cursor.execute('Select * from Computers')
for row in cursor:
    print('department = %r' %(row,))
