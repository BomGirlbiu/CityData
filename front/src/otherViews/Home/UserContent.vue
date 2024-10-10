
// 路由出口
<template>
  <div class="content">
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>
</template>

<script>
export default {
  name: "UserContent",
};
</script>

<style scoped>
.content {
  background: #fff;
  vertical-align: top;
  display: inline-block;
  width: 1170px;
  height: 100%;
  margin-left: 10px;
  overflow-y: auto;
  overflow: hidden;
  border-radius: 15px;
}
.content-main {
  margin: 20px;
  text-align: left;
}
</style>
