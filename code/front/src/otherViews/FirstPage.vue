<template>
  <div class="first-pa">
    <!-- Hero -->
    <section class="et-hero-tabs">
      <div class="work-title">
        <h1>中国城市国际传播大数据智能分析平台</h1>
        <h3>Sliding content with sticky tab nav</h3>
      </div>
      <!-- 
        color: String类型。默认'#dedede'。粒子颜色。
        particleOpacity: Number类型。默认0.7。粒子透明度。
        particlesNumber: Number类型。默认80。粒子数量。
        shapeType: String类型。默认'circle'。可用的粒子外观类型有："circle","edge","triangle", "polygon","star"。
        particleSize: Number类型。默认80。单个粒子大小。
        linesColor: String类型。默认'#dedede'。线条颜色。
        linesWidth: Number类型。默认1。线条宽度。
        lineLinked: 布尔类型。默认true。连接线是否可用。
        lineOpacity: Number类型。默认0.4。线条透明度。
        linesDistance: Number类型。默认150。线条距离。
        moveSpeed: Number类型。默认3。粒子运动速度。
        hoverEffect: 布尔类型。默认true。是否有hover特效。
        hoverMode: String类型。默认true。可用的hover模式有: "grab", "repulse", "bubble"。
        clickEffect: 布尔类型。默认true。是否有click特效。
        clickMode: String类型。默认true。可用的click模式有: "push", "remove", "repulse", "bubble"
       -->
      <vue-particles
        id="particles-js"
        color="#39AFFD"
        :particleOpacity="0.7"
        :particlesNumber="100"
        shapeType="circle"
        :particleSize="4"
        linesColor="#8DD1FE"
        :linesWidth="1"
        :lineLinked="true"
        :lineOpacity="0.4"
        :linesDistance="150"
        :moveSpeed="3"
        :hoverEffect="true"
        hoverMode="grab"
        :clickEffect="true"
        clickMode="push"
      >
      </vue-particles>
      <!-- <Header /> -->
      <div class="et-hero-tabs-container">
        <a class="et-hero-tab" href="#tab-es6">首页</a>
        <a class="et-hero-tab" href="#tab-flexbox">城市信息</a>
        <a class="et-hero-tab" href="#tab-react">数据跟踪</a>
        <a class="et-hero-tab" href="#tab-angular">数据对比</a>
        <a class="et-hero-tab" href="#tab-other">城市频道</a>
        <a class="et-hero-tab" href="#tab-magic">联想空间</a>
        <span class="et-hero-tab-slider"></span>
      </div>
    </section>

    <!-- Main -->
    <main class="et-main">
      <section class="et-slide" id="tab-es6">
        <h1>首页</h1>
        <h3>something about es6</h3>
      </section>
      <section class="et-slide" id="tab-flexbox">
        <router-link :to="{ name: '城市信息' }"><h1>城市信息</h1></router-link>
        <h3>something about flexbox</h3>
      </section>
      <section class="et-slide" id="tab-react">
        <router-link :to="{ name: '数据跟踪' }"><h1>数据跟踪</h1></router-link>
        <h3>something about react</h3>
      </section>
      <section class="et-slide" id="tab-angular">
        <router-link :to="{ name: '数据对比' }"><h1>城市对比</h1></router-link>
        <h3>something about angular</h3>
      </section>
      <section class="et-slide" id="tab-other">
        <router-link :to="{ name: '城市频道' }"><h1>城市频道</h1></router-link>
        <h3>something about other</h3>
      </section>
      <section class="et-slide" id="tab-magic">
        <router-link :to="{ name: '联想空间' }"><h1>联想空间</h1></router-link>
        <h3>something about other</h3>
      </section>
      <Footer />
    </main>
  </div>
</template>

<script>
// import TweenMax from "gsap";
import Footer from "../components/Layout/Footer.vue";
export default {
  components: {
    Footer,
  },
  data() {
    return {
      currentId: null,
      currentTab: null,
      tabContainerHeight: 70,
    };
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
          .querySelector(".et-hero-tabs-container")
          .classList.add("et-hero-tabs-container--top");
      } else {
        document
          .querySelector(".et-hero-tabs-container")
          .classList.remove("et-hero-tabs-container--top");
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
        console.log("newCurrentId", newCurrentId);
        console.log("newCurrentTab", newCurrentTab);
        console.log("newCurrentTab", typeof newCurrentTab);
        console.log("newCurrentTab", typeof newCurrentId);

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
.work-title {
  position: relative;
}
#particles-js {
  width: 100%;
  height: 100%;
  position: absolute;
}
body {
  font-family: "Century Gothic", "Lato", sans-serif;
}

a {
  text-decoration: none;
}

.et-hero-tabs,
.et-slide {
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

.et-hero-tabs-container {
  display: flex;
  flex-direction: row;
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 70px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  background: #fff;
  z-index: 10;
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
  .et-slide {
    h1 {
      font-size: 3rem;
    }
    h3 {
      font-size: 1rem;
    }
  }
  .et-hero-tab {
    font-size: 1rem;
  }
}
</style>
