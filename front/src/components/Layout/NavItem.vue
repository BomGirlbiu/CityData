<template>
  <div class="nav">
    <header class="Header" data-header>
      <div class="Header-inner" data-header-nav>
        <div class="logo">
          <img src="https://i.imgur.com/F0k8l7N.png" alt="" />
        </div>
        <nav class="Header-nav" data-nav>
          <div class="Header-nav-item" data-nav-item="1">
            <router-link :to="{ name: '首页' }">首页</router-link>
          </div>
          <div class="Header-nav-item" data-nav-item="2">
            <router-link :to="{ name: '城市信息' }">城市信息</router-link>
          </div>
          <div class="Header-nav-item" data-nav-item="3">
            <router-link to="/">城市分析</router-link>
          </div>
          <div class="Header-nav-item" data-nav-item="4">
            <router-link to="/">数据对比</router-link>
          </div>
          <div class="Header-nav-item" data-nav-item="5">
            <router-link :to="{ name: '城市频道' }">城市频道</router-link>
          </div>
          <!-- <div class="Header-nav-item" data-nav-item="6">
            <router-link :to="{ name: '用户登录' }"
              ><el-avatar :size="50"> user </el-avatar></router-link
            >
                        <router-link :to="{ path: `/member/${user.username}/setting` }"
              ><el-avatar :size="50"> user </el-avatar></router-link
            >
            
          </div> -->
        </nav>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  name: "NavItem",
  methods: {
  },
};
</script>

<style lang="scss" scope>
$header-transition: 0.4s ease;
.Header {
  align-items: center;
  background: white;
  border-bottom-left-radius: 30px;
  border-bottom-right-radius: 30px;
  display: flex;
  height: 100px;
  justify-content: center;
  position: fixed;
  text-align: center;
  top: 0;
  width: 97%;
  z-index: 10;
  margin-left: 20px;

  &.has-mobile-button {
    .MobileNav-trigger {
      display: flex;
    }
  }

  &-inner {
    display: flex;
    justify-content: space-between;
    transition: height $header-transition;
    width: 80vw;
  }

  .logo {
    align-self: center;
    display: flex;
    height: 80px;
    margin-right: 60px;
    width: 200px;

    img {
      height: 100%;
      object-fit: contain;
      width: 100%;
    }
  }

  &-nav {
    display: flex;
    flex-wrap: wrap;
    height: 0;
    justify-content: space-between;
    max-height: 105px;
    max-width: 940px;
    overflow: hidden;
    width: 100%;

    &-item {
      align-items: center;
      align-self: center;
      color: darkblue;
      display: flex;
      flex-shrink: 0;
      font-family: Lato, sans-serif;
      font-size: 20px;
      font-weight: bold;
      height: 100%;
      line-height: 32px;
      margin: 0 40px;
      transition: font-size $header-transition, padding $header-transition;

      &:last-child {
        margin-right: 0;
      }

      a {
        color: black;
        text-decoration: none;
      }

      &:hover {
        color: darkblue !important;
      }
    }

    &:hover {
      .Header-nav-item {
        color: rgba(darkblue, 0.5);
      }
    }
  }

  @media screen and (min-width: 481px) {
    &-nav {
      height: auto;
    }
  }
}
</style>