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
    path: "/teacher/home",
    name: "TeacherHome",
    component: () => import("../views/TeacherHome.vue"),
    redirect: "/teacher/overview",

    children: [
      {
        path: "/teacher/overview",
        name: "TeacherOverview",
        component: () => import("../views/teacher/Overview.vue")
      },
      {
        path: "/teacher/class",
        name: "TeacherClass",
        component: () => import("../views/teacher/Class.vue")
      },
      {
        path: "/teacher/student",
        name: "TeacherStudent",
        component: () => import("../views/teacher/Student.vue")
      },
      {
        path: "/teacher/me",
        name: "TeacherMe",
        component: () => import("../views/teacher/Me.vue")
      },
    ]
  },
  {
    path: "/stu/home",
    name: "StuHome",
    component: () => import("../views/StuHome.vue"),
    redirect: "/stu/overview",

    children: [
      {
        path: "/stu/overview",
        name: "StuOverview",
        component: () => import("../views/stu/Overview.vue")
      },
      {
        path: "/stu/me",
        name: "StuMe",
        component: () => import("../views/stu/Me.vue")
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
