#!C:/Program Files/Python311/python.exe

import sys
sys.path.append(r"C:/Users/admin/AppData/Roaming/Python/Python311/site-packages")

import cgi
import mysql.connector
from datetime import date

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
faculty_id = form.getvalue("id")
status = form.getvalue("status")

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="faculty_availability_db"
)

cur = con.cursor()
cur.execute(
    "UPDATE faculty SET status=%s, updated_on=%s WHERE faculty_id=%s",
    (status, date.today(), faculty_id)
)

con.commit()
con.close()

print("""
<h3>Status Updated Successfully</h3>
<a href="/cgi-bin/admin_dashboard.py">Back to Dashboard</a>
""")
