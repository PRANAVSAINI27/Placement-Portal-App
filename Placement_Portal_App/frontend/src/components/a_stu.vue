<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <img src="@/assets/placement.png" alt="Logo" class="navbar-logo" />
      <h1>Placement Portal Application</h1>
    </div>
    <div class="navbar-links">
      <router-link class="router-link" to="/admin/a_home">Home</router-link>
      <router-link class="router-link" to="/admin/a_companies">Companies</router-link>
      <router-link class="router-link" to="/admin/a_drives">Drives</router-link>
      <router-link class="router-link" style="color: red;" to="/logout">Log Out</router-link>
    </div>
  </nav>

  <body>
    <div class="content">
      <h2>STUDENTS</h2>
            <table>
                <tr><th style="width: 5%;">ID</th>
                    <th style="width: 25%;">Name</th>
                    <th style="width: 15%;">Branch</th>
                    <th style="width: 10%;">Contact</th>
                    <th style="width: 5%;">CGPA</th>
                    <th style="width: 5%;">Year</th>
                    <th style="width: 20%;"><input type="text" v-model="search" placeholder="Search STUDENT NAME" style="width: 100%;"></th>
                </tr>
                <tr v-for="student in filteredStudents" :key="student[0]" style="margin-bottom: 10px;">
                    <td>{{ student[0] }}</td>
                    <td>{{ student[1] }}</td>
                    <td>{{ student[2] }}</td>
                    <td>{{ student[3] }}</td>
                    <td>{{ student[4] }}</td>
                    <td>{{ student[5] }}</td>
                    <td v-if="student[6] == 'PENDING'" style="background-color: yellow; color: black;">
                      <p style="color: black; display: inline;">{{ student[6] }}</p>
                      <a :href="'http://192.168.29.178:5000/admin/a_s_approval/APPROVED/' + student[0]" ><button style="color: green;">Approve</button></a>
                      <a :href="'http://192.168.29.178:5000/admin/a_s_approval/REJECTED/' + student[0]" ><button style="color: red;">Reject</button></a>
                    </td>
                    <td v-else-if="student[6] == 'REJECTED'" style="background-color: grey; color: white;">
                      <p style="color: white; display: inline;">{{ student[6] }}</p>
                    </td>
                    <td v-if="student[7] == 'ACTIVATED' && student[6] == 'APPROVED'" style="background-color: green; color: white;">
                      <p style="color: white; display: inline;">{{ student[7] }}</p>
                      <a :href="'http://192.168.29.178:5000/admin/a_s_status/DEACTIVATED/' + student[0]" ><button style="color: blue;">Deactivate</button></a>
                      <a :href="'http://192.168.29.178:5000/admin/a_s_status/BLACKLISTED/' + student[0]" ><button style="color: black;">Blacklist</button></a>
                    </td>
                    <td v-else-if="student[7] == 'DEACTIVATED' && student[6] == 'APPROVED'" style="background-color: red; color: white;">
                      <p style="color: white; display: inline;">{{ student[7] }}</p>
                      <a :href="'http://192.168.29.178:5000/admin/a_s_status/ACTIVATED/' + student[0]" ><button style="color: green;">Activate</button></a>
                    </td>
                    <td v-else-if="student[7] == 'BLACKLISTED' && student[6] == 'APPROVED'" style="background-color: black; color: white;">BLACKLISTED</td>
                </tr>
            </table>
    </div>
  </body>
</template>

<script>
export default {
  name: 'a_students',
  data() {
    return {
        students: [],
        search: ""
    };
  },

    mounted() {
        fetch('http://192.168.29.178:5000/admin/a_students', {credentials: 'include'})
            .then(response => response.json())
            .then(data => {
                this.students = data;
            });
    },

  computed: {
    filteredStudents() {
        return this.students.filter(student => {
            return student[1]
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