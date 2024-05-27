
from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
import pyodbc as odbcconn
from math import ceil

app = Flask(__name__)


cursor = connect.cursor()

# @app.route('/', methods=['POST', 'GET'])
# def login():
#
#
#
#     return render_template('login.html')


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

# @app.route('/validate', methods=['GET', 'POST'])
# def validate():
#     if request.method == "POST":
#         user = request.form['user']
#
#         cursor.execute("SELECT * FROM INV_computers WHERE Username = ?", user)
#         row = cursor.fetchone()
#         if row:
#             error = "The Username Already Exists"
#
#             return render_template('add_inventory2.html', error=error)
#         else:
#             # If username doesn't exist, redirect to add_inventory2
#             return redirect(url_for('add_inventory2'))
#     else:
#         # Handle GET request to /validate if needed
#         pass


@app.route('/update_inventory', methods=['GET', 'POST'])
def update_inventory():
    id = request.args.get('id')
    department = request.args.get('department')
    user = request.args.get('user')

    computer_name = request.args.get('computer_name')

    ip = request.args.get('ip')
    processor = request.args.get('processor')
    motherboard = request.args.get('motherboard')
    power_supply = request.args.get('power_supply')
    ram = request.args.get('ram')
    storage = request.args.get('storage')
    os = request.args.get('os')
    eset = request.args.get('eset')
    ms_office = request.args.get('ms_office')
    asset_tag = request.args.get('asset_tag')
    computer_tag = request.args.get('computer_tag')
    network_tag = request.args.get('network_tag')
    ups = request.args.get('ups')
    serial_number = request.args.get('serial_number')
    op_stat = request.args.get('op_stat')

    cursor = connect.cursor()
    cursor.execute("SELECT * FROM INV_computers WHERE ID = ?",
                   (id,))
    details = cursor.fetchone()

    return render_template('update_inventory.html', op_stat=op_stat, department=department,ip=ip, id=id, processor=processor, motherboard=motherboard, power_supply=power_supply,
                           ram=ram, storage=storage, os=os, eset=eset, ms_office=ms_office, asset_tag=asset_tag, computer_tag=computer_tag,
                           network_tag=network_tag, ups=ups, serial_number=serial_number, details=details, user=user, computer_name=computer_name)




@app.route('/update_department', methods=['GET', 'POST'])
def update_department():
    if request.method == 'POST':
        id = request.form['id']
        old_department = request.form['old_department']
        new_department = request.form['new_department']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_department, new_department))

        cursor.execute("UPDATE INV_computers SET department = ? WHERE ID = ?",
                       (new_department, id))

        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_department=new_department, details=details,
                               old_department=old_department, field=field, id=id, msg=msg )

# @app.route('/update_department', methods=['GET', 'POST'])
# def update_department():
#     id = request.form['id']
#     department = request.args.get('department')
#
#     cursor = connect.cursor()
#     cursor.execute("SELECT * FROM INV_computers WHERE ID = ?", (id,))
#     details = cursor.fetchone()
#
#     if request.method == 'POST':
#         # Handle form submission
#         new_department = request.form['new_department']
#         old_department = request.form['old_department']
#         field = request.form['field']
#
#         new_department2 = cursor.execute("INSERT INTO INV_logs (id, field_modified, old_data, new_data) VALUES (?, ?, ?, ?)",
#                        (id, field, old_department, new_department))
#         cursor.execute("UPDATE INV_computers SET department = ? WHERE ID = ?", (new_department, id))
#
#         connect.commit()
#
#         return render_template('update_inventory.html', department=new_department, id=id, details=details,
#                                msg="The data has been updated successfully")
#
#     # Render the template for GET request
#     return render_template('update_inventory.html', department=department, id=id, details=details)

# @app.route('/update_username', methods=['GET', 'POST'])
# def update_username():
#     id = request.form['id']
#     user = request.args.get('user')
#
#     cursor = connect.cursor()
#     cursor.execute("SELECT * FROM INV_computers WHERE ID = ?", (id,))
#     details = cursor.fetchone()
#
#     if request.method == 'POST':
#         # Handle form submission
#         old_username = request.form['old_username']
#         new_username = request.form['new_username']
#         field = request.form['field']
#
#         cursor.execute("INSERT INTO INV_logs (id, field_modified, old_data, new_data) VALUES (?, ?, ?, ?)",
#                        (id, field, old_username, new_username))
#         cursor.execute("UPDATE INV_computers SET Username = ? WHERE ID = ?", (new_username , id))
#
#         connect.commit()
#
#         return render_template('update_inventory.html', user=new_username , id=id, details=details,
#                                msg="The data has been updated successfully")
#
#     # Render the template for GET request
#     return render_template('update_inventory.html', user=user, id=id, details=details)


