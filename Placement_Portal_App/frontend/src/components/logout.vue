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
</template>

<script>

export default {
  name: 'g_home',
  mounted() {
    fetch("http://192.168.29.178:5000/logout",{credentials:"include"})
      .then(()=>{
      this.$router.replace("/")})
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