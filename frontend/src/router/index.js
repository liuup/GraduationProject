import { createRouter, createWebHistory } from 'vue-router'
// import Cookies from "js-cookie"

const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import("../views/Login.vue")
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import("../views/Home.vue"),
    redirect: "/overview",

    // 二级路由
    children: [
      {
        path: "/overview",
        name: "Overview",
        component: () => import("../views/side/Overview.vue")
      },
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
        path: '/myself',
        name: 'Myself',
        component: () => import('../views/side/Myself.vue')
      },
      {
        path: '/about',
        name: 'About',
        component: () => import('../views/side/About.vue')
      },
    ]
  },
  {
    path: '/:path(.*)',
    name: 'NotFound',
    component: () => import("../views/NotFound.vue")
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// 导航守卫
router.beforeEach((to, from, next) => {
  const token = Cookies.get("token");

  if(!token || to.name != "Login") {
    next({name: "Login"});
  } else {
    next();
  }
})

export default router
