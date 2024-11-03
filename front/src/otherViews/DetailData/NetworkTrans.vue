<template>
  <div class="networktrans">
    <div class="select-city">
      网络传播影响力
      <select v-model="selected" class="selectcity">
        <option disabled value="">请选择二级影响因子...</option>
        <option v-for="item in influences" :key="item">{{ item }}</option>
      </select>
    </div>
    <div ref="chartDom" class="echarts" style="width: 100%; height: 100%">
      <img
        class="imgNodata"
        v-show="words == null || words.length == 0"
        src="../../assets/image/暂无数据.png"
      />
      <WordCloud2
        :selectedCity="selectedCity"
        :words="words"
        v-show="selected == '国际热度词条词云图'"
      />
      <div
        v-show="selected != '国际热度词条词云图'"
        ref="chartDom"
        class="echarts"
        style="width: 100%; height: 100%"
      ></div>
    </div>
  </div>
</template>
<!-- <script src="../node_modules/echarts/lib/chart/wordCloud/echart3.js"></script>
<script src="../node_modules/echarts/lib/chart/wordCloud/echarts-wordcloud.js"></script> -->
<script>
import axios from "axios";
import "echarts-wordcloud";
// import echartsWordCloud from "./utils/echarts-wordcloud.js";
import WordCloud2 from "./WordCloud2.vue";
// import wordcloud3D from "./wordcloud3D.vue";
export default {
  name: "NetworkTrans",
  components: {
    WordCloud2,
    // wordcloud3D,
  },
  data() {
    return {
      selected: "",
      words: [],
      chart: null,
      influences: ["国际热度词条词云图", "随便写的"],
    };
  },
  props: {
    selectedCity: String, // 声明selectedCity为String类型的prop
  },

  watch: {
    selectedCity: function (newVal, oldVal) {
      this.chart = null;
      if (this.selected == "国际热度词条词云图") {
        this.drawWordCloud(newVal);
      }
      console.log("selectedCity changed:", newVal);
    },
    selected: function (newVal, oldVal) {
      this.chart = null;
      if (newVal == "国际热度词条词云图") {
        this.drawWordCloud(this.selectedCity);
      }
      console.log("selected changed:", newVal);
    },
  },
  created() {
    this.selected = "国际热度词条词云图";
  },
  methods: {
    async drawWordCloud(cityname) {
      let params = new FormData();
      params.append("cityname", cityname);
      //   console.log("params:", params);
      try {
        const response = await axios({
          url: "http://localhost:82/index/visual/network/cloud",
          method: "post",
          data: params,
        }); // 处理响应数据
        this.words = response.data;
        // InitChart(response.data);
      } catch (error) {
        console.error("Error:", error);
      }
    },
  },

  beforeDestroy() {
    if (this.chart) {
      this.chart.dispose();
    }
  },
};
</script>
<style>
.networktrans {
  height: 95%;
  width: 100%;
  /* border: 1px solid white; */
}

.selectcity {
  /* 下拉框的样式 */
  width: 30%; /* 宽度可以根据需要调整 */
  padding: 8px; /* 添加一些内边距以提高可读性 */
  border: 1px solid #ccc; /* 边框样式 */
  border-radius: 4px; /* 边框圆角 */
}
</style>
