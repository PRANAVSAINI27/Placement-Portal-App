<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <img src="@/assets/placement.png" alt="Logo" class="navbar-logo" />
      <h1>Placement Portal Application</h1>
    </div>
    <div class="navbar-links">
      <router-link class="router-link" :to= "'/' + id + '/s_dash'">Home</router-link>
      <router-link class="router-link" :to="'/' + id + '/s_appr'">Approved</router-link>
      <router-link class="router-link" :to="'/' + id + '/s_profile'">Profile</router-link>
      <router-link class="router-link" style="color: red;" to="/logout">Log Out</router-link>
    </div>
  </nav>

  <body>
    <div class="content">
      <h2>APPLICATIONS</h2>
      <p>
        <input type="text" v-model="search" placeholder="Search Title" style="width: 25%; margin-left: 75%;">
        </p>
        <table>
          <tr>
            <th>Title</th>
            <th>Description</th>
            <th>Company Name</th>
            <th>Application Date</th>
            <th>Status</th>
          </tr>
          <tr v-for="appl in filteredApplications" :key="appl[0]">
            <td>{{ appl[1] }}</td>
            <td>{{ appl[2] }}</td>
            <td>{{ appl[5] }}</td>
            <td>{{ appl[3] }}</td>
            <td v-if="appl[4] == 'PENDING'" style="background-color: yellow;">{{ appl[4] }}</td>
            <td v-if="appl[4] == 'REJECTED'">{{ appl[4] }}</td>
          </tr>
          <tr></tr>
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
        appl: [],
        search: "",
    }
  },
  mounted() {
    this.id = this.$route.params.id

    fetch(`http://192.168.29.178:5000/${ this.id }/s_appl`, {credentials: 'include'})
        .then(response => response.json())
        .then(data => {
            this.appl = data;
        });
    },
    computed: {
    filteredApplications() {
        return this.appl.filter(appl => {
            return appl[1]
                .toLowerCase()
                .includes(this.search.toLowerCase())
        })
    }
  }
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