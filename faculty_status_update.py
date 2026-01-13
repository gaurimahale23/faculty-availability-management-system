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

print(f"""
<html>
<head>
    <meta http-equiv="refresh" content="0;url=/cgi-bin/faculty_dashboard.py?id={faculty_id}&msg=updated">
</head>
<body></body>
</html>
""")

