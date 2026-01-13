#!C:/Program Files/Python311/python.exe

import sys
sys.path.append(r"C:/Users/admin/AppData/Roaming/Python/Python311/site-packages")

import mysql.connector

print("Content-Type: text/html")
print()

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="faculty_availability_db"
)

cur = con.cursor()
cur.execute("SELECT * FROM faculty")
faculty_list = cur.fetchall()

# Count summary
cur.execute("SELECT COUNT(*) FROM faculty")
total = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM faculty WHERE status='Available'")
available = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM faculty WHERE status='On Leave'")
on_leave = cur.fetchone()[0]

con.close()

print(f"""
<!DOCTYPE html>
<html>
<head>
<title>Admin Dashboard</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="bg-light">
<div class="container mt-4">

<h2 class="mb-4">Admin Dashboard - Faculty Availability</h2>
<div class="mb-3">
    <a href="/cgi-bin/add_faculty_form.py" class="btn btn-primary">
        ? Add New Faculty
    </a>
</div>


<div class="row mb-4">
  <div class="col-md-4">
    <div class="card text-center shadow">
      <div class="card-body">
        <h5>Total Faculty</h5>
        <h3>{total}</h3>
      </div>
    </div>
  </div>

  <div class="col-md-4">
    <div class="card text-center shadow border-success">
      <div class="card-body text-success">
        <h5>Available</h5>
        <h3>{available}</h3>
      </div>
    </div>
  </div>

  <div class="col-md-4">
    <div class="card text-center shadow border-danger">
      <div class="card-body text-danger">
        <h5>On Leave</h5>
        <h3>{on_leave}</h3>
      </div>
    </div>
  </div>
</div>

<table class="table table-bordered table-striped shadow">
<thead class="table-dark">
<tr>
<th>Name</th>
<th>Department</th>
<th>Designation</th>
<th>Status</th>
<th>Action</th>
</tr>
</thead>
<tbody>
""")

for f in faculty_list:
    status_badge = (
        '<span class="badge bg-success">Available</span>'
        if f[6] == 'Available'
        else '<span class="badge bg-danger">On Leave</span>'
    )

    action_button = (
        f'<a href="/cgi-bin/update_status.py?id={f[0]}&status=On Leave" class="btn btn-sm btn-danger">Mark On Leave</a>'
        if f[6] == 'Available'
        else f'<a href="/cgi-bin/update_status.py?id={f[0]}&status=Available" class="btn btn-sm btn-success">Mark Available</a>'
    )

    print(f"""
    <tr>
      <td>{f[1]}</td>
      <td>{f[2]}</td>
      <td>{f[3]}</td>
      <td>{status_badge}</td>
      <td>{action_button}</td>
    </tr>
    """)

print("""
</tbody>
</table>

<a href="http://localhost/faculty_management_system/admin_login.html" class="btn btn-secondary">Logout</a>

</div>
</body>
</html>
""")
