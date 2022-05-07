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
    path: '/admin/home',
    name: 'AdminHome',
    component: () => import("../views/AdminHome.vue"),
    redirect: "/admin/overview",

    // 二级路由
    children: [
      {
        path: "/admin/overview",
        name: "AdminOverview",
        component: () => import("../views/admin/Overview.vue")
      },
      {
        path: "/admin/push",
        name: "AdminPush",
        component: () => import("../views/admin/Push.vue")
      },
      {
        path: "/admin/class",
        name: "AdminClass",
        component: () => import("../views/admin/Class.vue")
      },
      {
        path: "/admin/classinfo",
        name: "AdminClassinfo",
        component: () => import("../views/admin/ClassInfo.vue")
      },
      {
        path: "/admin/teacher",
        name: "AdminTeacher",
        component: () => import("../views/admin/Teacher.vue")
      },
      {
        path: "/admin/student",
        name: "AdminStudent",
        component: () => import("../views/admin/Student.vue")
      },
      {
        path: '/admin/me',
        name: 'AdminMe',
        component: () => import('../views/admin/Me.vue')
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
