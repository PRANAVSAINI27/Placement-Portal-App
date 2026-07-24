<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <img src="@/assets/placement.png" alt="Logo" class="navbar-logo" />
      <h1>Placement Portal Application</h1>
    </div>
    <div class="navbar-links">
      <router-link class="router-link" to="/admin/a_home">Home</router-link>
      <router-link class="router-link" to="/admin/a_drives">Drives</router-link>
      <router-link class="router-link" to="/admin/a_students">Students</router-link>
      <router-link class="router-link" style="color: red;" to="/logout">Log Out</router-link>
    </div>
  </nav>

  <body>
    <div class="content">
      <h2>COMPANIES</h2>
            <table>
                <tr>
                    <th style="width: 30%;">Name</th>
                    <th style="width: 10%;">HR Contact</th>
                    <th style="width: 30%;">Website</th>
                    <th style="width: 30%;"><input type="text" v-model="search" placeholder="Search COMPANY NAME" style="width: 100%;"></th>
                </tr>
                <tr v-for="company in filteredCompanies" :key="company[0]" style="margin-bottom: 10px;">
                    <td>{{ company[1] }}</td>
                    <td>{{ company[2] }}</td>
                    <td>{{ company[3] }}</td>
                    <td v-if="company[5] == 'PENDING'" style="background-color: yellow; color: black;">
                      <p style="color: black; display: inline;">{{ company[5] }}</p>
                      <a :href="'http://192.168.29.178:5000/admin/a_approval/APPROVED/' + company[0]" ><button style="color: green;">Approve</button></a>
                      <a :href="'http://192.168.29.178:5000/admin/a_approval/REJECTED/' + company[0]" ><button style="color: red;">Reject</button></a>
                    </td>
                    <td v-else-if="company[5] == 'REJECTED'" style="background-color: grey; color: white;">
                      <p style="color: white; display: inline;">{{ company[5] }}</p>
                    </td>
                    <td v-if="company[6] == 'ACTIVATED' && company[5] == 'APPROVED'" style="background-color: green; color: white;">
                      <p style="color: white; display: inline;">{{ company[6] }}</p>
                      <a :href="'http://192.168.29.178:5000/admin/a_status/DEACTIVATED/' + company[0]" ><button style="color: blue;">Deactivate</button></a>
                      <a :href="'http://192.168.29.178:5000/admin/a_status/BLACKLISTED/' + company[0]" ><button style="color: black;">Blacklist</button></a>
                    </td>
                    <td v-else-if="company[6] == 'DEACTIVATED' && company[5] == 'APPROVED'" style="background-color: red; color: white;">
                      <p style="color: white; display: inline;">{{ company[6] }}</p>
                      <a :href="'http://192.168.29.178:5000/admin/a_status/ACTIVATED/' + company[0]" ><button style="color: green;">Activate</button></a>
                    </td>
                    <td v-else-if="company[6] == 'BLACKLISTED' && company[5] == 'APPROVED'" style="background-color: black; color: white;">BLACKLISTED</td>
                </tr>
            </table>
    </div>
  </body>
</template>

<script>
export default {
  name: 'a_companies',
    data() {
        return {
        companies: [],
        search: ""
        }
    },
    mounted() {
        fetch('http://192.168.29.178:5000/admin/a_companies', {credentials: 'include'})
            .then(response => response.json())
            .then(data => {
                this.companies = data;
            });
    },

  computed: {
    filteredCompanies() {
        return this.companies.filter(company => {
            return company[1]
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
}

td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
  flex-direction: row;
}

</style>