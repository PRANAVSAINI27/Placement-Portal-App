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
        <h3>Create Account <a href="/s_reg">Student</a> / <a href="/c_reg">Company</a></h3>
        <h3>Have an account? Login as <a href="/s_login">Student</a> / <a href="/c_login">Company</a></h3>
    </div>
</template>

<script>

export default {
  name: '_register',
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

input{
    align-self: flex-start;
    align-self: center;
}
</style>