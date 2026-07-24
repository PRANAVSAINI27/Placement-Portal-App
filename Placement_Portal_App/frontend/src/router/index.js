import { createRouter, createWebHistory } from 'vue-router';
import a_home from '../components/a_home.vue';
import g_home from '../components/g_home.vue';
import a_comp from '../components/a_comp.vue';
import a_stu from '../components/a_stu.vue';
import a_drive from '../components/a_drive.vue';
import a_log from '../components/a_log.vue';
import logout from '../components/logout.vue'; 
import s_log from '../components/s_log.vue';
import s_dash from '../components/s_dash.vue';
import s_appl from '../components/s_appl.vue';
import s_appr from '../components/s_appr.vue';
import s_profile from '../components/s_profile.vue';
import _login from '../components/login.vue';
import _register from '../components/register.vue';
import c_log from '../components/c_log.vue';
import c_dash from '../components/c_dash.vue';
import c_cdrive from '../components/c_cdrive.vue';
import c_appl from '../components/c_appl.vue';
import s_register from '../components/s_register.vue';
import c_register from '../components/c_register.vue';

const routes = [
  {
    path: '/admin/a_home',
    component: a_home,
  },
  {
    path: '/',
    component: g_home,
  },
  {
    path: '/admin/a_companies',
    component: a_comp,
  },
  {
    path: '/admin/a_students',
    component: a_stu,
  },
  {
    path: '/admin/a_drives',
    component: a_drive,
  },
  {
    path: '/a_login',
    component: a_log,
  },
  {
    path: '/logout',
    component: logout,
  },
  {
    path: '/s_login',
    component: s_log,
  },
  {
    path: '/:id/s_dash',
    component: s_dash,
  },
  {
    path: '/:id/s_appl',
    component: s_appl,
  },
  {
    path: '/:id/s_appr',
    component: s_appr,
  },
  {
    path: '/:id/s_profile',
    component: s_profile,
  },
  {
    path: '/login',
    component: _login,
  },
  {
    path: '/register',
    component: _register,
  },
  {
    path: '/c_login',
    component: c_log,
  },
  {
    path: '/:id/c_dash',
    component: c_dash,
  },
  {
    path: '/:id/c_cdrive',
    component: c_cdrive,
  },
  {
    path: '/:id/c_appl',
    component: c_appl,
  },
  {
    path: '/s_reg',
    component: s_register,
  },
  {
    path: '/c_reg',
    component: c_register,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;