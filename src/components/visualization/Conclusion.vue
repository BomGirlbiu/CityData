<template>
  <div class="conclusion">
    <div
      ref="chartDom"
      class="echarts"
      style="width: 450px; height: 305px"
    ></div>
  </div>
</template>
<script>
import axios from "axios";
import echarts from "echarts";
export default {
  name: "Conclusion",
  data() {
    return {
      chart: null,
    };
  },
  props: {
    selectedCity: String, // 声明selectedCity为String类型的prop
  },

  watch: {
    selectedCity: function (newVal, oldVal) {
      this.tourism(newVal);
      console.log("selectedCity changed:", newVal);
    },
  },
  created() {
    this.tourism(this.selectedCity);
  },
  methods: {
    async tourism(cityname) {
      let params = new FormData();
      params.append("cityname", cityname);
      //   console.log("params:", params);
      try {
        const response = await axios({
          url: "http://localhost:8081/index/visual/conclusion",
          method: "post",
          data: params,
        });
        console.log(response.data + "这里是五项数据"); // 处理响应数据
        this.initChart(response.data);
      } catch (error) {
        console.error("Error:", error);
      }
    },
    initChart(datas) {
      if (datas != null) {
        var rate = [];
        rate[0] = datas[0].network;
        rate[1] = datas[0].mediatr;
        rate[2] = datas[0].social;
        rate[3] = datas[0].tourism;
        rate[4] = datas[0].searchin;
        this.chart = echarts.init(this.$refs.chartDom);
        const option = {
          color: ["#67F9D8", "#FFE434", "#56A3F1", "#FF917C"],
          legend: {
            textStyle: {
              fontSize: 18, //字体大小
              color: "#000", //字体颜色
            },
          },
          radar: [
            {
              indicator: [
                { text: "网络传播影响力" },
                { text: "媒体报道影响力" },
                { text: "社交媒体影响力" },
                { text: "国际访客影响力" },
                { text: "搜索引擎影响力" },
              ],
              center: ["50%", "50%"],
              radius: 100,
              startAngle: 90,
              splitNumber: 4,
              shape: "circle",
              axisName: {
                formatter: "【{value}】",
                color: "#ffffff",
              },
              splitArea: {
                areaStyle: {
                  color: ["#77EADF", "#26C3BE", "#64AFE9", "#428BD4"],
                  shadowColor: "rgba(0, 0, 0, 0.2)",
                  shadowBlur: 10,
                },
              },
            },
          ],
          series: [
            {
              type: "radar",
              emphasis: {
                lineStyle: {
                  width: 4,
                },
              },
              data: [
                {
                  value: rate,
                  name: "指数大小",
                  areaStyle: {
                    color: "rgba(255, 228, 52, 0.6)",
                  },
                },
              ],
            },
          ],
        };
        this.chart.setOption(option);
      } else {
        console.log("数据为空");
      }
    },
  },
};
</script>
<style>
.conclusion {
  border: 1px solid white;
}
.select-city {
  /* 为下拉框容器设置样式（如果需要的话） */
}

.selectcity {
  /* 下拉框的样式 */
  width: 30%; /* 宽度可以根据需要调整 */
  padding: 8px; /* 添加一些内边距以提高可读性 */
  border: 1px solid #ccc; /* 边框样式 */
  border-radius: 4px; /* 边框圆角 */
}
</style>
