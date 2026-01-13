#!C:/Program Files/Python311/python.exe

import sys
import os
sys.path.append(r"C:/Users/admin/AppData/Roaming/Python/Python311/site-packages")

import cgi
import mysql.connector

# ---------------- HTTP HEADER ----------------
print("Content-Type: text/html")
print()

# ---------------- READ QUERY ----------------
form = cgi.FieldStorage()
faculty_id = form.getvalue("id")

query = os.environ.get("QUERY_STRING", "")
show_msg = "msg=updated" in query

# ---------------- DB CONNECTION ----------------
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="faculty_availability_db"
)

cur = con.cursor()
cur.execute(
    "SELECT name, department, designation, status FROM faculty WHERE faculty_id=%s",
    (faculty_id,)
)
faculty = cur.fetchone()
con.close()

# ---------------- INVALID ACCESS ----------------
if not faculty:
    print("<h3>Invalid Access</h3>")
    sys.exit()

# ---------------- UI ----------------
print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Faculty Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="bg-light">

<div class="container mt-5">
    <div class="card shadow p-4 text-center">

        <h3>Welcome, {faculty[0]}</h3>
        <p class="text-muted">
            {faculty[1]} | {faculty[2]}
        </p>
""")

# -------- SUCCESS MESSAGE --------
if show_msg:
    print("""
        <div class="alert alert-success mt-3">
            Status updated successfully
        </div>
    """)

# -------- STATUS + ACTIONS --------
print(f"""
        <h5 class="mt-3">
            Current Status:
            <span class="badge {'bg-success' if faculty[3]=='Available' else 'bg-danger'}">
                {faculty[3]}
            </span>
        </h5>

        <div class="mt-4">
            <a href="/cgi-bin/faculty_status_update.py?id={faculty_id}&status=Available"
               class="btn btn-success m-2">
               Mark Available
            </a>

            <a href="/cgi-bin/faculty_status_update.py?id={faculty_id}&status=On Leave"
               class="btn btn-danger m-2">
               Mark On Leave
            </a>
        </div>

        <div class="mt-4">
            <a href="/faculty_management_system/index.html"
               class="btn btn-secondary">
               Logout
            </a>
        </div>

    </div>
</div>

</body>
</html>
""")

