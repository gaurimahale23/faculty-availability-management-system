#!C:/Program Files/Python311/python.exe

import sys
sys.path.append(r"C:/Users/admin/AppData/Roaming/Python/Python311/site-packages")

import cgi
import mysql.connector
from datetime import date

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()

name = form.getvalue("name")
department = form.getvalue("department")
designation = form.getvalue("designation")
username = form.getvalue("username")
password = form.getvalue("password")

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="faculty_availability_db"
)

cur = con.cursor()

try:
    cur.execute("""
        INSERT INTO faculty
        (name, department, designation, username, password, status, updated_on)
        VALUES (%s, %s, %s, %s, %s, 'Available', %s)
    """, (name, department, designation, username, password, date.today()))

    con.commit()

    print("""
    <h3>Faculty Added Successfully ?</h3>
    <a href="/cgi-bin/admin_dashboard.py">Back to Dashboard</a>
    """)

except mysql.connector.errors.IntegrityError:
    print("""
    <h3 style="color:red;">Username already exists ?</h3>
    <a href="/cgi-bin/add_faculty_form.py">Try Again</a>
    """)

con.close()


