
from flask import Flask, render_template, request, url_for, redirect, flash, jsonify, g, session
import os
import pyodbc as odbcconn
from math import ceil

app = Flask(__name__)

app.secret_key = os.urandom(24)

connect = odbcconn.connect("Driver={ODBC Driver 13 for SQL Server};"
                           "Server= 192.168.1.11;"
                           "Database=vmdevapps;"
                           "uid=local1;"
                           "pwd=$3rver012345")

cursor = connect.cursor()


@app.before_request
def before_request():
    g.user = None
    if 'Username' in session:
        g.user = session['Username']

@app.route('/main_page', methods=['GET'])
def main_page():
    if g.user:
        cursor.execute('SELECT * FROM INV_computers')
        get_page = cursor.fetchall()
        return render_template('main_page.html', get_page=get_page, user=session['Username'])
    return redirect(url_for('login'))


@app.route('/update_inventory', methods=['GET', 'POST'])
def update_inventory():
    if g.user:
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
                               network_tag=network_tag, ups=ups, serial_number=serial_number, details=details, user=user, computer_name=computer_name, session=session['Username'])
    return redirect(url_for('login'))



@app.route('/update_department', methods=['GET', 'POST'])
def update_department():
    if request.method == 'POST':
        id = request.form['id']
        dept_date = request.form['dept_date']
        old_department = request.form['old_department']
        new_department = request.form['new_department']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id,  date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, dept_date, field, old_department, new_department))

        cursor.execute("UPDATE INV_computers SET department = ? WHERE ID = ?",
                       (new_department, id))

        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_department=new_department,
                               old_department=old_department, field=field, id=id, msg=msg, dept_date=dept_date )



@app.route('/update_username', methods=['GET', 'POST'])
def update_username():
    if request.method == 'POST':
        id = request.form['id']
        user_date = request.form['user_date']
        old_username = request.form['old_username']
        new_username = request.form['new_username']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id,date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, user_date, field, old_username, new_username))

        cursor.execute("UPDATE INV_computers SET Username = ? WHERE ID = ?",
                       (new_username, id))
        msg = "The data has been updated successfully"

        connect.commit()

        return render_template('update_inventory.html', new_username=new_username,
                               old_username=old_username, field=field, id=id, msg=msg, user_date=user_date)

