<template>
  <div class="home-page">
    <div class="nav">
      <nav-item />
    </div>
    <div class="container-user">
      <div class="left">
        <UserInfo
          :nick="userInfo.nick || ''"
          :portrait="userInfo.portrait || ''"
          :level="userInfo.ulevel || 1"
          :uid="userInfo.uid || ''"
          :starNumber="userInfo.point || 0"
          :diamondNumber="userInfo.gold || 0"
        ></UserInfo>
        <UserMenu :uid="userInfo.uid"></UserMenu>
      </div>
      <UserContent></UserContent>
    </div>
  </div>
</template>

<script>
import UserInfo from "./UserInfo.vue";
import UserMenu from "./UserMenu.vue";
import UserContent from "./UserContent.vue";
import NavItem from "../NavItem.vue";

export default {
  name: "HomePage",
  data() {
    return {
      isLogin: false,
      userInfo: {
        //保存用户信息
        nick: null,
        ulevel: null,
        uid: null,
        gold: null,
        point: null,
        portrait: null,
      },
    };
  },
  components: {
    UserInfo,
    UserMenu,
    UserContent,
    NavItem,
  },
  mounted() {
    //组件开始挂载时获取用户信息
    this.getUserInfo();
    // this.loadData();
    //获取元素
    const container = document.querySelector(".container");
    const imgs = document.querySelectorAll("img");

    //绑定鼠标移入事件
    container.addEventListener("mouseenter", function (e) {
      //获取鼠标在移入时的偏移
      this.x = e.clientX;
      //移除过渡效果
      imgs.forEach((item) => {
        item.style.transition = "none";
      });
    });
    //绑定鼠标移动事件
    container.addEventListener("mousemove", function (e) {
      //获取鼠标移动时的偏移
      this._x = e.clientX;
      //计算鼠标移动的向量
      let disX = this._x - this.x;

      //第一张图的初始值以及变化
      //filter  blur(4px)
      //transform: translate(0px, 0px)
      //变化
      //x       0    1920    1920    disX
      //filter  4     8       4       ???
      const blur_0 = Math.abs(4 + (4 * disX) / 1920);
      imgs[0].style.filter = `blur(${blur_0}px)`;

      //第二张图的初始值以及变化
      //filter  blur(0px)
      //transform: translate(0px, 0px)
      //变化
      //x             0    1920        disX
      //filter        0     10          ???
      //translate     0     10
      const blur_1 = Math.abs((10 * disX) / 1920);
      const translateX_1 = (10 * disX) / 1920;
      imgs[1].style.filter = `blur(${blur_1}px)`;
      imgs[1].style.transform = `translate(${translateX_1}px, 0px) rotate(0deg)`;

      //第三张图的初始值以及变化
      //filter  blur(1px)
      //transform: translate(-58px, 0px)
      //变化
      //x             0       1920        disX
      //filter        1       -5          ???
      //translate     -58     10          ???
      const blur_2 = Math.abs(1 - (5 * disX) / 1920);
      const translateX_2 = -58 + (10 * disX) / 1920;
      imgs[2].style.filter = `blur(${blur_2}px)`;
      imgs[2].style.transform = `translate(${translateX_2}px, 0px) rotate(0deg)`;

      //第四张图的初始值以及变化
      //filter  blur(4px)
      //transform: translate(0px, 4.87742px)
      //变化
      //x             0       1920        disX
      //filter        4       -10          ???
      //translate     0        42          ???
      const blur_3 = Math.abs(4 - (10 * disX) / 1920);
      const translateX_3 = (42 * disX) / 1920;
      imgs[3].style.filter = `blur(${blur_3}px)`;
      imgs[3].style.transform = `translate(${translateX_3}px, 4.87742px) rotate(0deg)`;

      //第五张图的初始值以及变化
      //filter  blur(5px)
      //transform: translate(0px, -2.09032px)
      //变化
      //x             0       1920        disX
      //filter        5       -10          ???
      //translate     0        91          ???
      const blur_4 = Math.abs(5 - (10 * disX) / 1920);
      const translateX_4 = (91 * disX) / 1920;
      imgs[4].style.filter = `blur(${blur_4}px)`;
      imgs[4].style.transform = `translate(${translateX_4}px, -2.09032px) rotate(0deg)`;

      //第六张图的初始值以及变化
      //filter  blur(5px)
      //transform: translate(0px, 0px)
      //变化
      //x             0       1920        disX
      //filter        6       -6          ???
      //translate     0        114        ???
      const blur_5 = Math.abs(6 - (6 * disX) / 1920);
      const translateX_5 = (114 * disX) / 1920;
      imgs[5].style.filter = `blur(${blur_5}px)`;
      imgs[5].style.transform = `translate(${translateX_5}px, 0px) rotate(0deg)`;
    });
    //绑定鼠标离开事件
    container.addEventListener("mouseleave", function () {
      //增加过渡效果
      imgs.forEach((item) => {
        item.style.transition = "all 0.5s";
      });
      //样式清空
      imgs[0].style.filter = "blur(4px)";
      imgs[0].style.transform = "translate(0px, 0px) rotate(0deg)";

      imgs[1].style.filter = "blur(0px)";
      imgs[1].style.transform = "translate(0px, 0px) rotate(0deg)";

      imgs[2].style.filter = "blur(1px)";
      imgs[2].style.transform = "translate(-58.0645px, 0px) rotate(0deg)";

      imgs[3].style.filter = "blur(4px)";
      imgs[3].style.transform = "translate(0px, 4.87742px) rotate(0deg)";

      imgs[4].style.filter = "blur(5px)";
      imgs[4].style.transform = "translate(0px, -2.09032px) rotate(0deg)";

      imgs[5].style.filter = "blur(6px)";
      imgs[5].style.transform = "translate(0px, 0px) rotate(0deg)";
    });
  },

  methods: {
    //请求用户的一些信息
    getUserInfo() {
      //发送http请求获取，这里写死作演示
      this.userInfo = {
        nick: "Doterlin",
        ulevel: 20,
        uid: "10000",
        gold: "2186",
        point: "8864",
        portrait: "../../assets/img/3.png",
      };

      //实例开发中这里会向服务端请求数据
      //如下(用了vue-resource):
      /*ts.$http.get(url, {
        //参数
        "params":{}
      }).then((response) => {
        //Success
      }, (response) => {
        //Error
      });*/

      //提交mutation到Store
      this.$store.commit("updateUserInfo", this.userInfo);
    },
  },
};
</script>

