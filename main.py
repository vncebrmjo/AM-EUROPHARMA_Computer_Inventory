from flask import Flask, render_template, request, url_for
import pyodbc as odbcconn

app = Flask(__name__)

Total_Pages = 5

connect = odbcconn.connect("Driver={ODBC Driver 13 for SQL Server};"
                        "Server=ICT_LAPTOP02S;"
                        "Database=eDevInventoy;"
                        "Trusted_Connection=yes;")

@app.route('/', methods=['POST', 'GET'])
def main_page():
    cursor = connect.cursor()
    department = request.form.get('department')

    if request.method == 'POST':
        cursor.execute("SELECT * FROM Computers WHERE Department = ?",
                       (department,))

    else:
        cursor.execute("SELECT * FROM Computers")

    data = cursor.fetchall()
    cursor.close()

    return render_template('main_page.html', department=department, data=data)

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

    return render_template('Add_Inventory.html')

if __name__ == "__main__":
    app.run(debug=True)