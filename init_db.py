import sqlite3
connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO person (p_id,p_name,p_gender,p_blood_grp,p_address,p_dob) VALUES (?,?,?,?,?,?)",
            ('001','Mathangi','Female','A+','JUBILEE MANSION, BANGALORE','2002-2-2')
            )
cur.execute("INSERT INTO stock (s_blood_grp,quantity)VALUES (?,?)",("A+",0))
cur.execute("INSERT INTO stock (s_blood_grp,quantity)VALUES (?,?)",("A-",0))
cur.execute("INSERT INTO stock (s_blood_grp,quantity)VALUES (?,?)",("AB+",0))
cur.execute("INSERT INTO stock (s_blood_grp,quantity)VALUES (?,?)",("AB-",0))

cur.execute("INSERT INTO stock (s_blood_grp,quantity)VALUES (?,?)",("B+",0))
cur.execute("INSERT INTO stock (s_blood_grp,quantity)VALUES (?,?)",("B-",0))

cur.execute("INSERT INTO stock (s_blood_grp,quantity)VALUES (?,?)",("O+",0))
cur.execute("INSERT INTO stock (s_blood_grp,quantity)VALUES (?,?)",("O-",0))






cur.execute("INSERT INTO auth(username,passw) VALUES (?,?)",('admin','admin'))

connection.commit()
connection.close()