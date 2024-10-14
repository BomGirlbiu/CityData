<template>
  <div class="detail-data">
    <div class="floating-div">
      <SelectCity @citydata="handleCityFromChild"></SelectCity>
    </div>
    <aside class="sidebar">
      <ul>
        <li>
          <h3>{{ selectedCity }}市数据分析</h3>
        </li>
        <li
          v-for="(bookmark, index) in bookmarks"
          :key="index"
          :class="{ active: isActive(bookmark.id) }"
        >
          <a :href="`#${bookmark.id}`" @click.prevent="scrollTo(bookmark.id)">{{
            bookmark.title
          }}</a>
        </li>
        <li>
          <el-button type="primary"
            >生成城市报告<i class="el-icon-upload el-icon--right"></i
          ></el-button>
        </li>
        <li>
          <el-button id="floating-button" @click="goToAnotherPage"
            >切换可视化大屏</el-button
          >
        </li>
      </ul>
    </aside>
    <img
      src="../../assets/image/返回.png"
      alt="返回"
      class="back-button"
      @click="goBackToHome"
    />
    <main class="content">
      <section id="section1" class="section">
        <div style="height: 320px; width: 38%">
          <Conclusion :selectedCity="selectedCity"></Conclusion>
        </div>
        <div style="height: 320px; flex: 0"></div>
        <!-- 这里的flex为0表示左对齐，右对齐则为flex:1 -->
        <FiveInfluence></FiveInfluence>
      </section>
      <section id="section2" class="section">
        <div style="height: 480px; width: 50%">
          <SearchEngine :selectedCity="selectedCity"></SearchEngine>
        </div>
      </section>
      <section id="section3" class="section">
        <div style="height: 480px; width: 50%">
          <NationTourism :selectedCity="selectedCity"></NationTourism>
        </div>
      </section>
      <section id="section4" class="section">
        <div style="height: 480px; width: 50%">
          <NetworkTrans :selectedCity="selectedCity"></NetworkTrans>
        </div>
      </section>
      <section id="section5" class="section">
        <div style="height: 480px; width: 50%">
          <SocialMedia :selectedCity="selectedCity"></SocialMedia>
        </div>
      </section>
      <section id="section6" class="section">
        <div style="height: 480px; width: 50%">
          <MediaReport :selectedCity="selectedCity"></MediaReport>
        </div>
      </section>
    </main>
  </div>
</template>
<script>
import MediaReport from "./MediaReport.vue";
import SocialMedia from "./SocialMedia.vue";
import NetworkTrans from "./NetworkTrans.vue";
import SearchEngine from "./SearchEngine.vue";
import NationTourism from "./NationTourism.vue";
import Conclusion from "./Conclusion.vue";
import FiveInfluence from "./FiveInfluence.vue";
import SelectCity from "./SelectCity.vue";

export default {
  components: {
    Conclusion,
    MediaReport,
    NationTourism,
    SearchEngine,
    SocialMedia,
    NetworkTrans,
    FiveInfluence,
    SelectCity,
  },
  data() {
    return {
      selectedCity: "北京",
      bookmarks: [
        { title: "城市传播指数", id: "section1" },
        { title: "搜索引擎影响力", id: "section1" },
        { title: "国际访客影响力", id: "section2" },
        { title: "网络传播影响力", id: "section3" },
        { title: "社交媒体影响力", id: "section4" },
        { title: "媒体报道影响力", id: "section5" },
        // 更多书签
      ],
      activeBookmark: null,
    };
  },
  created() {
    if (this.selectedCity == "北京" && this.$route.query.cityname) {
      this.selectedCity = this.$route.query.cityname;
    }
  },
  methods: {
    handleCityFromChild(data) {
      if (data.slice(-2, -1) == "城" || data.slice(-2, -1) == "郊") {
        this.selectedCity = data.slice(0, -2);
      } else {
        this.selectedCity = data.slice(0, -1);
      }
      // 处理从子组件接收到的数据
      // 如果需要，也可以将数据进一步传递给其他组件或执行其他操作
    },
    goBackToHome() {
      this.$router.push({ name: "首页" });
    },
    goToAnotherPage() {
      this.$router.push({
        name: "可视化大屏",
        query: { cityname: this.selectedCity },
      });
    },
    isActive(id) {
      return this.activeBookmark === id;
    },
    scrollTo(id) {
      const element = document.getElementById(id);
      if (element) {
        element.scrollIntoView({ behavior: "smooth" });
        this.activeBookmark = id;
      }
    },
    onScroll() {
      const sections = document.querySelectorAll(".section");
      let activeId = null;
      sections.forEach((section) => {
        const rect = section.getBoundingClientRect();
        if (
          rect.top >= 0 &&
          rect.bottom <=
            (window.innerHeight || document.documentElement.clientHeight)
        ) {
          activeId = section.id;
        }
      });
      this.activeBookmark = activeId;
    },
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.onScroll);
  },
};
</script>
<style scoped>
.floating-div {
  position: fixed;
  top: 0; /* 固定在屏幕顶部 */
  left: 35%; /* 可以根据需要调整水平位置，比如设置为 '50%' 并配合 transform: translateX(-50%) 来居中 */
  width: 100%; /* 或者设置为具体的宽度 */
  color: #fff; /* 白色文字 */
  text-align: center; /* 文字居中 */
  padding: 10px 0; /* 内边距 */
  z-index: 9999; /* 确保它悬浮在其他内容之上 */
}
.back-button {
  height: 60px;
  position: fixed;
  top: -5px; /* Adjust as needed */
  left: 10px; /* Adjust as needed */
  z-index: 1000; /* Ensure it's above other content */
  padding: 10px 20px;
  cursor: pointer;
  font-size: 16px;
}