<style lang="scss" scope>
// li {
//   list-style: none;
//   vertical-align: top;
// }
.home-page{
  background-color: #cfcfcf;
  height: 100%;
  width: 100%;
  margin: 0px;
}
// .body{
//   background-color: #a8a5a5;
//   margin: 0;
//   padding: 0;
//   font-family: "Microsoft YaHei", Helvetica;
// }
.container-user {
  padding-top: 160px;
  width: 1700px;
  margin: 0 auto;
  padding-bottom: 20px;
  overflow: hidden;
}
.left {
  display: inline-block;
}
.block {
  display: block;
}
.bold {
  font-weight: bold;
  color: #3c3c3c;
}

.dib {
  display: inline-block;
}
.ml20 {
  margin-left: 20px;
}
.ml19 {
  margin-left: 19px;
}
.ml10 {
  margin-left: 10px;
}
.mt10 {
  margin-top: 10px;
}
.fs12 {
  font-size: 12px;
}
.btn-loading {
  background-color: #a5f0e6 !important;
}

.input {
  width: 278px;
  padding: 0 10px;
  margin: 0 auto;
  margin-top: 25px;
  background: #fff;
  color: #333;
  height: 39px;
  line-height: 39px;
  border-radius: 5px;
  border: 1px solid #e3e3e3;
}
.empty {
  border: 1px solid #f97a7a;
}
.btn-lg {
  display: block;
  width: 300px;
  margin: 0 auto;
  background: #50e3ce;
  color: #fff;
  height: 41px;
  line-height: 41px;
  border-radius: 5px;
  margin-top: 20px;
  text-align: center;
}

