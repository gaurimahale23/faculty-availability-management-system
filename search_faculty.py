#!C:/Program Files/Python311/python.exe

import sys
sys.path.append(r"C:/Users/admin/AppData/Roaming/Python/Python311/site-packages")

import cgi
import mysql.connector

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
query = form.getvalue("q")

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="faculty_availability_db"
)

cur = con.cursor()
cur.execute(
    """
    SELECT name, department, designation, status
    FROM faculty
    WHERE name LIKE %s OR department LIKE %s
    """,
    (f"%{query}%", f"%{query}%")
)

results = cur.fetchall()
con.close()

print("""
<!DOCTYPE html>
<html>
<head>
<title>Search Results</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-5">

<h3 class="mb-4">Search Results</h3>
""")

if results:
    print("""
    <table class="table table-bordered table-striped">
        <thead class="table-dark">
            <tr>
                <th>Name</th>
                <th>Department</th>
                <th>Designation</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
    """)

    for r in results:
        badge = (
            '<span class="badge bg-success">Available</span>'
            if r[3] == 'Available'
            else '<span class="badge bg-danger">On Leave</span>'
        )

        print(f"""
        <tr>
            <td>{r[0]}</td>
            <td>{r[1]}</td>
            <td>{r[2]}</td>
            <td>{badge}</td>
        </tr>
        """)

    print("</tbody></table>")
else:
    print("<p>No faculty found.</p>")

print("""
<a href="http://localhost/faculty_management_system/faculty_search.html" class="btn btn-secondary">Back</a>
</div>
</body>
</html>
""")
