<template>
  <div class="charts-box">
    <qiun-vue-ucharts type="radar" :opts="opts" :chartData="chartData" />
  </div>
</template>

<script>
// 需要在您的项目内执行 npm i @qiun/vue-ucharts
import qiunVueUcharts from "@qiun/vue-ucharts";

export default {
  name: "Rador",
  props: {
    fivedatas: Array,
    selectedCity: String,
  },
  components: {
    qiunVueUcharts,
  },
  data() {
    return {
      chartData: {},
      //您可以通过修改 config-ucharts.js 文件中下标为 ['radar'] 的节点来配置全局默认参数，如都是默认参数，此处可以不传 opts 。实际应用过程中 opts 只需传入与全局默认参数中不一致的【某一个属性】即可实现同类型的图表显示不同的样式，达到页面简洁的需求。
      opts: {
        color: [
          "#FAC858",
          "#EE6666",
          "#73C0DE",
          "#3CA272",
          "#FC8452",
          "#9A60B4",
          "#ea7ccc",
        ],
        padding: [5, 5, 5, 5],
        dataLabel: false,
        dataPointShape: false,
        enableScroll: false,
        legend: {
          show: true,
          position: "center",
          lineHeight: 25,
        },
        extra: {
          radar: {
            gridType: "circle",
            gridColor: "#fff",
            gridCount: 3,
            opacity: 0.2,
            max: 200,
            labelShow: true,
            axisLabel: true,
            gridEval: 2,
            border: true,
          },
        },
      },
    };
  },
  mounted() {
    this.getServerData();
  },
  methods: {
    getServerData() {
      //模拟服务器返回数据，如果数据格式和标准格式不同，需自行按下面的格式拼接
      let res = {
        categories: [
          "网络传播影响力",
          "媒体报道影响力",
          "社交媒体影响力",
          "国际访客影响力",
          "搜索引擎影响力",
        ],
        series: [
          {
            name: this.selectedCity,
            data: [
              this.fivedatas[0].network,
              this.fivedatas[0].mediatr,
              this.fivedatas[0].social,
              this.fivedatas[0].tourism,
              this.fivedatas[0].searchin,
            ],
          },
        ],
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
  height: 340px;
}
</style>
