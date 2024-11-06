<template>
  <div class="networktrans">
    <div class="select-city">
      网络传播影响力
      <select v-model="selected" class="selectcity">
        <option disabled value="">请选择二级影响因子...</option>
        <option v-for="item in influences" :key="item">{{ item }}</option>
      </select>
    </div>
    <div
      v-if="isShowExplain"
      ref="chartDom"
      class="echarts"
      style="width: 50%; height: 100%"
    >
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
        style="width: 50%; height: 100%"
      ></div>
    </div>
    <div
      v-else
      ref="chartDom"
      class="echarts"
      style="width: 100%; height: 100%"
    >
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
        style="width: 50%; height: 100%"
      ></div>
    </div>
    <div v-if="isShowExplain" class="explain_detail">
      <ZhiPu :analyzedata="analyzedata" :Question="Question"></ZhiPu>
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
import ZhiPu from "./ZhiPu.vue";
// import wordcloud3D from "./wordcloud3D.vue";
export default {
  name: "NetworkTrans",
  components: {
    WordCloud2,
    ZhiPu,
    // wordcloud3D,
  },
  data() {
    return {
      selected: "",
      words: [],
      chart: null,
      influences: ["国际热度词条词云图", "其他影响因素"],
      analyzedata: null,
      Question:
        "以下数据格式为{城市名，关键词，出现次数}，该数据为提及城市在网络上出现的热度，分析为什么这些词是热度较高的词，不用提及到具体次数，回答在400字以内",
    };
  },
  props: {
    selectedCity: String, // 声明selectedCity为String类型的prop
    isShowExplain: Boolean,
  },

  watch: {
    selectedCity: function (newVal, oldVal) {
      this.chart = null;
      if (this.selected == "国际热度词条词云图") {
        this.drawWordCloud(newVal);
        this.Question =
          "以下数据格式为{城市名，关键词，出现次数}，该数据为提及城市在网络上出现的热度，挑选次数较高的关键词，分析为什么这些词是热度较高的词，不用提及到具体次数，答案在500字以内";
      }
      // console.log("selectedCity changed:", newVal);
    },
    selected: function (newVal, oldVal) {
      this.chart = null;
      if (newVal == "国际热度词条词云图") {
        this.drawWordCloud(this.selectedCity);
        this.Question =
          "以下数据格式为{城市名，关键词，出现次数}，该数据为提及城市在网络上出现的热度，挑选次数较高的关键词，分析为什么这些词是热度较高的词，不用提及到具体次数，答案在500字以内";
      }
      // console.log("selected changed:", newVal);
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
        // console.log(response.data);
        this.analyzedata = response.data;
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
  position: relative;
  /* border: 1px solid white; */
}

.selectcity {
  /* 下拉框的样式 */
  width: 30%; /* 宽度可以根据需要调整 */
  padding: 8px; /* 添加一些内边距以提高可读性 */
  border: 1px solid #ccc; /* 边框样式 */
  border-radius: 4px; /* 边框圆角 */
}
.explain_detail {
  position: absolute; /* 设置为绝对定位 */
  top: 0; /* 顶部与父元素对齐 */
  right: 0%; /* 右侧距离父元素右侧0% */
  width: 50%; /* 子元素的宽度 */
  height: 100%; /* 子元素的高度 */
}
</style>
