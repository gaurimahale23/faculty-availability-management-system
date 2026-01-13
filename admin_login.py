#!C:/Program Files/Python311/python.exe

import sys
import os
sys.path.append(r"C:/Users/admin/AppData/Roaming/Python/Python311/site-packages")

import cgi
import mysql.connector

# ---------------- HTTP HEADER ----------------
print("Content-Type: text/html")
print()

# ---------------- READ REQUEST ----------------
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

query = os.environ.get("QUERY_STRING", "")
show_error = "error=1" in query

# ---------------- LOGIN CHECK ----------------
login_success = False

if username and password:
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
    if cur.fetchone():
        login_success = True
    con.close()

    if login_success:
        print("""
        <html>
        <head>
            <meta http-equiv="refresh" content="0;url=/cgi-bin/admin_dashboard.py">
        </head>
        <body></body>
        </html>
        """)
        sys.exit()

    else:
        show_error = True

# ---------------- LOGIN PAGE UI ----------------
print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Admin Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="bg-light">

<div class="container d-flex justify-content-center align-items-center" style="height:100vh;">
    <div class="card shadow p-4" style="width:360px;">
        <h4 class="text-center mb-3">Admin Login</h4>
""")

if show_error:
    print("""
        <div class="alert alert-danger text-center">
            Invalid Username or Password
        </div>
    """)

print("""
        <form method="post" action="/cgi-bin/admin_login.py">
            <div class="mb-3">
                <input type="text" name="username" class="form-control"
                       placeholder="Username" required>
            </div>

            <div class="mb-3">
                <input type="password" name="password" class="form-control"
                       placeholder="Password" required>
            </div>

            <button type="submit" class="btn btn-primary w-100">
                Login
            </button>
        </form>
    </div>
</div>

</body>
</html>
""")

