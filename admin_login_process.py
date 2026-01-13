#!C:/Program Files/Python311/python.exe

import sys
sys.path.append(r"C:/Users/admin/AppData/Roaming/Python/Python311/site-packages")

import cgi
import mysql.connector

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="faculty_availability_db"
)

cur = con.cursor()
cur.execute(
    "SELECT * FROM admin WHERE username=%s AND password=%s",
    (username, password)
)

result = cur.fetchone()
con.close()

if result:
    print("Status: 302 Found")
    print("Location: /cgi-bin/admin_dashboard.py")
    print()
else:
    print("Status: 302 Found")
    print("Location: /cgi-bin/admin_login.py?error=1")
    print()