#floating-button {
  position: fixed; /* 固定定位 */
  bottom: 20px; /* 距离页面底部20px */
  left: 20px; /* 距离页面左侧20px */
  width: 110px; /* 按钮宽度 */
  height: 50px; /* 按钮高度 */
  background-color: #66b2ff; /*按钮背景颜色 */
  color: white; /* 按钮文字颜色 */
  border: none; /* 无边框 */
  border-radius: 10px; /* 圆角 */
  cursor: pointer; /* 鼠标悬停时显示为手指 */
  font-size: 14px; /* 文字大小 */
  display: flex; /* 使用Flexbox布局 */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 添加阴影 */
  transition: background-color 0.3s ease; /* 背景颜色过渡效果 */
}

#floating-button:hover {
  background-color: #2a5288; /* 鼠标悬停时背景颜色变化 */
}
.detail-data {
  display: flex;
  height: 100vh;
  overflow: hidden;
  background-color: #1e3c72; /* 深蓝色背景 */
  color: #ffffff; /* 白色文字 */
  font-family: "Arial", sans-serif; /* 简洁的字体 */
}

.sidebar {
  border-top-left-radius: 50px; /* 左上角 */
  border-top-right-radius: 50px; /* 右上角 */
  border-bottom-right-radius: 50px; /* 右下角 */
  border-bottom-left-radius: 50px;
  width: 250px;
  padding: 20px;
  margin-top: 50px;
  background-color: #254e88; /* 稍浅的蓝色背景 */
  border-right: none;
  box-shadow: 5px 0px 15px rgba(0, 0, 0, 0.2);
}

.sidebar ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.sidebar li {
  margin: 15px 0;
  position: relative;
  align-items: center;
  text-align: center;
}

.sidebar li::before {
  content: "";
  position: absolute;
  left: -15px;
  top: 50%;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border-top: 7px solid transparent;
  border-bottom: 7px solid transparent;
  border-right: 7px solid #66b2ff; /* 蓝色箭头 */
  opacity: 0;
  transition: opacity 0.3s;
}

.sidebar li.active::before,
.sidebar li a:hover::before {
  opacity: 1;
}

.sidebar li.active a,
.sidebar li a:hover {
  color: #d3d3d3; /* 鼠标悬停或激活时文字变为灰色加深效果 */
  text-decoration: none;
  font-weight: bold;
}

.sidebar a {
  display: block;
  padding: 5px 10px;
  color: #ffffff; /* 白色文字 */
  transition: color 0.3s;
}

.content {
  margin-top: 30px;
  flex-grow: 1;
  padding: 20px;
  overflow-y: auto;
}

.section {
  display: flex; /* 设置为 flex 容器 */
  border-radius: 30px;
  margin-bottom: 40px;
  padding: 20px;
  background-color: #2a5288; /* 浅于背景色的部分背景 */
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.section > div {
  /* 确保所有的直接子 div 都遵循 flex 布局规则 */
  box-sizing: border-box; /* 确保 padding 和 border 不会增加元素的总宽度 */
}

.section h2 {
  color: #ffffff; /* 白色标题 */
}
.imgNodata {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); /* 水平和垂直居中 */
  max-width: 100%;
  height: auto;
}

/* 可选：添加滚动条样式（仅适用于webkit浏览器） */
/* ::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-thumb {
  background-color: #66b2ff;
  border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
  background-color: #88c5ff;
} */
</style>
