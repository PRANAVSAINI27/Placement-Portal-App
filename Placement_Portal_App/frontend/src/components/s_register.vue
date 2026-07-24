<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <img src="@/assets/placement.png" alt="Logo" class="navbar-logo" />
      <h1>Placement Portal Application</h1>
    </div>
    <div class="navbar-links">
      <router-link class="router-link" to="/a_login">Admin</router-link>
      <router-link class="router-link" to="/login">Login</router-link>
      <router-link class="router-link" to="/register">Register</router-link>
    </div>
  </nav>

  <div class="login-form">
        <form action="http://192.168.29.178:5000/s_reg" method="POST">
            <br>
            <h2>Register as Student</h2>
            <br>
            <table>
                <tr>
                    <th style="width: 50%;">Field</th>
                    <th>Update</th>
                </tr>
                <tr>
                    <td>ID</td>
                    <td><input type="number" name="id"></td>
                </tr>
                <tr>
                    <td>Name</td>
                    <td><input type="text" name="name"></td>
                </tr>
                <tr>
                    <td>Branch</td>
                    <td><input type="text" name="branch"></td>
                </tr>
                <tr>
                    <td>Contact</td>
                    <td><input type="text" name="contact"></td>
                </tr>
                <tr>
                    <td>CGPA</td>
                    <td><input type="text" name="cgpa"></td>
                </tr>
                <tr>
                    <td>Year</td>
                    <td><input type="text" name="year"></td>
                </tr>
                <tr>
                    <td>Password</td>
                    <td><input type="password" name="password"></td>
                </tr><br>
                <br><br>
            </table>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>

export default {
  name: 's_signup',
}
</script>

<style>
.navbar {
  display: flex;
  align-items: center;
  margin-top: 0;
  max-width: 100%;
  background: #242424;
  padding: 10px 10px;
  justify-content: space-between;
  color: white;
}

.navbar-brand {
  display: flex;
  align-items: center;
  gap: 10px;
}

.navbar-logo {
  width: 60px;
  margin-right: 10px;
}

.navbar-links {
  display: flex;
  gap: 20px;
  margin-right: 20px;
}

.router-link {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.content {
  padding: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
  text-align: center;
  margin-left: 25%;
}

td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
  flex-direction: row;
  text-align: center;
  margin-left: 25%
}


</style>