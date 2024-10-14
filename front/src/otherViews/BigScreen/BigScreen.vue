<template>
  <div class="dashboard">
    <img
      src="../../assets/image/返回2.png"
      alt="返回"
      class="back-button"
      @click="goBackToHome"
    />
    <header>
      <h1>{{ this.selectedCity }}数据可视化大屏</h1>
    </header>
    <div class="content">
      <div class="part">
        <Conclusion :selectedCity="selectedCity"></Conclusion>
      </div>
      <div class="part">
        <SearchEngine :selectedCity="selectedCity"></SearchEngine>
      </div>
      <div class="part">
        <NationTourism :selectedCity="selectedCity"></NationTourism>
      </div>
      <div class="part">
        <NetworkTrans :selectedCity="selectedCity"></NetworkTrans>
      </div>
      <div class="part">
        <SocialMedia :selectedCity="selectedCity"></SocialMedia>
      </div>
      <div class="part">
        <MediaReport :selectedCity="selectedCity"></MediaReport>
      </div>
      <el-button id="floating-button" @click="anotherPage"
        >查看数据分析</el-button
      >
    </div>
  </div>
</template>

<script>
import Conclusion from "../DetailData/Conclusion.vue";
import MediaReport from "../DetailData/MediaReport.vue";
import NationTourism from "../DetailData/NationTourism.vue";
import NetworkTrans from "../DetailData/NetworkTrans.vue";
import SocialMedia from "../DetailData/SocialMedia.vue";
import SearchEngine from "../DetailData/SearchEngine.vue";

export default {
  components: {
    Conclusion,
    MediaReport,
    SocialMedia,
    SearchEngine,
    NetworkTrans,
    NationTourism,
  },
  data() {
    return {
      selectedCity: "北京",
    };
  },
  created() {
    this.selectedCity = this.$route.query.cityname;
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
    anotherPage() {
      this.$router.push({
        name: "数据跟踪",
        query: { cityname: this.selectedCity },
      });
    },
  },
};
</script>

<style scoped>
/* body,
html {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow-x: hidden; 
} */
.back-button {
  height: 60px;
  position: fixed;
  top: 0px; /* Adjust as needed */
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

.dashboard {
  font-family: Arial, sans-serif;
  background-color: #0e1a35; /* 深蓝色背景 */
  color: #ffffff; /* 白色文字 */
  padding: 10px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  height: 100vh; /* 使dashboard占据整个视口高度 */
}

header {
  text-align: center;
  margin-bottom: 20px;
  font-size: 20px;
}

.content {
  margin-bottom: 10px;
  display: flex;
  flex-wrap: wrap;
  gap: 6px; /* 各个部分之间的间距 */
  justify-content: center;
}

.part {
  height: 330px;
  flex: 1 1 calc(30% - 6px); /* 默认三列布局，每列宽度为30%减去间距 */
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.1); /* 轻微透明背景 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  text-align: center;
}
</style>
