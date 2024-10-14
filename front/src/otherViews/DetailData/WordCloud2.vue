<template>
  <div ref="chartDom" class="echarts" style="width: 100%; height: 100%"></div>
</template>

<script>
import * as echarts from "echarts"; // echarts5版本 引入
import "echarts-wordcloud";

export default {
  name: "WordCloud2",
  props: {
    selectedCity: String,
    words: {
      type: Array,
      required: true, // 确保 words 是一个必需的 prop
    },
  },
  data() {
    return {
      chart: null,
      processedData: [], // 用于存储处理后的数据
    };
  },
  watch: {
    words() {
      if (this.words.length != 0) {
        this.processData();
        this.initChart();
      }
    },
  },
  mounted() {
    // 组件挂载后初始化图表
    this.initChart();
    // 监听 selectedCity 的变化
    this.$watch("selectedCity", this.updateChart);
  },
  methods: {
    processData() {
      // 处理数据
      this.processedData = this.words.map((word) => ({
        name: word.name,
        value: word.value * 30,
      }));
    },
    initChart() {
      // 初始化图表
      this.chart = echarts.init(this.$refs.chartDom);
      this.updateChart();
    },
    updateChart() {
      // 词云图的配置项
      const option = {
        tooltip: {
          show: true,
        },
        series: [
          {
            name: "词云图",
            type: "wordCloud",
            sizeRange: [20, 50], // 文字范围
            rotationRange: [-45, 90],
            rotationStep: 45,
            textRotation: [0, 45, 90, -45],
            shape: "circle",
            textStyle: {
              color: function () {
                // 文字颜色的随机色
                return (
                  "rgb(" +
                  [
                    Math.round(Math.random() * 250),
                    Math.round(Math.random() * 250),
                    Math.round(Math.random() * 250),
                  ].join(",") +
                  ")"
                );
              },
              emphasis: {
                shadowBlur: 10,
                shadowColor: "#333",
              },
            },
            data: this.processedData,
          },
        ],
      };

      // 更新图表配置
      if (this.chart) {
        this.chart.setOption(option);
      }
    },
  },
  beforeDestroy() {
    // 组件销毁前销毁图表实例
    if (this.chart) {
      this.chart.dispose();
    }
  },
};
</script>
