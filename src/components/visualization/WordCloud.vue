<template>
  <div class="charts-box">
    <qiun-vue-ucharts type="word" :opts="opts" :chartData="chartData" />
  </div>
</template>

<script>
// 需要在您的项目内执行 npm i @qiun/vue-ucharts
import qiunVueUcharts from "@qiun/vue-ucharts";
// import "../../../node_modules/echarts/lib/chart/wordCloud/echarts3.js";
// import "../../../node_modules/echarts/lib/chart/wordCloud/echarts-wordcloud.js";

export default {
  name: "WordCloud",
  props: {
    words: Array,
    selectedCity: String, // 声明selectedCity为String类型的prop
  },
  components: {
    qiunVueUcharts,
  },
  data() {
    return {
      new: [],
      datas: [],
      chartData: {},
      //您可以通过修改 config-ucharts.js 文件中下标为 ['word'] 的节点来配置全局默认参数，如都是默认参数，此处可以不传 opts 。实际应用过程中 opts 只需传入与全局默认参数中不一致的【某一个属性】即可实现同类型的图表显示不同的样式，达到页面简洁的需求。
      opts: {
        color: [
          "#1890FF",
          "#91CB74",
          "#FAC858",
          "#EE6666",
          "#73C0DE",
          "#3CA272",
          "#FC8452",
          "#9A60B4",
          "#ea7ccc",
        ],
        padding: undefined,
        enableScroll: true,
        extra: {
          word: {
            type: "vertical",
            autoColors: false,
          },
        },
      },
    };
  },
  created() {
    this.getServerData(this.words);
  },
  watch: {
    words: function (newVal, oldVal) {
      this.getServerData(newVal);
      console.log("words changed:", newVal);
    },
  },
  methods: {
    getServerData(words) {
      this.datas = words[0].name;
      var data = [];
      for (var i = 0; i < words.length; i++) {
        data[i] = new Object();
        data[i].name = words[i].name;
        data[i].textSize = words[i].value * 12;
        data[i].data = "undefined";
      }
      this.new = data;
      //模拟服务器返回数据，如果数据格式和标准格式不同，需自行按下面的格式拼接
      let res = {
        series: this.new,
      };
      this.chartData = JSON.parse(JSON.stringify(res));
    },
  },
};
</script>

<style scoped>
/* 请根据实际需求修改父元素尺寸，组件自动识别宽高 */
.charts-box {
  width: 450px;
  height: 280px;
}
</style>
