import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: () => import("../views/Login.vue")
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import("../views/Home.vue"),
    redirect: "/student",

    // 二级路由
    children: [
      {
        path: "/student",
        name: "Student",
        component: () => import("../views/side/Student.vue")
      },
      {
        path: "/class",
        name: "Class",
        component: () => import("../views/side/Class.vue")
      },
      {
        path: "/classinfo",
        name: "ClassInfo",
        component: () => import("../views/side/ClassInfo.vue")
      },
      {
        path: '/about',
        name: 'About',
        component: () => import('../views/side/About.vue')
      },
    ]
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
