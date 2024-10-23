// 后台管理整体布局
<template>
  <div class="manager-home">
    <el-container>
        <!-- 侧边栏 -->
      <el-aside style="width: 250px;">
        <Menu />
      </el-aside>

      <el-container>
        <el-header style="width:1320px"><Breadcrumb /></el-header>
        <el-main>    <router-view /></el-main>
      </el-container>

    </el-container>
  </div>
</template>

<script>
import Menu from "./Menu.vue";
import Breadcrumb from "./Breadcrumb.vue";
export default {
  name: "ManagerHome",
  components: {
    Menu,
    Breadcrumb,
  },
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
.manager-home {
  width: 100%;
  height: 100%;
}
</style>