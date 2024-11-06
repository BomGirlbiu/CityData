import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters'
import user from './modules/user'

Vue.use(Vuex)
// 用于响应组件中的动作
const actions = {
}
// 用于操作数据
const mutations = {
    CURRENTCITY(state, ProvinceName) {
        console.log("选择了页面", ProvinceName)
        state.currentProvince=ProvinceName
    },
}
// 用于存储数据
const state = {
    currentProvince:''//显示用户选择的内容（美食、政治...）
}
const store = new Vuex.Store({
    modules: {
        user
    },
    getters,
    actions,
    mutations,
    state,
})

export default store