import { createRouter, createWebHistory } from 'vue-router'
import Cookies from "js-cookie"
import { ElMessage } from 'element-plus'

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
        path: "/push",
        name: "Push",
        component: () => import("../views/side/Push.vue")
      },
      {
        path: "/class",
        name: "Class",
        component: () => import("../views/side/Class.vue")
      },
      {
        path: "/teacher",
        name: "Teacher",
        component: () => import("../views/side/Teacher.vue")
      },
      {
        path: "/student",
        name: "Student",
        component: () => import("../views/side/Student.vue")
      },
      {
        path: '/me',
        name: 'Me',
        component: () => import('../views/side/Me.vue')
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
  if(to.path == "/") {
    next();
  } else {
    const token = Cookies.get("token");

    if(token == null || token == "") {
      ElMessage({
        message: '用户未登录',
        type: 'error',
      })
      
      next({name: "Login"});
    } else {
      next();
    }
  }
})

export default router
