<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <img src="@/assets/placement.png" alt="Logo" class="navbar-logo" />
      <h1>Placement Portal Application</h1>
    </div>
    <div class="navbar-links">
      <router-link class="router-link" to="/admin/a_companies">Companies</router-link>
      <router-link class="router-link" to="/admin/a_drives">Drives</router-link>
      <router-link class="router-link" to="/admin/a_students">Students</router-link>
      <router-link class="router-link" style="color: red;" to="/logout">Log Out</router-link>
    </div>
  </nav>

  <body>
    <div class="content">
      <h2>Welcome to the Admin Dashboard</h2>
      <h4> Total Companies: {{ companies }}</h4>
      <h4> Total Students: {{ students }}</h4>
      <h4> Total Drives: {{ drives }}</h4>

      <p>Use the navigation bar to manage companies, drives, and students...</p>
    </div>
  </body>
</template>

<script>
export default {
  name: 'a_home',
  data() {
    return {
      companies: [],
      students: [],
      drives: [],
    };
  },

  mounted() {
    fetch('http://192.168.29.178:5000/admin/a_home', {credentials: 'include'})
      .then(response => response.json())
      .then(data => {
        this.companies = data.companies;
        this.students = data.students;
        this.drives = data.drives;
      })
  },
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
</style>