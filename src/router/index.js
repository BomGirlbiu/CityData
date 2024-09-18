
import Vue from 'vue'
import Router from 'vue-router'
import { getToken } from '@/utils/setToken'
import { removeToken } from '@/utils/setToken'

Vue.use(Router)
//创建路由器
let router = new Router({
    routes: [
        //导航栏路由
        {
            //一级路由
            path: '/',
            name: '首页',
            //定义图标
            redirect: '/index/indexContent',//默认显示
            component: () => import('@/components/index'),
            //二级路由
            children: [
                {
                    path: '/index/indexContent',
                    name: '首页内容',
                    component: () => import('@/components/nav/indexContent')
                },
                {
                    path: '/index/news',
                    name: '热点新闻',
                    component: () => import('@/components/nav/news')
                },
                {
                    path: '/index/visual',
                    name: '大屏可视化',
                    component: () => import('@/components/nav/visual')
                },
                {
                    path: '/index/evaluate',
                    name: '城市传播指数',
                    component: () => import('@/components/nav/evaluate')
                },
                {
                    path: '/index/login',
                    name: '登录',
                    component: () => import('@/components/nav/login'),
                },
                {
                    path: '/index/register',
                    name: '注册',
                    // hidden: true,
                    component: () => import('@/components/nav/register')
                }
            ]
        },
        {
            path: '*',
            name: 'NotFound',
            hidden: true,
            component: () => import('@/components/NotFound')
        },
        {
            path: '/index/:city', // 使用动态段 :id 来匹配城市ID  
            // path: '/index/news/:city', // 使用动态段 :id 来匹配城市ID  
            name: '城市新闻详情页', // 路由名称，用于编程式导航  
            component: () => import('@/components/nav/news/newsContent.vue'),
            props: true // 如果你希望将路由参数作为props传递给组件，可以取消注释这行  
        },
        {
            //一级路由
            path: '/home',
            name: '数据分析',
            //定义图标
            iconClass: 'fa fa-users',
            redirect: '/home/citys',//默认显示
            component: () => import('@/components/home'),
            //二级路由
            children: [
                {
                    path: '/home/citys',
                    name: '传播数据',
                    iconClass: 'fa fa-list',
                    component: () => import('@/components/citys/CityList')
                },
                {
                    path: '/home/news',
                    name: '城市信息',
                    iconClass: 'fa fa-list-alt',
                    component: () => import('@/components/citys/NewsList')
                },
            ]
        },
        {
            path: '/users',
            name: '个人中心',
            iconClass: 'fa fa-user',
            component: () => import('@/components/home'),
            children: [
                {
                    path: '/users/info',
                    name: '个人信息',
                    iconClass: 'fa fa-user',
                    component: () => import('@/components/users/Info')
                }

            ]
        },
        {
            path: '/loginout',
            name: '退出登录',
            iconClass: 'el-icon-d-arrow-left',
            component: () => import('@/components/nav/login'),
            children: [
                {
                    path: '/logout1',
                    name: '返回首页',
                    iconClass: 'el-icon-back',
                    component: () => import('@/components/nav/login')
                },
                {
                    path: '/logout2',
                    name: '登录页面',
                    iconClass: 'el-icon-back',
                    component: () => import('@/components/nav/login')
                }
            ]
        },
    ],
    mode: 'history'
})

//全局守卫：前置守卫（在路由跳转之间进行判断）
router.beforeEach((to, from, next) => {
    //to:获取到要跳转到的路由信息
    //from：获取到从哪个路由跳转过来来的信息
    //next: next() 放行  next(path) 放行  
    //方便测试 统一放行
    //  next();
    //获取本地的token-----可以确定用户是登录了
    let token = getToken('id');

    if (token) {
        if (to.path === "/index/login" || to.path === "/index/register") {
            alert('你已登录'); // 弹出提示
            next('/home');
        } else {
            if ((from.path.indexOf('/home') !== -1 || from.path.indexOf('/users') !== -1) && (to.path === "/logout1" || to.path === "/logout2")) {
                removeToken('id');
                if(to.path === "/logout1") {
                    next('/index/indexContent')
                } else {
                    next('/index/login');
                }
            } else {
                next();
            }
        }
    } else {
        let toPath = to.path;
        if (toPath.indexOf('/users') !== -1 || toPath.indexOf('/home') !== -1) {
            next('/index/login');
        } else {
            next();
        }
    }
});

export default router;