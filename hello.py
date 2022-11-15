from flask import Flask
import json
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

def get_record(p_id):
    conn = get_db_connection()
    print(p_id)
    record = conn.execute('SELECT * FROM person WHERE p_id = ?',(p_id,)).fetchone()
    print("rec: ",record)
    conn.close()
    if record is None:
        abort(404)
    return record
@app.route('/', methods=('GET', 'POST'))
def home():
    error = ""
    conn = get_db_connection()
    if request.method == 'POST':
        auth =""
        username = request.form['username']
        passw = request.form['password']
        authdeets = conn.execute('SELECT * FROM auth where username = ? and passw = ?',(username,passw)).fetchone()
        if authdeets:
            for auth in authdeets:
                print(auth)
        if auth != "":
            print("here")
            return redirect(url_for('index'))
        else:
            error = "INVALID DETAILS"
        conn.commit()
        conn.close()
        

    return render_template('home_auth.html',error = error)


@app.route('/person')
def index():
    conn = get_db_connection()
    orderdeets = conn.execute('SELECT * FROM person').fetchall()
    conn.close()
   
    return render_template('index2.html', orderdeets= orderdeets)


@app.route('/stock')
def stock():
    conn = get_db_connection()
    stockdeets = conn.execute('SELECT * FROM stock').fetchall()
    conn.close()
    return render_template('stock.html', stockdeets= stockdeets)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        p_id = request.form['p_id']
        p_name = request.form['p_name']
        p_address = request.form['p_address']
        p_blood_grp = request.form['p_blood_grp']
        p_gender = request.form['p_gender']
        p_dob = request.form['p_dob']

        if not p_id:
            flash('name is required!')

        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO person (p_id, p_name,p_address,p_blood_grp,p_gender,p_dob) VALUES (?, ?,?,?,?,?)',
                         (p_id,p_name, p_address,p_blood_grp,p_gender,p_dob))
            
            
            
            
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/donationloc', methods=('GET', 'POST'))
def edit_order():
    
    
    if request.method == 'POST':
        conn = get_db_connection()
        p_id = request.form['p_id']
        print(p_id) 
        quantity = request.form['quantity']
        date_of_don = request.form['p_dob']
        print(date_of_don) 
        p = conn.execute(('SELECT p_blood_grp FROM person where p_id = ?'),(p_id)).fetchone()
        print("p",p)
        qty = (conn.execute('SELECT quantity from stock where s_blood_grp = ?',(p)).fetchone())

        print(qty)
        conn.execute('INSERT INTO donation_loc (p_id,quantity,date_of_don) values(?,?,?)',(p_id,quantity,date_of_don))
        conn.execute("UPDATE stock SET quantity = ? WHERE  s_blood_grp = ?",(int(quantity)+(qty[0]),p[0]))
        print("here2") 
        conn.commit()
        conn.close()
        print("here3")
        return redirect(url_for('index'))

    return render_template('edit_order.html',message = "",title = "Donation Location")
@app.route('/recieve', methods=('GET', 'POST'))
def recieve():
    
    
    if request.method == 'POST':
        conn = get_db_connection()
        p_id = request.form['p_id']
        print(p_id) 
        quantity = request.form['quantity']
        date_of_don = request.form['p_dob']
        print(date_of_don) 
        p = conn.execute(('SELECT p_blood_grp FROM person where p_id = ?'),(p_id)).fetchone()
        if(not p):
            return render_template('edit_order.html',message="Invalid PID",title="Recieve Location")

        qty = (conn.execute('SELECT quantity from stock where s_blood_grp = ?',(p)).fetchone())

        print(qty)
        conn.execute('INSERT INTO recieve_loc (p_id,quantity,r_date) values(?,?,?)',(p_id,quantity,date_of_don))
        if(int(quantity)-qty[0]>0):
            message = "Invalid qty"
            return render_template('edit_order.html',message=message,title="Recieve Location")
        
        conn.execute("UPDATE stock SET quantity = ? WHERE  s_blood_grp = ?",(int(quantity)-(qty[0]),p[0]))
        print("here2") 
        conn.commit()
        conn.close()
        print("here3")
        return redirect(url_for('index'))

    return render_template('edit_order.html',message = "",title="Recieve Location")


if __name__ == "__main__":

    app.run()
