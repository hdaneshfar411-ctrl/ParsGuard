<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Users - ParsGuard</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<link rel="stylesheet" href="/static/css/style.css">

</head>

<body>

<div class="d-flex">

<div class="sidebar bg-dark text-white p-3">

<h3 class="text-center mb-4">ParsGuard</h3>

<div class="list-group">

<a href="/panel/" class="list-group-item list-group-item-action">
Dashboard
</a>

<a href="/users/" class="list-group-item list-group-item-action active">
Users
</a>

<a href="/servers/" class="list-group-item list-group-item-action">
Servers
</a>

<a href="/settings/" class="list-group-item list-group-item-action">
Settings
</a>

</div>

</div>

<div class="flex-grow-1">

<nav class="navbar navbar-light bg-white shadow-sm px-4">

<h4>Users</h4>

<button class="btn btn-success">
Add User
</button>

</nav>

<div class="container-fluid mt-4">

<div class="card">

<div class="card-header">

All Users

</div>

<div class="card-body">

<table class="table table-hover">

<thead>

<tr>

<th>ID</th>

<th>Username</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody>

<tr>

<td>1</td>

<td>admin</td>

<td>

<span class="badge bg-success">
Active
</span>

</td>

<td>

<button class="btn btn-danger btn-sm">

Delete

</button>

</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

</div>

</div>

</body>
</html>
