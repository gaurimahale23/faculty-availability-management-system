#!C:/Program Files/Python311/python.exe

print("Content-Type: text/html")
print()

print("""
<!DOCTYPE html>
<html>
<head>
<title>Add New Faculty</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="bg-light">
<div class="container mt-5">
<h3 class="mb-4">Add New Faculty</h3>

<form action="/cgi-bin/add_faculty.py" method="post" class="card p-4 shadow">

<div class="mb-3">
<label>Name</label>
<input type="text" name="name" class="form-control" required>
</div>

<div class="mb-3">
<label>Department</label>
<input type="text" name="department" class="form-control" required>
</div>

<div class="mb-3">
<label>Designation</label>
<input type="text" name="designation" class="form-control" required>
</div>

<div class="mb-3">
<label>Username (for faculty login)</label>
<input type="text" name="username" class="form-control" required>
</div>

<div class="mb-3">
<label>Password</label>
<input type="password" name="password" class="form-control" required>
</div>

<button type="submit" class="btn btn-success">Add Faculty</button>
<a href="/cgi-bin/admin_dashboard.py" class="btn btn-secondary">Cancel</a>

</form>
</div>
</body>
</html>
""")
