<template>
  <div class="mediareport">
    <div class="select-city">
      媒体报道影响力
      <select v-model="selected" class="selectcity">
        <option disabled value="">请选择二级影响因子...</option>
        <option v-for="item in influences" :key="item">{{ item }}</option>
      </select>
    </div>
    <div
      ref="chartDom"
      class="echarts"
      style="width: 500px; height: 305px"
    ></div>
  </div>
</template>
<script>
import axios from "axios";
import echarts from "echarts";
export default {
  name: "MediaReport",
  props: {
    selectedCity: String, // 声明selectedCity为String类型的prop
  },
  data() {
    return {
      selected: "",
      chart: null,
      influences: ["纽约时报报道次数"],
    };
  },
  watch: {
    selectedCity: function (newVal, oldVal) {
      if (this.selected == "纽约时报报道次数") {
        this.newyork(newVal);
      }
      console.log("selectedCity changed:", newVal);
    },
    selected: function (newVal, oldVal) {
      if (newVal == "纽约时报报道次数") {
        this.newyork(this.selectedCity);
      }
      console.log("selected changed:", newVal);
    },
  },
  methods: {
    async newyork(cityname) {
      let params = new FormData();
      cityname = cityname + "市";
      // console.log(cityname);
      params.append("cityname", cityname);
      //   console.log("params:", params);
      try {
        const response = await axios({
          url: "http://localhost:8081/index/visual/media/newyork",
          method: "post",
          data: params,
        });
        console.log(response.data); // 处理响应数据
        this.initChart(response.data);
      } catch (error) {
        console.error("Error:", error);
      }
    },
    initChart(datas) {
      if (datas != null) {
        const starttime = [];
        const counts = [];
        for (var i = 0; i < datas.length; i++) {
          starttime[i] = datas[i].starttime.split("-")[0];
          counts[i] = datas[i].counts;
        }
        console.log(starttime, counts);
        this.chart = echarts.init(this.$refs.chartDom);
        const option = {
          title: {
            text: "纽约时报报道次数",
            left: "center",
            textStyle: {
              fontSize: 16, //字体大小
              color: "#000", //字体颜色
            },
          },
          xAxis: {
            type: "category",
            data: starttime,
            color: "#000",
            axisLabel: {
              show: true,
              textStyle: {
                color: "#000",
              },
            },
          },
          yAxis: {
            type: "value",
            color: "#000",
            axisLabel: {
              show: true,
              textStyle: {
                color: "#000",
              },
            },
          },
          series: [
            {
              data: counts,
              type: "line",
              symbol: "triangle",
              symbolSize: 20,
              lineStyle: {
                color: "#000",
                width: 4,
                type: "dashed",
              },
              itemStyle: {
                borderWidth: 3,
                borderColor: "#EE6666",
                color: "yellow",
              },
            },
          ],
        };
        this.chart.setOption(option);
      } else {
        console.log("数据为空");
      }
    },
  },

  created() {
    this.selected = "纽约时报报道次数";
  },
  beforeDestroy() {
    if (this.chart) {
      this.chart.dispose();
    }
  },
};
</script>
<style>
.mediareport {
  border: 1px solid white;
}

.selectcity {
  /* 下拉框的样式 */
  width: 100%; /* 宽度可以根据需要调整 */
  padding: 8px; /* 添加一些内边距以提高可读性 */
  border: 1px solid #ccc; /* 边框样式 */
  border-radius: 4px; /* 边框圆角 */
}
</style>
