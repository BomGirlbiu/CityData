<template>
  <div class="menu">
    <el-aside width="200px">
      <!-- 导航栏内 -->
      <el-menu
        router
        default-active="2"
        class="el-menu-vertical-demo"
        background-color="#263238"
        text-color="#c0c4cc"
        active-text-color="#ffd04b"
      >
        <!-- 遍历渲染 -->
        <div>
          <div>
            <el-avatar
              src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
            ></el-avatar>
          </div>
          <div class="userInfo">用户:{{ name }}</div>
        </div>
        <template v-for="(item, index) in menus">
          <el-submenu :index="index + ''" :key="index" v-if="!item.hidden">
            <template slot="title">
              <i :class="item.iconClass"></i>
              <span>{{ item.name }}</span>
            </template>
            <el-menu-item-group
              v-for="(child, index) in item.children"
              :key="index"
            >
              <el-menu-item :index="child.path">
                <i :class="child.iconClass"></i>
                {{ child.name }}
              </el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </template>
        <!-- <div class="bottom-content">
          <i class="el-icon-d-arrow-left"></i>
          <el-button round class="menu-button">退出登录</el-button>                    
        </div> -->
      </el-menu>
    </el-aside>
  </div>
</template>
<script>
import { getToken } from "@/utils/setToken.js";
export default {
  data() {
    return {
      menus: [],
    };
  },
  created() {
    // 打印路由数据
    console.log(this.$router.options.routes);

    // 假设我们只想要遍历那些具有特定名称（比如 'home' 或 'about'）的路由
    const specificRoutes = this.$router.options.routes.filter((route) => {
      // 这里可以根据你的需求来修改条件
      // 例如，只选择 name 属性为 'home' 或 'about' 的路由
      return ["城市管理", "数据分析", "个人中心", "退出登录"].includes(
        route.name
      );
    });

    // 然后，将过滤后的路由数组赋值给 this.menus
    this.menus = [...specificRoutes];

    // this.menus = [...this.$router.options.routes]
    //生命周期中获取名字，登录时存储的
    this.name = getToken("username");
  },
};
</script>
<style lang="scss">
.menu {
  //上下铺满，不出现滚动条
  background-color: #263238;
  .el-aside {
    background: #ffffff;
    height: 100%;
    .el-menu {
      background: #263238;
      height: 100%;
      .fa {
        margin-right: 10px;
      }
    }
    .el-submenu .el-menu-item {
      min-width: 0;
    }
  }
  .userInfo {
    margin-bottom: 10px;
    margin-top: 10px;
  }
}
// .bottom-content{
//     position: absolute;
//     right: 0;
//     height: 8%;
//     min-width: 60px;
//     display: flex;
//     align-items: center;
//     justify-content: center;
//     border-radius: 6px;
//     cursor: pointer;
//     width: 80%;
//     display: contents;
// }
// .menu-button{
//   background-color: rgb(0 0 0 / 0%);
//   border: 0px solid #DCDFE6;
//   color: #c0c4cc;
//   // :active:-moz-any()
//   //       background-color:"#263238";
//   //       active-text-color:"#ffd04b";
// }
// .el-button.is-round{
//   padding: 13px 7px;
// }
</style>