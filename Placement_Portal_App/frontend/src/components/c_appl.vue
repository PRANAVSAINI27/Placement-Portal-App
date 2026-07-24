<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <img src="@/assets/placement.png" alt="Logo" class="navbar-logo" />
      <h1>Placement Portal Application</h1>
    </div>
    <div class="navbar-links">
      <router-link class="router-link" :to="'/' + id + '/c_dash'">Home</router-link>
      <router-link class="router-link" :to="'/' + id + '/c_cdrive'">Create Drive</router-link>
      <router-link class="router-link" style="color: red;" to="/logout">Log Out</router-link>
    </div>
  </nav>

  <body>
    <div class="content">
      <h2>APPLICATIONS</h2>
        <table>
          <tr>
            <th>Student ID</th>
            <th>Description</th>
            <th>Application Date</th>
            <th>Status</th>
            <th></th>
          </tr>
          <template v-for="appl in applications" :key="appl[0]">
            <tr v-if="appl[0] != null">
                <td>{{ appl[1] }}</td>
                <td>{{ appl[2] }}</td>
                <td>{{ appl[3] }}</td>
                <td v-if="appl[4] == 'PENDING'" style="background-color: yellow;">{{ appl[4] }}
                    <a :href="'http://192.168.29.178:5000/' + id + '/c_uappl/APPROVED/' + appl[0]" ><button style="color: green;">Approve</button></a>
                    <a :href="'http://192.168.29.178:5000/' + id + '/c_uappl/REJECTED/' + appl[0]" ><button style="color: red;">Reject</button></a>
                </td>
                <td v-else-if="appl[4] == 'REJECTED'" style="background-color: gray;">{{ appl[4] }}</td>
                <td v-else-if="appl[4] == 'APPROVED'" style="background-color: green;">{{ appl[4] }}</td>
            </tr>
        </template>
        </table>
    </div>
  </body>
</template>

<script>
export default {
  name: 's_appl',
  data() {
    return {
        id: "",
        applications: [],
    }
  },
  mounted() {
    this.id = this.$route.params.id

    fetch(`http://192.168.29.178:5000/${ this.id }/c_appl`, {credentials: 'include'})
        .then(response => response.json())
        .then(data => {
            this.applications = data;
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