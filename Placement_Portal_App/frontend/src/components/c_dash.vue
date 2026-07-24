<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <img src="@/assets/placement.png" alt="Logo" class="navbar-logo" />
      <h1>Placement Portal Application</h1>
    </div>
    <div class="navbar-links">
      <router-link class="router-link" :to="'/' + id + '/c_cdrive'">Create Drive</router-link>
      <router-link class="router-link" :to="'/' + id + '/c_appl'">Applications</router-link>
      <router-link class="router-link" style="color: red;" to="/logout">Log Out</router-link>
    </div>
  </nav>

  <body>
    <div class="content">
      <h2>INFO</h2>
        <table>
          <tr>
            <th>Company Name</th>
            <th>HR Contact</th>
            <th>Website</th>
          </tr>
          <tr v-for="com in comp" :key="com[0]">
            <td>{{ com[1] }}</td>
            <td>{{ com[2] }}</td>
            <td>{{ com[3] }}</td>
          </tr>
        </table>
      <br><br>
      <h2>DRIVES</h2>
        <table>
          <tr>
            <th>Title</th>
            <th>Description</th>
            <th>Eligibility</th>
            <th>Deadline</th>
            <th>No. of Postings</th>
            <th>Application Status</th>
            <th>Status</th>
          </tr>
          <tr v-for="d in drive" :key="d[0]">
            <td>{{ d[2] }}</td>
            <td>{{ d[3] }}</td>
            <td>{{ d[4] }}</td>
            <td>{{ d[5] }}</td>
            <td>{{ d[8] }}</td>
            <td v-if="d[6] == 'PENDING'" style="background-color: yellow; color: black;">{{ d[6] }}</td>
            <td v-else-if="d[6] == 'REJECTED'" style="background-color: grey; color: white;">{{ d[6] }}</td>
            <td v-else-if="d[6] == 'APPROVED'" style="background-color: green; color: white;">{{ d[6] }}</td>
            <td v-if="d[7] == 'ACTIVATED' && d[6] == 'APPROVED'" style="background-color: green; color: white;">{{ d[7] }}</td>
            <td v-else-if="d[7] == 'REVOKED' && d[6] == 'APPROVED'" style="background-color: red; color: white;">{{ d[7] }}</td>
          </tr>
        </table>
        <br><br>
        <h2>NO OF APPLICANTS</h2>
        <table>
          <tr>
            <th>Drive</th>
            <th>Count</th>
          </tr>
          <tr v-for="count in c" :key="count[0][0]">
            <td v-if="count[0][0] != null">{{ count[0][0] }}</td>
            <td v-if="count[0][0] != null">{{ count[0][1] }}</td>
          </tr>
        </table>
    </div>
  </body>
</template>

<script>
export default {
  name: 'c_dash',
  data() {
    return {
        id: "",
        comp: [],
        drive: [],
        c: [],
    }
  },
  mounted() {
    this.id = this.$route.params.id

    fetch(`http://192.168.29.178:5000/${ this.id }/c_dash`, {credentials: 'include'})
        .then(response => response.json())
        .then(data => {
            this.comp = data.comp;
            this.drive = data.drive;
            this.c = data.c;
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
}

td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
  flex-direction: row;
}

</style>