@app.route('/update_computername', methods=['GET', 'POST'])
def update_computername():
    if request.method == 'POST':
        id = request.form['id']
        com_date = request.form['com_date']
        old_computername = request.form['old_computername']
        new_computername = request.form['new_computername']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id,date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id,com_date, field, old_computername, new_computername))

        cursor.execute("UPDATE INV_computers SET Computer_Name = ? WHERE ID = ?",
                       (new_computername, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_computername=new_computername,
                               old_computername=old_computername, field=field, id=id, msg=msg, com_date=com_date)

@app.route('/update_ip', methods=['GET', 'POST'])
def update_ip():
    if request.method == 'POST':
        id = request.form['id']
        ip_date = request.form['ip_date']
        old_ip = request.form['old_ip']
        new_ip = request.form['new_ip']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, ip_date, field, old_ip, new_ip))

        cursor.execute("UPDATE INV_computers SET IP = ? WHERE ID = ?",
                       (new_ip, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_ip=new_ip,
                               old_ip=old_ip, field=field, id=id, msg=msg, ip_date=ip_date)


@app.route('/update_asset_tag', methods=['GET', 'POST'])
def update_asset_tag():
    if request.method == 'POST':
        id = request.form['id']
        asset_date = request.form['asset_date']
        old_asset_tag = request.form['old_asset_tag']
        new_asset_tag = request.form['new_asset_tag']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, asset_date, field, old_asset_tag, new_asset_tag))

        cursor.execute("UPDATE INV_computers SET Asset_Tag = ? WHERE ID = ?",
                       (new_asset_tag, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_asset_tag=new_asset_tag,
                               old_asset_tag=old_asset_tag, field=field, id=id, msg=msg, asset_date=asset_date)

@app.route('/update_serial_number', methods=['GET', 'POST'])
def update_serial_number():
    if request.method == 'POST':
        id = request.form['id']
        serial_date = request.form['serial_date']
        old_serial_number = request.form['old_serial_number']
        new_serial_number = request.form['new_serial_number']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, serial_date, field, old_serial_number, new_serial_number))

        cursor.execute("UPDATE INV_computers SET Serial_Number = ? WHERE ID = ?",
                       (new_serial_number, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_serial_number=new_serial_number,
                               old_serial_number=old_serial_number, field=field, id=id, msg=msg, serial_date=serial_date)

@app.route('/update_processor', methods=['GET', 'POST'])
def update_processor():
    if request.method == 'POST':
        id = request.form['id']
        processor_date = request.form['processor_date']
        old_processor = request.form['old_processor']
        new_processor = request.form['new_processor']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id,date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, processor_date, field, old_processor, new_processor))

        cursor.execute("UPDATE INV_computers SET Processor = ? WHERE ID = ?",
                       (new_processor, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_processor=new_processor,
                               old_processor=old_processor, field=field, id=id, msg=msg, processor_date=processor_date)

@app.route('/update_os', methods=['GET', 'POST'])
def update_os():
    if request.method == 'POST':
        id = request.form['id']
        os_date = request.form['os_date']
        old_os = request.form['old_os']
        new_os = request.form['new_os']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, os_date, field, old_os, new_os))

        cursor.execute("UPDATE INV_computers SET OS = ? WHERE ID = ?",
                       (new_os, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_os=new_os,
                               old_os=old_os, field=field, id=id, msg=msg, os_date=os_date)

@app.route('/update_mobo', methods=['GET', 'POST'])
def update_mobo():
    if request.method == 'POST':
        id = request.form['id']
        mobo_date = request.form['mobo_date']
        old_mobo = request.form['old_mobo']
        new_mobo = request.form['new_mobo']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, mobo_date, field, old_mobo, new_mobo))

        cursor.execute("UPDATE INV_computers SET MotherBoard = ? WHERE ID = ?",
                       (new_mobo, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_mobo=new_mobo,
                               old_mobo=old_mobo, field=field, id=id, msg=msg, mobo_date=mobo_date)

@app.route('/update_ram', methods=['GET', 'POST'])
def update_ram():
    if request.method == 'POST':
        id = request.form['id']
        ram_date = request.form['ram_date']
        old_ram= request.form['old_ram']
        new_ram = request.form['new_ram']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, ram_date, field, old_ram, new_ram))

        cursor.execute("UPDATE INV_computers SET RAM = ? WHERE ID = ?",
                       (new_ram, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_ram=new_ram,
                               old_ram=old_ram, field=field, id=id, msg=msg, ram_date=ram_date)

@app.route('/update_storage', methods=['GET', 'POST'])
def update_storage():
    if request.method == 'POST':
        id = request.form['id']
        storage_date = request.form['storage_date']
        old_storage = request.form['old_storage']
        new_storage = request.form['new_storage']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, storage_date, field, old_storage, new_storage))

        cursor.execute("UPDATE INV_computers SET Storage = ? WHERE ID = ?",
                       (new_storage, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_storage=new_storage,
                               old_storage=old_storage, field=field, id=id, msg=msg, storage_date=storage_date)

@app.route('/update_ps', methods=['GET', 'POST'])
def update_ps():
    if request.method == 'POST':
        id = request.form['id']
        ps_date = request.form['ps_date']
        old_ps = request.form['old_ps']
        new_ps = request.form['new_ps']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, ps_date, field, old_ps, new_ps))

        cursor.execute("UPDATE INV_computers SET Power_Supply = ? WHERE ID = ?",
                       (new_ps, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_ps=new_ps,
                               old_ps=old_ps, field=field, id=id, msg=msg, ps_date=ps_date)

@app.route('/update_msoffice', methods=['GET', 'POST'])
def update_msoffice():
    if request.method == 'POST':
        id = request.form['id']
        ms_date = request.form['ms_date']
        old_msoffice = request.form['old_msoffice']
        new_msoffice = request.form['new_msoffice']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, ms_date, field, old_msoffice, new_msoffice))

        cursor.execute("UPDATE INV_computers SET MS_Office = ? WHERE ID = ?",
                       (new_msoffice, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_msoffice=new_msoffice,
                               old_msoffice=old_msoffice, field=field, id=id, msg=msg, ms_date=ms_date)

@app.route('/update_comtag', methods=['GET', 'POST'])
def update_comtag():
    if request.method == 'POST':
        id = request.form['id']
        comtag_date = request.form['comtag_date']
        old_comtag = request.form['old_comtag']
        new_comtag = request.form['new_comtag']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, comtag_date, field, old_comtag, new_comtag))

        cursor.execute("UPDATE INV_computers SET Computer_Tag = ? WHERE ID = ?",
                       (new_comtag, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_comtag=new_comtag,
                               old_comtag=old_comtag, field=field, id=id, msg=msg, comtag_date=comtag_date)

@app.route('/update_nettag', methods=['GET', 'POST'])
def update_nettag():
    if request.method == 'POST':
        id = request.form['id']
        nettag_date = request.form['nettag_date']
        old_nettag = request.form['old_nettag']
        new_nettag = request.form['new_nettag']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, nettag_date, field, old_nettag, new_nettag))

        cursor.execute("UPDATE INV_computers SET Network_Tag = ? WHERE ID = ?",
                       (new_nettag, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_nettag=new_nettag,
                               old_nettag=old_nettag, field=field, id=id, msg=msg, nettag_date=nettag_date)


@app.route('/update_eset', methods=['GET', 'POST'])
def update_eset():
    if request.method == 'POST':
        id = request.form['id']
        eset_date = request.form['eset_date']
        old_eset = request.form['old_eset']
        new_eset = request.form['new_eset']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, eset_date, field, old_eset, new_eset))

        cursor.execute("UPDATE INV_computers SET ESET = ? WHERE ID = ?",
                       (new_eset, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_eset=new_eset,
                               old_eset=old_eset, field=field, id=id, msg=msg, eset_date=eset_date)

@app.route('/update_ups', methods=['GET', 'POST'])
def update_ups():
    if request.method == 'POST':
        id = request.form['id']
        ups_date = request.form['ups_date']
        old_ups = request.form['old_ups']
        new_ups = request.form['new_ups']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, ups_date, field, old_ups, new_ups))

        cursor.execute("UPDATE INV_computers SET UPS = ? WHERE ID = ?",
                       (new_ups, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_ups=new_ups,
                               old_ups=old_ups, field=field, id=id, msg=msg, ups_date=ups_date)



@app.route('/opstat', methods=['GET', 'POST'])
def update_opstat():
    if request.method == 'POST':
        id = request.form['id']
        status_date = request.form['status_date']
        old_opstat = request.form['old_opstat']
        new_opstat = request.form['new_opstat']
        field = request.form['field']

        cursor = connect.cursor()

        cursor.execute(
            "INSERT INTO INV_logs (id, date_modified, field_modified, old_data, new_data) "
            "VALUES ( ?, ?, ?, ?, ?)",
            (id, status_date, field, old_opstat, new_opstat))

        cursor.execute("UPDATE INV_computers SET Operational_Status = ? WHERE ID = ?",
                       (new_opstat, id))
        msg = "The data has been updated successfully"

        connect.commit()


        return render_template('update_inventory.html', new_opstat=new_opstat,
                               old_opstat=old_opstat, field=field, id=id, msg=msg, status_date=status_date)


@app.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if g.user:
        cursor.execute('SELECT * FROM INV_computers')
        get_page = cursor.fetchall()
        return render_template('update_user.html',get_page=get_page, user=session['Username'])
    return redirect(url_for('login'))


@app.route('/add_inventory2', methods=['GET', 'POST'])
def add_inventory2():
    if g.user:
        if request.method == "POST":
            user = request.form['user']
            session['user'] = user

            cursor.execute("SELECT * FROM INV_computers WHERE Username = ?", user)
            row = cursor.fetchone()
            if row:
                error = "The Username already exists"

                return render_template('add_inventory2.html', error=error)

        if request.method == "POST":
            computer_name = request.form['computer_name']
            session['computer_name'] = computer_name

            cursor.execute("SELECT * FROM INV_computers WHERE COMPUTER_NAME = ?", computer_name)
            row = cursor.fetchone()
            if row:
                error2 = "The Computer name already exists"

                return render_template('add_inventory2.html', error2=error2)

        if request.method == "POST":
            ip = request.form['ip']
            session['ip'] = ip

            cursor.execute("SELECT * FROM INV_computers WHERE IP = ?", ip)
            row = cursor.fetchone()
            if row:
                error3 = "The IP Already Exists"

                return render_template('add_inventory2.html', error3=error3)

        if request.method == "POST":
            asset_tag = request.form['asset_tag']
            session['asset_tag'] = asset_tag

            cursor.execute("SELECT * FROM INV_computers WHERE Asset_Tag = ?", asset_tag)
            row = cursor.fetchone()
            if row:
                error4 = "The Asset Tag Already Exists"

                return render_template('add_inventory2.html', error4=error4)

        if request.method == "POST":
            serial_number = request.form['serial_number']
            session['serial_number'] = serial_number

            cursor.execute("SELECT * FROM INV_computers WHERE Serial_Number = ?", serial_number)
            row = cursor.fetchone()
            if row:
                error5 = "The Serial Number Already Exists"

                return render_template('add_inventory2.html', error5=error5)

        if request.method == "POST":
            processor_3 = request.form['processor_3']
            session['processor_3'] = processor_3

        if request.method == "POST":
            ram_1 = request.form['ram_1']
            session['ram_1'] = ram_1
            ram_2 = request.form['ram_2']
            session['ram_2'] = ram_2
            ram_3 = request.form['ram_3']
            session['ram_3'] = ram_3
            ram = ram_1 + ' ' + ram_2 + ' ' + ram_3

        if request.method == "POST":
            storage_1 = request.form['storage_1']
            session['storage_1'] = storage_1

        if request.method == "POST":
            mobo_2 = request.form['mobo_2']
            session['mobo_2'] = mobo_2
            mobo_1 = request.form['mobo_1']
            session['mobo_1'] = mobo_1
            mobo = mobo_1 + ' ' + mobo_2

        if request.method == "POST":
            ps_1 = request.form['ps_1']
            session['ps_1'] = ps_1
            ps_2 = request.form['ps_2']
            session['ps_2'] = ps_2
            ps = ps_1 + ' ' + ps_2

        if request.method == "POST":
            storage_1 = request.form['storage_1']
            session['storage_1'] = storage_1
            storage_2 = request.form['storage_2']
            session['storage_2'] = storage_2
            storage_3 = request.form['storage_3']
            session['storage_3'] = storage_3
            storage = storage_1 + ' ' + storage_2 + ' ' + storage_3


        if request.method == "POST":
            computer_tag = request.form['computer_tag']
            session['computer_tag'] = computer_tag

        if request.method == "POST":
            network_tag = request.form['network_tag']
            session['network_tag'] = network_tag








        if request.method == "POST":
            department = request.form.get('department')


            processor_1 = request.form.get('processor_1')
            processor_2 = request.form.get('processor_2')

            processor = processor_1 + ' ' + processor_2 + ' ' + processor_3

            os = request.form.get('os_1')
            ms_type = request.form.get('ms_type')
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

            return render_template('add_inventory2.html', success_message=success_message, user=session['Username'])

        return render_template('add_inventory2.html', user=session['Username'])
    return redirect(url_for('login'))

@app.route('/Modified_Details', methods=['POST', 'GET'])
def Modified_Details():

    return render_template('Modified_Details.html')


@app.route('/Report_Logs', methods=['POST', 'GET'])
def Report_Logs():
    if g.user:
        cursor.execute('SELECT * FROM INV_logs')
        get_page = cursor.fetchall()

        return render_template('Report_Logs.html', get_page=get_page, user=session['Username'])
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['Password']

        cursor.execute("SELECT * FROM INV_login WHERE Username = ? AND Password = ?", (username, password))
        user = cursor.fetchone()

        if user:
            session['Username'] = username
            return redirect(url_for('main_page'))

        error = "Incorrect Username or Password"
        return render_template('login.html', error=error)

    return render_template('login.html', error=None)


@app.route('/logout')
def logout():
    session.pop('Username', None)
    return render_template('login.html')

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