.icons {
  background: url(../../assets/img/3.png) no-repeat;
  display: inline-block;
}
.login-fb {
  height: 29px;
  width: 13px;
  background-position: 0 0;
}
.close {
  height: 16px;
  width: 16px;
  background-position: -13px 0;
}
.info {
  height: 18px;
  width: 18px;
  background-position: -29px 0;
}
.info-focus {
  height: 18px;
  width: 18px;
  background-position: -47px 0;
}
.star {
  height: 24px;
  width: 25px;
  background-position: -65px 0;
}
.star-sm {
  height: 18px;
  width: 18px;
  background-position: -48px -1px;
  background-size: 360px 22px;
}
.login-vk {
  height: 15px;
  width: 27px;
  background-position: -90px 0;
}
.login-email {
  height: 17px;
  width: 29px;
  background-position: -117px 0;
}
.login-tw {
  height: 23px;
  width: 29px;
  background-position: -146px 0;
}
.diamond {
  height: 22px;
  width: 29px;
  background-position: -175px 0;
}
.diamond-sm {
  height: 18px;
  width: 21px;
  background-position: -127px 1px;
  background-size: 360px 23px;
}
.process-i2 {
  height: 30px;
  width: 30px;
  background-position: -204px 0;
}
.login-kakao {
  height: 28px;
  width: 31px;
  background-position: -234px 0;
}
.process-i3 {
  height: 31px;
  width: 31px;
  background-position: -265px 0;
}
.process-i1 {
  height: 29px;
  width: 31px;
  background-position: -296px 0;
}
.icon_level_1 {
  height: 15px;
  width: 15px;
  background-position: -333px 3px;
}
.icon_level_2 {
  height: 15px;
  width: 15px;
  background-position: -353px 3px;
}
.icon_level_4 {
  height: 15px;
  width: 15px;
  background-position: -393px 4px;
}
.icon_level_5 {
  height: 15px;
  width: 15px;
  background-position: -411px 3px;
}
.icon_level_3 {
  height: 15px;
  width: 15px;
  background-position: -375px 3px;
}
.icon_level_6 {
  height: 15px;
  width: 15px;
  background-position: -430px 3px;
}
.icon-prev {
  height: 18px;
  width: 9px;
  background-position: -451px 0;
}
.icon-next {
  height: 18px;
  width: 9px;
  background-position: -466px 0;
}

/* transition animate */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
}

.slide-enter-active {
  transition: all 0.3s ease;
}
.slide-leave-active {
  /* transition: all .3s cubic-bezier(1.0, 0.5, 0.8, 1.0); */
}
.slide-enter,
.slide-leave-active {
  transform: translateX(10px);
  opacity: 0;
}

// // 修改导航栏样式
// $header-transition: 0.4s ease;
// .Header {
//   align-items: center;
//   background: rgba(255, 255, 255, 0.459);
//   border-bottom-left-radius: 30px;
//   border-bottom-right-radius: 30px;
// //   display: flex;
//   height: 60px;
//   justify-content: center;
//   position: absolute;
//   text-align: center;
//   top: 0;
//   width: 100%;
//   z-index: 10;

//   &.has-mobile-button {
//     .MobileNav-trigger {
//       display: flex;
//     }
//   }

//   &-inner {
//     display: flex;
//     justify-content: space-between;
//     transition: height $header-transition;
//     width: 80vw;
//   }
// }

// // 景深效果的banner
// .banner {
//   .container {
//     transform: scale(2);
//     transform-origin: 0 0;
//     width: 50%;
//     position: relative;
//     height: 100px;
//     overflow: hidden;
//   }

//   .container .layer {
//     position: absolute;
//     left: 0;
//     top: 0;
//     height: 100%;
//     width: 100%;
//     display: flex;
//     justify-content: center;
//     align-items: center;
//   }
//   /* From Uiverse.io by Praashoo7 */
//   .main {
//     display: flex;
//     align-items: center;
//     justify-content: center;
//   }

//   .loaders,
//   .loadersB {
//     display: flex;
//     align-items: center;
//     justify-content: center;
//   }

