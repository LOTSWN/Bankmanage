import {createRouter, createWebHistory} from "vue-router";
import Home from "../views/Home.vue";

const routes = [
    {
        path: '/',
        redirect: '/home'
    }, {
        path: "/",
        name: "Home",
        component: Home,
        children: [
            {
                path: 'home',
                name: "home",
                meta: {
                    title: '主页'
                },
                component: () => import (
                /* webpackChunkName: "adminInfo" */
                "../views/adminInfo.vue")
            }, 
            {
                path: "/admininfo",
                name: "admininfo",
                meta: {
                    title: '管理员信息'
                },
                component: () => import (
                /* webpackChunkName: "adminInfo" */
                "../views/adminInfo.vue")
            }, {
                path: "/newclient",
                name: "newclient",
                meta: {
                    title: '用户创建'
                },
                component: () => import (
                /* webpackChunkName: "newClient" */
                "../views/newClient.vue")
            },{
                path: "/savenote",
                name: "savenote",
                meta: {
                    title: '储蓄账户创建'
                },
                component: () => import (
                /* webpackChunkName: "savenote" */
                "../views/savenote.vue")
            },{
                path: "/savemanage",
                name: "savemanage",
                meta: {
                    title: '储蓄账户管理'
                },
                component: () => import (
                /* webpackChunkName: "savemanage" */
                "../views/savemanage.vue")
            },{                
                path: "/loannote",
                name: "loannote",
                meta: {
                    title: '贷款申请'
                },
                component: () => import (
                /* webpackChunkName: "loannote" */
                "../views/loannote.vue")
            },{                
                path: "/fuser",
                name: "fuser",
                meta: {
                    title: '用户信息查询'
                },
                component: () => import (
                /* webpackChunkName: "fuser" */
                "../views/fuser.vue")
            },{
                path: "/fuloan",
                name: "fuloan",
                meta: {
                    title: '贷款账户查询'
                },
                component: () => import (
                /* webpackChunkName: "fuloan" */
                "../views/fuloan.vue")
            }, {
                path: "/fusave",
                name: "fusave",
                meta: {
                    title: '储蓄账户查询',
                },
                component: () => import (
                /* webpackChunkName: "fusave" */
                "../views/fusave.vue")
            }, {
                path: '*',
                name: '*',
                meta: {
                    title: '找不到页面'
                },
                component: () => import (/* webpackChunkName: "404" */
                '../views/404.vue')
            }
        ]
    }, 
    {
        path: "/login",
        name: "Login",
        meta: {
            title: '登录'
        },
        component: () => import (
        /* webpackChunkName: "login" */
        "../views/Login.vue")
    },
    {
        path: "/adminlogin",
        name: "adminLogin",
        meta: {
            title: '管理员登录'
        },
        component: () => import (
        /* webpackChunkName: "login" */
        "../views/adminLogin.vue")
    }
    
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | vue-manage-system`;
    const role = localStorage.getItem('user_type');
    if (!role && to.path !== '/login' && to.path !== '/adminlogin') {
        next('/login');
    } else {
        next();
    }
});

export default router;