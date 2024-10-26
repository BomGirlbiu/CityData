import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  //显示首页
  {
    path: "/",
    redirect: "/FirstPage",
  },
  {
    //一级路由
    path: "/FirstPage",
    name: "首页",
    //定义图标
    component: () => import("@/otherViews/FirstPage"),
  },
  {
    //一级路由
    path: "/CityInfo",
    name: "城市信息",
    //定义图标npm
    component: () => import("@/otherViews/CityInfo/CityInfo"),
  },
  {
    //一级路由
    path: "/CityFood",
    name: "美食天地",
    //定义图标npm
    component: () => import("@/otherViews/CityInfo/CityFood"),
  },
  {
    //一级路由
    path: "/CityTravel",
    name: "旅游空间",
    //定义图标npm
    component: () => import("@/otherViews/CityInfo/CityTravel"),
  },
  {
    //一级路由
    path: "/CityNews",
    name: "热点讯息",
    //定义图标npm
    component: () => import("@/otherViews/CityInfo/CityNews"),
  },
  {
    //一级路由
    path: "/DetailData",
    name: "数据跟踪",
    //定义图标npm
    component: () => import("@/otherViews/DetailData/DetailData"),
  },
  {
    //一级路由
    path: "/BigScreen",
    name: "城市对比",
    //定义图标npm
    component: () => import("@/otherViews/BigScreen/BigScreen"),
  },

  // 个人中心
  {
    //一级路由
    path: "/HomePage",
    name: "个人中心",
    //定义图标npm
    component: () => import("@/otherViews/Home/HomePage"),
    children: [
      {
        path: "/HomePage/PageMain",
        component: () => import("@/otherViews/Home/PageMain"),
      },
      {
        path: "/HomePage/withdrawal",
        component: () => import("@/otherViews/Home/UserWithdrawal"),
      },
    ],
  },

  // 社区
  {
    path: "/Community",
    name: "城市频道",
    redirect: "/Community/Home",
    component: () => import("@/views/CommunityLayout"),
    children: [
      {
        path: "/Community/Home",
        component: () => import("@/views/Home"),
      },
    ],
  },
// 管理员
{
  path: '/managerLogin',
  name: '管理员登录',
  //定义图标
  component: () => import('@/otherViews/Manager/Login/Login'),
},
{
  //一级路由
  path: '/ManagerHome',
  name: '后台管理',
  //定义图标
  redirect: '/ManagerHome/CityData',//默认显示城市数据模块
  component: () => import('@/otherViews/Manager/Layout/ManagerHome'),
  children: [
      {
          path: '/ManagerHome/CityData',
          name: '城市信息',
          redirect:'/ManagerHome/CityData/food',
          component: () => import('@/otherViews/Manager/CityData/CityData'),
          children:[
              {
                  path: '/ManagerHome/CityData/food',
                  name: '城市信息-美食',
                  component: () => import('@/otherViews/Manager/CityData/food'),
              },
              {
                  path: '/ManagerHome/CityData/travel',
                  name: '城市信息-旅游',
                  component: () => import('@/otherViews/Manager/CityData/travel'),
              },
              {
                  path: '/ManagerHome/CityData/news',
                  name: '城市信息-新闻',
                  component: () => import('@/otherViews/Manager/CityData/news'),
              }

          ]
      },
    ]
  },
  {
    path: "/register",
    name: "register",
    component: () => import("@/views/auth/Register"),
    meta: { title: "注册" },
  },
  // 登录
  {
    name: "登录",
    path: "/login",
    component: () => import("@/views/auth/Login"),
    meta: { title: "登录" },
  },
  // 发布
  {
    name: "post-create",
    path: "/post/create",
    component: () => import("@/views/post/Create"),
    meta: { title: "信息发布", requireAuth: true },
  },
  // 编辑
  {
    name: "topic-edit",
    path: "/topic/edit/:id",
    component: () => import("@/views/post/Edit"),
    meta: {
      title: "编辑",
      requireAuth: true,
    },
  },
  // 详情
  {
    name: "post-detail",
    path: "/post/:id",
    component: () => import("@/views/post/Detail"),
    meta: { title: "详情" },
  },
  {
    name: "tag",
    path: "/tag/:name",
    component: () => import("@/views/tag/Tag"),
    meta: { title: "主题列表" },
  },
  // 检索
  {
    name: "search",
    path: "/search",
    component: () => import("@/views/Search"),
    meta: { title: "检索" },
  },
  // 用户主页
  {
    name: "user",
    path: "/member/:username/home",
    component: () => import("@/views/user/Profile"),
    meta: { title: "用户主页" },
  },
  // 用户设置
  {
    name: "user-setting",
    path: "/member/:username/setting",
    component: () => import("@/views/user/Setting"),
    meta: { title: "设置", requireAuth: true },
  },
  {
    path: "/404",
    name: "404",
    component: () => import("@/views/error/404"),
    meta: { title: "404-NotFound" },
  },
  {
    path: "*",
    redirect: "/404",
    hidden: true,
  },
];


const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch((err) => err);
};

const router = new VueRouter({
  routes,
  mode: "history",
});

export default router;