@app.route('/update_username', methods=['GET', 'POST'])
def update_username():
    if request.method == 'POST':
        id = request.form['id']
        old_username = request.form['old_username']
        new_username = request.form['new_username']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_username, new_username))

        cursor.execute("UPDATE INV_computers SET Username = ? WHERE ID = ?",
                       (new_username, id))
        msg = "The data has been updated successfully"

        connect.commit()

        return render_template('update_inventory.html', new_username=new_username, details=details,
                               old_username=old_username, field=field, id=id, msg=msg)

@app.route('/update_computername', methods=['GET', 'POST'])
def update_computername():
    if request.method == 'POST':
        id = request.form['id']
        old_computername = request.form['old_computername']
        new_computername = request.form['new_computername']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_computername, new_computername))

        cursor.execute("UPDATE INV_computers SET Computer_Name = ? WHERE ID = ?",
                       (new_computername, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_computername=new_computername, details=details,
                               old_computername=old_computername, field=field, id=id, msg=msg)

@app.route('/update_ip', methods=['GET', 'POST'])
def update_ip():
    if request.method == 'POST':
        id = request.form['id']
        old_ip = request.form['old_ip']
        new_ip = request.form['new_ip']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_ip, new_ip))

        cursor.execute("UPDATE INV_computers SET IP = ? WHERE ID = ?",
                       (new_ip, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_ip=new_ip, details=details,
                               old_ip=old_ip, field=field, id=id, msg=msg)


@app.route('/update_asset_tag', methods=['GET', 'POST'])
def update_asset_tag():
    if request.method == 'POST':
        id = request.form['id']
        old_asset_tag = request.form['old_asset_tag']
        new_asset_tag = request.form['new_asset_tag']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_asset_tag, new_asset_tag))

        cursor.execute("UPDATE INV_computers SET Asset_Tag = ? WHERE ID = ?",
                       (new_asset_tag, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_asset_tag=new_asset_tag, details=details,
                               old_asset_tag=old_asset_tag, field=field, id=id, msg=msg)

@app.route('/update_serial_number', methods=['GET', 'POST'])
def update_serial_number():
    if request.method == 'POST':
        id = request.form['id']
        old_serial_number = request.form['old_serial_number']
        new_serial_number = request.form['new_serial_number']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_serial_number, new_serial_number))

        cursor.execute("UPDATE INV_computers SET Serial_Number = ? WHERE ID = ?",
                       (new_serial_number, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_serial_number=new_serial_number, details=details,
                               old_serial_number=old_serial_number, field=field, id=id, msg=msg)

@app.route('/update_processor', methods=['GET', 'POST'])
def update_processor():
    if request.method == 'POST':
        id = request.form['id']
        old_processor = request.form['old_processor']
        new_processor = request.form['new_processor']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_processor, new_processor))

        cursor.execute("UPDATE INV_computers SET Processor = ? WHERE ID = ?",
                       (new_processor, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_processor=new_processor, details=details,
                               old_processor=old_processor, field=field, id=id, msg=msg)

@app.route('/update_os', methods=['GET', 'POST'])
def update_os():
    if request.method == 'POST':
        id = request.form['id']
        old_os = request.form['old_os']
        new_os = request.form['new_os']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_os, new_os))

        cursor.execute("UPDATE INV_computers SET OS = ? WHERE ID = ?",
                       (new_os, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_os=new_os, details=details,
                               old_os=old_os, field=field, id=id, msg=msg)

@app.route('/update_mobo', methods=['GET', 'POST'])
def update_mobo():
    if request.method == 'POST':
        id = request.form['id']
        old_mobo = request.form['old_mobo']
        new_mobo = request.form['new_mobo']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_mobo, new_mobo))

        cursor.execute("UPDATE INV_computers SET MotherBoard = ? WHERE ID = ?",
                       (new_mobo, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_mobo=new_mobo, details=details,
                               old_mobo=old_mobo, field=field, id=id, msg=msg)

@app.route('/update_ram', methods=['GET', 'POST'])
def update_ram():
    if request.method == 'POST':
        id = request.form['id']
        old_ram= request.form['old_ram']
        new_ram = request.form['new_ram']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_ram, new_ram))

        cursor.execute("UPDATE INV_computers SET RAM = ? WHERE ID = ?",
                       (new_ram, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_ram=new_ram, details=details,
                               old_ram=old_ram, field=field, id=id, msg=msg)

@app.route('/update_storage', methods=['GET', 'POST'])
def update_storage():
    if request.method == 'POST':
        id = request.form['id']
        old_storage = request.form['old_storage']
        new_storage = request.form['new_storage']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_storage, new_storage))

        cursor.execute("UPDATE INV_computers SET Storage = ? WHERE ID = ?",
                       (new_storage, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_storage=new_storage, details=details,
                               old_storage=old_storage, field=field, id=id, msg=msg)

@app.route('/update_ps', methods=['GET', 'POST'])
def update_ps():
    if request.method == 'POST':
        id = request.form['id']
        old_ps = request.form['old_ps']
        new_ps = request.form['new_ps']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_ps, new_ps))

        cursor.execute("UPDATE INV_computers SET Power_Supply = ? WHERE ID = ?",
                       (new_ps, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_ps=new_ps, details=details,
                               old_ps=old_ps, field=field, id=id, msg=msg)

@app.route('/update_msoffice', methods=['GET', 'POST'])
def update_msoffice():
    if request.method == 'POST':
        id = request.form['id']
        old_msoffice = request.form['old_msoffice']
        new_msoffice = request.form['new_msoffice']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_msoffice, new_msoffice))

        cursor.execute("UPDATE INV_computers SET MS_Office = ? WHERE ID = ?",
                       (new_msoffice, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_msoffice=new_msoffice, details=details,
                               old_msoffice=old_msoffice, field=field, id=id, msg=msg)

@app.route('/update_comtag', methods=['GET', 'POST'])
def update_comtag():
    if request.method == 'POST':
        id = request.form['id']
        old_comtag = request.form['old_comtag']
        new_comtag = request.form['new_comtag']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_comtag, new_comtag))

        cursor.execute("UPDATE INV_computers SET Computer_Tag = ? WHERE ID = ?",
                       (new_comtag, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_comtag=new_comtag, details=details,
                               old_comtag=old_comtag, field=field, id=id, msg=msg)

@app.route('/update_nettag', methods=['GET', 'POST'])
def update_nettag():
    if request.method == 'POST':
        id = request.form['id']
        old_nettag = request.form['old_nettag']
        new_nettag = request.form['new_nettag']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_nettag, new_nettag))

        cursor.execute("UPDATE INV_computers SET Network_Tag = ? WHERE ID = ?",
                       (new_nettag, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_nettag=new_nettag, details=details,
                               old_nettag=old_nettag, field=field, id=id, msg=msg)


@app.route('/update_eset', methods=['GET', 'POST'])
def update_eset():
    if request.method == 'POST':
        id = request.form['id']
        old_eset = request.form['old_eset']
        new_eset = request.form['new_eset']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_eset, new_eset))

        cursor.execute("UPDATE INV_computers SET ESET = ? WHERE ID = ?",
                       (new_eset, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_eset=new_eset, details=details,
                               old_eset=old_eset, field=field, id=id, msg=msg)

@app.route('/update_ups', methods=['GET', 'POST'])
def update_ups():
    if request.method == 'POST':
        id = request.form['id']
        old_ups = request.form['old_ups']
        new_ups = request.form['new_ups']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_ups, new_ups))

        cursor.execute("UPDATE INV_computers SET UPS = ? WHERE ID = ?",
                       (new_ups, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_ups=new_ups, details=details,
                               old_ups=old_ups, field=field, id=id, msg=msg)



@app.route('/opstat', methods=['GET', 'POST'])
def update_opstat():
    if request.method == 'POST':
        id = request.form['id']
        old_opstat = request.form['old_opstat']
        new_opstat = request.form['new_opstat']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?)",
            (id, field, old_opstat, new_opstat))

        cursor.execute("UPDATE INV_computers SET Operational_Status = ? WHERE ID = ?",
                       (new_opstat, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_opstat=new_opstat, details=details,
                               old_opstat=old_opstat, field=field, id=id, msg=msg)







@app.route('/update_user', methods=['GET', 'POST'])
def update_user():
    cursor.execute('SELECT * FROM INV_computers')
    get_page = cursor.fetchall()
    return render_template('update_user.html',get_page=get_page)

@app.route('/add_inventory2', methods=['GET', 'POST'])
def add_inventory2():
    if request.method == "POST":
        user = request.form['user']

        cursor.execute("SELECT * FROM INV_computers WHERE Username = ?", user)
        row = cursor.fetchone()
        if row:
            error = "The Username already exists"

            return render_template('add_inventory2.html', error=error)

    if request.method == "POST":
        computer_name = request.form['computer_name']

        cursor.execute("SELECT * FROM INV_computers WHERE COMPUTER_NAME = ?", computer_name)
        row = cursor.fetchone()
        if row:
            error2 = "The Computer name already exists"

            return render_template('add_inventory2.html', error2=error2)

    if request.method == "POST":
        ip = request.form['ip']

        cursor.execute("SELECT * FROM INV_computers WHERE IP = ?", ip)
        row = cursor.fetchone()
        if row:
            error3 = "The IP Already Exists"

            return render_template('add_inventory2.html', error3=error3)


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


        cursor.execute(
            "INSERT INTO INV_computers (DEPARTMENT, USERNAME, COMPUTER_NAME, IP, PROCESSOR, MOTHERBOARD, POWER_SUPPLY, RAM, STORAGE, OS, MS_OFFICE, ASSET_TAG, COMPUTER_TAG, NETWORK_TAG, UPS, SERIAL_NUMBER, OPERATIONAL_STATUS, ESET) "
            "VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (department, user, computer_name, ip, processor, mobo, ps, ram, storage, os, ms_type, asset_tag,
             computer_tag, network_tag, ups, serial_number, opstat, eset))
        success_message = "The information has been added successfully!"
        connect.commit()

        return render_template('add_inventory2.html', success_message=success_message)

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
