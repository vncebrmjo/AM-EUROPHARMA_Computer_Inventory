from flask import Flask, render_template, request, url_for, redirect
import pyodbc as odbcconn
from math import ceil

app = Flask(__name__)



connect = odbcconn.connect("Driver={ODBC Driver 13 for SQL Server};"
                        "Server=ICT_LAPTOP02S;"
                        "Database=eDevInventoy;"
                        "Trusted_Connection=yes;")
cursor = connect.cursor()

@app.route('/', methods=['POST', 'GET'])
def main_page():
    page = int(request.args.get('page', 1))
    per_page = 10  # Number of rows per page

    department = request.form.get('department')

    get_page = get_data(page, per_page, department)

    cursor.execute("SELECT COUNT(*) FROM Computers")
    total_rows = cursor.fetchone()[0]

    # Calculate total number of pages
    total_pages = ceil(total_rows / per_page)


    return render_template('main_page.html', get_page=get_page, page=page,
                           len=len, per_page=per_page, total_pages=total_pages, department=department )
'''
def get_data(page, per_page, department=None):
    offset = (page - 1) * per_page
    query = "SELECT * FROM Computers ORDER BY ID OFFSET ? ROWS FETCH NEXT ? ROWS ONLY"
    cursor.execute(query, offset, per_page)
    get_page = cursor.fetchall()
    return get_page
'''

def get_data(page, per_page, department=None):
    offset = (page - 1) * per_page
    query = "SELECT * FROM Computers"
    params = []

    if department:
        query += " WHERE department = ?"
        params.append(department)

    query += " ORDER BY id OFFSET ? ROWS FETCH NEXT ? ROWS ONLY"
    params.extend([offset, per_page])

    cursor.execute(query, params)
    get_page = cursor.fetchall()
    return get_page

@app.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'GET':
        id = request.args.get('id')
        user = request.args.get('user')
        computer_name = request.args.get('computer_name')
        processor = request.args.get('processor')
        motherboard = request.args.get('motherboard')
        power_supply = request.args.get('power_supply')
        ram = request.args.get('ram')
        storage = request.args.get('storage')
        os = request.args.get('os')
        eset = request.args.get('eset')
        msoffice = request.args.get('msoffice')
        asset_tag = request.args.get('asset_tag')
        computer_tag = request.args.get('computer_tag')
        network_tag = request.args.get('network_tag')
        ups = request.args.get('ups')
        serial_number = request.args.get('serial_number')

        cursor = connect.cursor()
        cursor.execute("SELECT * FROM Computers WHERE ID = ?",
                       (id,))
        details = cursor.fetchone()

    return render_template('details.html', id=id, processor=processor, motherboard=motherboard, power_supply=power_supply,
                           ram=ram, storage=storage, os=os, eset=eset, msoffice=msoffice, asset_tag=asset_tag, computer_tag=computer_tag,
                           network_tag=network_tag, ups=ups, serial_number=serial_number, details=details, user=user, computer_name=computer_name)

@app.route('/Add_Inventory')
def Add_Inventory():
    if request.method == "POST":
        user = request.form['user']
        department = request.form.get('department')
        computer_name = request.form['computer_name']
        ip = request.form['ip']
        asset_tag = request.form['asset_tag']
        serial_number = request.form['serial_number']

        processor = request.form.get('processor_1 ' + ' ' + 'processor_2' + ' ' + ' processor_3' )
        mobo = request.form.get('mobo_1' + ' ' + 'mobo_2')
        ps = request.form.get('ps_1' + ' ' + 'ps_2')
    return render_template('Add_Inventory.html')

if __name__ == "__main__":
    app.run(debug=True)

    # department = request.form.get('department')
    # mobo = request.form.get('mobo')
    # ram = request.form.get('ram', ' ')

    # if request.method == 'POST':
    #    cursor.execute("SELECT * FROM Computers WHERE Department = ? " ,
    #                   (department))
    # cursor.execute("SELECT * FROM Computers WHERE MotherBoard LIKE  ? ",
    #              ())

    # else:
    #    cursor.execute("SELECT * FROM Computers")

    # data = cursor.fetchall()