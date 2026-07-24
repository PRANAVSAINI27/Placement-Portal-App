<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <img src="@/assets/placement.png" alt="Logo" class="navbar-logo" />
      <h1>Placement Portal Application</h1>
    </div>
    <div class="navbar-links">
      <router-link class="router-link" :to="'/' + id + '/c_dash'">Home</router-link>
      <router-link class="router-link" :to="'/' + id + '/c_appl'">Applications</router-link>
      <router-link class="router-link" style="color: red;" to="/logout">Log Out</router-link>
    </div>
  </nav>

  <body>
    <div class="content">
      <h2>CREATE DRIVE</h2>
        <form :action='"http://192.168.29.178:5000/" + id + "/c_cdrive"' method="POST">
            <br>
            <label>&emsp;&emsp;TITLE : &emsp;&emsp;</label>
            <input type="text" name="TITLE" required>
            <br><br>
            <label>DESCRIPTION: </label>
            <input type="text" name="DESCRIPTION" required>
            <br><br>
            <label>&nbsp;ELIGIBILITY: &emsp;</label>
            <input type="text" name="ELIGIBILITY" placeholder="X.X(CGPA)-20XX(YEAR)" required>
            <br><br>
            <label>&nbsp;&nbsp;DEADLINE: &emsp;&nbsp;</label>
            <input type="text" name="DEADLINE" placeholder="YYYY-MM-DD" pattern="\d{4}-\d{2}-\d{2}" required>
            <br><br>
            <label>VACANCIES: &emsp;</label>
            <input type="number" name="VACANCIES" required><br>
            <br><br>
            <input type="hidden" name="PLACED" value=0>
            <button type="submit">Submit</button>
        </form>
    </div>
  </body>
</template>

<script>
export default {
  name: 'c_dash',
  data() {
    return {
        id: "",
    }
  },
  mounted() {
    this.id = this.$route.params.id
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
}

td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
  flex-direction: row;
}

</style>