//   .loader {
//     position: absolute;
//     width: 1.15em;
//     height: 13em;
//     border-radius: 50px;
//     background: #e0e0e0;
//   }
//   .loader:after {
//     content: "";
//     position: absolute;
//     left: 0;
//     top: 0;
//     width: 1.15em;
//     height: 5em;
//     background: #e0e0e0;
//     border-radius: 50px;
//     border: 1px solid #e2e2e2;
//     box-shadow: inset 5px 5px 15px #d3d2d2ab, inset -5px -5px 15px #e9e9e9ab;
//     mask-image: linear-gradient(
//       to bottom,
//       black calc(100% - 48px),
//       transparent 100%
//     );
//   }
//   .loader::before {
//     content: "";
//     position: absolute;
//     bottom: 0;
//     right: 0;
//     width: 1.15em;
//     height: 4.5em;
//     background: #e0e0e0;
//     border-radius: 50px;
//     border: 1px solid #e2e2e2;
//     box-shadow: inset 5px 5px 15px #d3d2d2ab, inset -5px -5px 15px #e9e9e9ab;
//     mask-image: linear-gradient(
//       to top,
//       black calc(100% - 48px),
//       transparent 100%
//     );
//   }
//   .loaderA {
//     position: absolute;
//     width: 1.15em;
//     height: 13em;
//     border-radius: 50px;
//     background: transparent;
//   }
//   .ball0,
//   .ball1,
//   .ball2,
//   .ball3,
//   .ball4,
//   .ball5,
//   .ball6,
//   .ball7,
//   .ball8,
//   .ball9 {
//     width: 1.15em;
//     height: 1.15em;
//     box-shadow: rgba(0, 0, 0, 0.17) 0px -10px 10px 0px inset,
//       rgba(0, 0, 0, 0.15) 0px -15px 15px 0px inset,
//       rgba(0, 0, 0, 0.1) 0px -40px 20px 0px inset,
//       rgba(0, 0, 0, 0.06) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 4px 2px,
//       rgba(0, 0, 0, 0.09) 0px 8px 4px, rgba(0, 0, 0, 0.09) 0px 16px 8px,
//       rgba(0, 0, 0, 0.09) 0px 32px 16px, 0px -1px 15px -8px rgba(0, 0, 0, 0.09);
//     border-radius: 50%;
//     transition: transform 800ms cubic-bezier(1, -0.4, 0, 1.4);
//     background-color: rgba(232, 232, 232, 1);
//     animation: 3.63s move ease-in-out infinite;
//   }
//   .loader:nth-child(2) {
//     transform: rotate(20deg);
//   }
//   .loader:nth-child(3) {
//     transform: rotate(40deg);
//   }
//   .loader:nth-child(4) {
//     transform: rotate(60deg);
//   }
//   .loader:nth-child(5) {
//     transform: rotate(80deg);
//   }
//   .loader:nth-child(6) {
//     transform: rotate(100deg);
//   }
//   .loader:nth-child(7) {
//     transform: rotate(120deg);
//   }
//   .loader:nth-child(8) {
//     transform: rotate(140deg);
//   }
//   .loader:nth-child(9) {
//     transform: rotate(160deg);
//   }

//   .loaderA:nth-child(2) {
//     transform: rotate(20deg);
//   }
//   .loaderA:nth-child(3) {
//     transform: rotate(40deg);
//   }
//   .loaderA:nth-child(4) {
//     transform: rotate(60deg);
//   }
//   .loaderA:nth-child(5) {
//     transform: rotate(80deg);
//   }
//   .loaderA:nth-child(6) {
//     transform: rotate(100deg);
//   }
//   .loaderA:nth-child(7) {
//     transform: rotate(120deg);
//   }
//   .loaderA:nth-child(8) {
//     transform: rotate(140deg);
//   }
//   .loaderA:nth-child(9) {
//     transform: rotate(160deg);
//   }

//   .ball1 {
//     animation-delay: 0.2s;
//   }
//   .ball2 {
//     animation-delay: 0.4s;
//   }
//   .ball3 {
//     animation-delay: 0.6s;
//   }
//   .ball4 {
//     animation-delay: 0.8s;
//   }
//   .ball5 {
//     animation-delay: 1s;
//   }
//   .ball6 {
//     animation-delay: 1.2s;
//   }
//   .ball7 {
//     animation-delay: 1.4s;
//   }
//   .ball8 {
//     animation-delay: 1.6s;
//   }
//   .ball9 {
//     animation-delay: 1.8s;
//   }

//   @keyframes move {
//     0% {
//       transform: translateY(0em);
//     }
//     50% {
//       transform: translateY(12em);
//     }
//     100% {
//       transform: translateY(0em);
//     }
//   }
// }
</style>
