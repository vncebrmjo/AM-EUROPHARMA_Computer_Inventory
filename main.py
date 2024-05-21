from flask import Flask, render_template, request, url_for, redirect, flash
import pyodbc as odbcconn
from math import ceil

app = Flask(__name__)




cursor = connect.cursor()

@app.route('/', methods=['POST', 'GET'])
def main_page():
    cursor.execute('SELECT * FROM INV_computers')
    get_page = cursor.fetchall()


    return render_template('main_page.html', get_page=get_page)

'''
def get_data(page, per_page, department=None):
    offset = (page - 1) * per_page
    query = "SELECT * FROM Computers ORDER BY ID OFFSET ? ROWS FETCH NEXT ? ROWS ONLY"
    cursor.execute(query, offset, per_page)
    get_page = cursor.fetchall()
    return get_page
'''

@app.route('/test', methods=['POST', 'GET'])
def test():
    cursor.execute('SELECT * FROM INV_computers')
    get_page = cursor.fetchall()
    # cursor.close()
    return render_template('test.html', get_page=get_page)


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
        cursor.execute("SELECT * FROM INV_computers WHERE ID = ?",
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
        ram = request.form.get('ram_1' + ' ' + 'ram_2' + ' ' + 'ram_3')
        storage = request.form.get('storage_1' + ' ' + 'storage_2' + ' ' + 'storage_3')
        os = request.form.get('os_1')
        ms_type = request.form.get('ms_type')
        computer_tag = request.form.get('computer_tag')
        network_tag = request.form.get('network_tag')
        eset = request.form['btn_eset']
        eset = request.form['btn_ups']
        eset = request.form['btn_eset']
        opstat = request.form['btn_opstat']
        cursor = connect.cursor()


    return render_template('Add_Inventory.html')

@app.route('/add_inventory2', methods=['GET', 'POST'])
def add_inventory2():
    msg: ''
    # if request.method == "POST" and 'department' in request.form and 'user' in request.form and 'computer_name' in request.form and 'ip' in request.form and 'processor_1 ' + ' ' + 'processor_2' + ' ' + ' processor_3' in request.form and 'mobo_1' + ' ' + 'mobo_2' in request.form\
    #         and 'ram_1' + ' ' + 'ram_2' + ' ' + 'ram_3' in request.form and 'asset_tag' in request.form and 'serial_number' in request.form and 'storage_1' + ' ' + 'storage_2' + ' ' + 'storage_3' in request.form and 'os_1' in request.form and 'ms_type' in request.form and 'computer_tag' in request.form\
    #         and 'network_tag' in request.form and 'btn_ups' in request.form and 'btn_opstat' in request.form and 'ps_1' + ' ' + 'ps_2' in request.form:
    if request.method == "POST":
        department = request.form.get('department')
        user = request.form['user']
        computer_name = request.form['computer_name']
        ip = request.form['ip']

        processor_1 = request.form.get('processor_1')
        processor_2 = request.form.get('processor_2')
        processor_3 = request.form.get('processor_3')

        processor = processor_1 + ' ' + processor_2 + ' ' + processor_3

        mobo_1 = request.form['mobo_1']
        mobo_2 = request.form['mobo_2']
        mobo = mobo_1 + ' ' +mobo_2




        ps_1 = request.form['ps_1']
        ps_2 = request.form['ps_2']
        ps = ps_1 + ' ' + ps_2



        ram_1 = request.form['ram_1']
        ram_2 = request.form.get('ram_2')
        ram_3 = request.form.get('ram_3')
        ram = ram_1 + ' ' + ram_2 + ' ' + ram_3

        asset_tag = request.form['asset_tag']
        serial_number = request.form['serial_number']


        storage_1 = request.form['storage_1']
        storage_2 = request.form.get('storage_2')
        storage_3 = request.form['storage_3']
        storage = storage_1 + ' ' + storage_2 + ' ' + storage_3


        os = request.form.get('os_1')
        ms_type = request.form.get('ms_type')
        computer_tag = request.form.get('computer_tag')
        network_tag = request.form.get('network_tag')
        eset = request.form['btn_eset']
        ups = request.form['btn_ups']
        opstat = request.form['btn_opstat']

        # cursor.execute("SELECT COUNT(*) FROM Computers WHERE USER = ?  ", (user ))
        # count = cursor.fetchone()[0]
        # if count > 0:
        #     msg = 'The user already exists'
        # else:
        # cursor.execute("INSERT INTO Computers WHERE DEPARTMENT = ?  USER = ? COMPUTER_NAME = ? IP = ? PROCESSOR = ? MOTHERBOARD = ? POWER_SUPPLY = ?"
        #                "RAM = ? STORAGE = ? OS = ? MS_OFFICE = ? ASSET_TAG = ? COMPUTER_TAG = ? NETWORK_TAG = ? UPS = ? SERIAL_NUMBER = ? OPERATIONAL_STATUS = ? ", (department, user, computer_name, ip, processor, mobo, ps,  ram, storage, os, ms_type,
        #                 asset_tag, computer_tag, network_tag,  ups, serial_number, opstat))
        cursor.execute(
            "INSERT INTO INV_computers (DEPARTMENT, USERNAME, COMPUTER_NAME, IP, PROCESSOR, MOTHERBOARD, POWER_SUPPLY, RAM, STORAGE, OS, MS_OFFICE, ASSET_TAG, COMPUTER_TAG, NETWORK_TAG, UPS, SERIAL_NUMBER, OPERATIONAL_STATUS, ESET) "
            "VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (department, user, computer_name, ip, processor, mobo, ps, ram, storage, os, ms_type, asset_tag,
             computer_tag, network_tag, ups, serial_number, opstat, eset))

        connect.commit()
        # flash("Data Saved Successfully")

    return render_template('add_inventory2.html')

@app.route('/Modified_Details', methods=['POST', 'GET'])
def Modified_Details():

    return render_template('Modified_Details.html')


@app.route('/Report_Logs', methods=['POST', 'GET'])
def Report_Logs():

    cursor.execute('SELECT * FROM INV_logs')
    get_page = cursor.fetchall()

    return render_template('Report_Logs.html', get_page=get_page)


'''
@app.route('/save_data', methods=['POST', 'GET'])
def save_data():
    if request.method == "POST":
        user = request.form['user']
        department = request.form.get('department')
        computer_name = request.form['computer_name']
        ip = request.form['ip']
        asset_tag = request.form['asset_tag']
        serial_number = request.form['serial_number']
    return redirect(url_for('Add_Inventory'))
'''

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