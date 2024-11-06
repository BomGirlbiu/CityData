<template>
  <div class="et-hero-tabs-container1">
    <router-link class="et-hero-tab" :to="{ name: '首页' }">首页</router-link>
    <router-link class="et-hero-tab" :to="{ name: '城市信息' }"
      >城市信息</router-link
    >
    <router-link class="et-hero-tab" :to="{ name: '数据跟踪' }"
      >数据跟踪</router-link
    >
    <router-link class="et-hero-tab" :to="{ name: '首页' }"
      >城市对比</router-link
    >
    <router-link class="et-hero-tab" :to="{ name: '城市频道' }"
      >城市频道</router-link
    >
    <router-link class="et-hero-tab" :to="{ name: '首页' }"
      >联想空间</router-link
    >

    <!-- <a class="et-hero-tab" href="#tab-es6">首页</a> -->
    <!-- <a class="et-hero-tab" href="#tab-flexbox">城市信息</a>
        <a class="et-hero-tab" href="#tab-react">城市分析</a>
        <a class="et-hero-tab" href="#tab-angular">数据对比</a>
        <a class="et-hero-tab" href="#tab-other">城市频道</a>
        <a class="et-hero-tab" href="#tab-magic">联想空间</a> -->
    <span class="et-hero-tab-slider"></span>
  </div>
</template>

<script>
// import TweenMax from "gsap";
export default {
  // props: {
  //   CurrentModule:{
  //     type:Object,
  //     default:() => ({})
  //   },
  //   CurrentID:{
  //     type:String,
  //     default:""
  //   }
  // },
  data() {
    return {
      currentId: null,
      currentTab: null,
      tabContainerHeight: 70,
    };
  },
  created() {
    this.newCurrentId = this.CurrentID;
    this.newCurrentTab = this.CurrentModule;
    console.log("CurrentID", this.CurrentID);
    console.log("CurrentModule", this.CurrentModule);
  },
  mounted() {
    this.initStickyNavigation();
    window.addEventListener("scroll", this.onScroll);
    window.addEventListener("resize", this.onResize);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.onScroll);
    window.removeEventListener("resize", this.onResize);
  },
  methods: {
    initStickyNavigation() {
      this.$nextTick(() => {
        document.querySelectorAll(".et-hero-tab").forEach((tab) => {
          tab.addEventListener("click", (event) => {
            event.preventDefault();
            const scrollTop =
              document.querySelector(event.target.getAttribute("href"))
                .offsetTop -
              this.tabContainerHeight +
              1;
            window.scrollTo({
              top: scrollTop,
              behavior: "smooth",
            });
          });
        });
      });
    },
    onTabClick(event, element) {
      event.preventDefault();
      const scrollTop =
        document.querySelector(element.getAttribute("href")).offsetTop -
        this.tabContainerHeight +
        1;
      window.scrollTo({
        top: scrollTop,
        behavior: "smooth",
      });
    },
    onScroll() {
      this.checkTabContainerPosition();
      this.findCurrentTabSelector();
    },
    onResize() {
      if (this.currentId) {
        this.setSliderCss();
      }
    },
    checkTabContainerPosition() {
      const offset =
        document.querySelector(".et-hero-tabs").offsetTop +
        document.querySelector(".et-hero-tabs").offsetHeight -
        this.tabContainerHeight;
      if (window.pageYOffset > offset) {
        document
          .querySelector(".et-hero-tabs-container1")
          .classList.add("et-hero-tabs-container1--top");
      } else {
        document
          .querySelector(".et-hero-tabs-container1")
          .classList.remove("et-hero-tabs-container1--top");
      }
    },
    findCurrentTabSelector() {
      let newCurrentId = null;
      let newCurrentTab = null;
      document.querySelectorAll(".et-hero-tab").forEach((tab) => {
        const id = tab.getAttribute("href");
        const offsetTop =
          document.querySelector(id).offsetTop - this.tabContainerHeight;
        const offsetBottom =
          document.querySelector(id).offsetTop +
          document.querySelector(id).offsetHeight -
          this.tabContainerHeight;
        if (
          window.pageYOffset > offsetTop &&
          window.pageYOffset < offsetBottom
        ) {
          newCurrentId = id;
          newCurrentTab = tab;
        }
      });
      if (this.currentId !== newCurrentId || this.currentId === null) {
        this.currentId = newCurrentId;
        this.currentTab = newCurrentTab;
        this.setSliderCss();
      }
    },
    setSliderCss() {
      if (this.currentTab) {
        const width = this.currentTab.offsetWidth;
        const left = this.currentTab.offsetLeft;
        document.querySelector(
          ".et-hero-tab-slider"
        ).style.width = `${width}px`;
        document.querySelector(".et-hero-tab-slider").style.left = `${left}px`;
      }
    },
  },
};
</script>

<style lang="scss" scope>
.et-hero-tabs {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  position: relative;
  background: #eee;
  text-align: center;
  padding: 0 2em;
  h1 {
    font-size: 2rem;
    margin: 0;
    letter-spacing: 1rem;
  }
  h3 {
    font-size: 1rem;
    letter-spacing: 0.3rem;
    opacity: 0.6;
  }
}
.et-hero-tabs-container1 {
  display: flex;
  flex-direction: row;
  position: fixed;
  top: 0;
  width: 100%;
  height: 70px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  background: #fff;
  z-index: 100;
  &--top {
    position: fixed;
    top: 0;
  }
}
.et-hero-tab {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1;
  color: #000;
  letter-spacing: 0.1rem;
  transition: all 0.5s ease;
  font-size: 0.8rem;
  &:hover {
    color: white;
    background: rgba(102, 177, 241, 0.8);
    transition: all 0.5s ease;
  }
}

.et-hero-tab-slider {
  position: absolute;
  bottom: 0;
  width: 0;
  height: 6px;
  background: #66b1f1;
  transition: left 0.3s ease;
}

@media (min-width: 800px) {
  .et-hero-tabs,
  .et-hero-tab {
    font-size: 1rem;
  }
}
</style>