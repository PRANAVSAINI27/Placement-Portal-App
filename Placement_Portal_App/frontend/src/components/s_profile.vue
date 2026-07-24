<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <img src="@/assets/placement.png" alt="Logo" class="navbar-logo" />
      <h1>Placement Portal Application</h1>
    </div>
    <div class="navbar-links">
      <router-link class="router-link" :to= "'/' + id + '/s_dash'">Home</router-link>
      <router-link class="router-link" :to="'/' + id + '/s_appl'">Application Status</router-link>
      <router-link class="router-link" :to="'/' + id + '/s_appr'">Approved</router-link>
      <router-link class="router-link" style="color: red;" to="/logout">Log Out</router-link>
    </div>
  </nav>

  <body>
    <div class="content">
      <h2>PROFILE</h2>
      <p>
        </p>
        <form :action="'http://192.168.29.178:5000/' + id + '/s_uprofile'" method="POST">
        <table>
          <tr>
            <th style="width: 50%;">Field</th>
            <th>Update</th>
          </tr>
          <tr>
            <td>Name</td>
            <td><input type="text" name="name" :value="profile[1]"></td>
          </tr>
          <tr>
            <td>Branch</td>
            <td><input type="text" name="branch" :value="profile[2]"></td>
          </tr>
          <tr>
            <td>Contact</td>
            <td><input type="text" name="contact" :value="profile[3]"></td>
          </tr>
          <tr>
            <td>CGPA</td>
            <td><input type="text" name="cgpa" :value="profile[4]"></td>
          </tr>
          <tr>
            <td>Year</td>
            <td><input type="text" name="year" :value="profile[5]"></td>
          </tr>
          <tr>
            <td>Password</td>
            <td><input type="text" name="password" :value="profile[8]"></td>
          </tr><br>
          <br><br>
        </table>
        <button type="submit">Submit</button>
      </form>
    </div>
  </body>
</template>

<script>
export default {
  name: 's_profile',
  data() {
    return {
        id: "",
        profile: [],
    }
  },
  mounted() {
    this.id = this.$route.params.id

    fetch(`http://192.168.29.178:5000/${ this.id }/s_profile`, {credentials: 'include'})
        .then(response => response.json())
        .then(data => {
            this.profile = data;
        });
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
}

td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
  flex-direction: row;
  text-align: center;
}


</style>