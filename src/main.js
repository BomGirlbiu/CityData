import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'font-awesome/css/font-awesome.min.css'
import router from './router'
import service from './service'
import echarts from 'echarts'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueSlideMini from 'vue-slide-mini'
Vue.use(VueSlideMini)
Vue.use(BootstrapVue)
Vue.use(ElementUI)
Vue.prototype.service = service // 挂载到原型,可以在全局使用
Vue.prototype.$echarts = echarts 
Vue.config.productionTip = false
Vue.config.productionTip = false;

// 路由导航守卫
router.beforeEach((to, from, next) => {
  if (!localStorage.getItem('username')) {
    if (to.path !== '/login') {
      next('/login')
    } else next()
  } next()
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
