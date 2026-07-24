<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <img src="@/assets/placement.png" alt="Logo" class="navbar-logo" />
      <h1>Placement Portal Application</h1>
    </div>
    <div class="navbar-links">
      <router-link class="router-link" :to="'/' + id + '/s_appl'">Application Status</router-link>
      <router-link class="router-link" :to="'/' + id + '/s_appr'">Approved</router-link>
      <router-link class="router-link" :to="'/' + id + '/s_profile'">Profile</router-link>
      <router-link class="router-link" style="color: red;" to="/logout">Log Out</router-link>
    </div>
  </nav>

  <body>
    <div class="content">
      <h2>DRIVES</h2>
        <table>
          <tr>
            <th>Company Name</th>
            <th>Title</th>
            <th>Description</th>
            <th>Eligibility Criteria</th>
            <th>Application Deadline</th>
            <th><input type="text" v-model="search" placeholder="Search Title" style="width: 100%;"></th>
          </tr>
          <tr v-for="drive in filteredDrives" :key="drive[0]">
            <td>{{ drive[1] }}</td>
            <td>{{ drive[2] }}</td>
            <td>{{ drive[3] }}</td>
            <td>{{ drive[4] }}</td>
            <td>{{ drive[5] }}</td>
            <td v-if="drive[6] == 'APPROVED' && drive[7] != 'REVOKED' && new Date(drive[5]) >= new Date()">
              <form :action="'http://192.168.29.178:5000/' + id + '/s_apply'" method="POST">
                <input type="hidden" name="drive_id" :value="drive[0]">
                <button type="submit">APPLY</button>
              </form>
            </td>
          </tr>
        </table>
        <form :action="'http://192.168.29.178:5000/' + id + '/s_export_csv'" method="POST">
          <button type="submit">Export CSV</button>
        </form>
        <form :action="'http://192.168.29.178:5000/' + id + '/s_download_csv'" method="POST">
          <button type="submit">Download CSV</button>
        </form>
    </div>
  </body>
</template>

<script>
export default {
  name: 's_dash',
  data() {
    return {
        id: "",
        eligible_drives: [],
        search: "",
    }
  },
  mounted() {
    this.id = this.$route.params.id;

    fetch(`http://192.168.29.178:5000/${this.id}/s_dash`, {
        credentials: "include"
    })
    .then(response => {
        console.log(response.status);

        if (!response.ok) {
            throw new Error("HTTP " + response.status);
        }

        return response.json();
    })
    .then(data => {
        console.log(data);
        this.eligible_drives = data;
    })
    .catch(err => {
        console.log(err);
    });
},
    computed: {
    filteredDrives() {
        return this.eligible_drives.filter(drives => {
            return drives[2]
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