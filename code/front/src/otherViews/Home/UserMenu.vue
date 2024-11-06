// 侧边导航
<template>
  <div class="menu">
    <ul class="menu-ul">
      <router-link class="menu-link" to="/HomePage/PageMain" tag="li"
        >主页</router-link
      >
      <router-link class="menu-link" to="/HomePage/withdrawal" tag="li"
        >动态</router-link
      >
      <router-link class="menu-link" to="/HomePage/recharge" tag="li"
        >投稿</router-link
      >
      <router-link class="menu-link" to="/HomePage/recharge" tag="li"
        >收藏</router-link
      >
      <router-link class="menu-link" to="/HomePage/recharge" tag="li"
        >设置</router-link
      >
      <router-link class="menu-link" to="/ManagerHome" tag="li"
        ><el-button icon="el-icon-search" circle></el-button
      ></router-link>
    </ul>
  </div>
</template>

<script>
export default {
  name: "UserMenu",
};
</script>

<style scoped>
.menu {
  background: #fff;
  width: 300px;
  height: 740px;
  margin-top: 15px;
  text-align: left;
  color: #737373;
  border-radius: 15px;
}
.menu-ul {
  padding: 0;
  margin: 0;
}
.router-link-active {
  font-weight: bold;
  color: #353535;
  background: #dcf9f5;
}
.menu-link {
  list-style-type: none;
  height: 60px;
  cursor: pointer;
  line-height: 60px;
  padding: 0 0 0 25px;
  transition: all 0.4s;
  border-radius: 15px;
}
</style>