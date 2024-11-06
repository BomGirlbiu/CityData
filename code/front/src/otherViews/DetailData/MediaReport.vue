<template>
  <div class="mediareport">
    <div class="select-city">
      媒体报道影响力
      <select v-model="selected" class="selectcity">
        <option disabled value="">请选择二级影响因子...</option>
        <option v-for="item in influences" :key="item">{{ item }}</option>
      </select>
    </div>
    <div ref="chartDom" class="echarts" style="width: 100%; height: 100%">
      <img
        class="imgNodata"
        v-show="chart == null"
        src="../../assets/image/暂无数据.png"
      />
    </div>
  </div>
</template>
<script>
import axios from "axios";
import * as echarts from "echarts";
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
          url: "http://localhost:82/index/visual/media/newyork",
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
      if (datas != null && datas.length > 0) {
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
              fontSize: 16, // 字体大小
              color: "#FFF", // 字体颜色改为白色
            },
          },
          xAxis: {
            name: "年份",
            nameTextStyle: {
              color: "#fff", // y轴名称字体颜色改为白色
            },
            type: "category",
            data: starttime,
            color: "#000", // 注意：这里的 color 属性对轴线的颜色进行设置，通常不影响标签颜色
            axisLabel: {
              show: true,
              textStyle: {
                color: "#FFF", // 字体颜色改为白色
              },
            },
          },
          yAxis: {
            type: "value",
            color: "#000", // 注意：这里的 color 属性对轴线的颜色进行设置，通常不影响标签颜色
            axisLabel: {
              show: true,
              textStyle: {
                color: "#FFF", // 字体颜色改为白色
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
                color: "#000", // 线条颜色
                width: 4,
                type: "dashed",
              },
              itemStyle: {
                borderWidth: 3,
                borderColor: "#EE6666",
                color: "yellow", // 数据点的填充颜色
              },
            },
          ],
        };
        this.chart.setOption(option);
      } else {
        this.chart.dispose();
        this.chart = null;
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
  height: 90%;
}

.selectcity {
  /* 下拉框的样式 */
  width: 100%; /* 宽度可以根据需要调整 */
  padding: 8px; /* 添加一些内边距以提高可读性 */

  /* 背景颜色设置为浅蓝色，与整体蓝色基调协调 */
  background-color: #e6f7ff; /* 浅蓝色 */

  /* 文字颜色设置为深蓝或黑色，以确保文字清晰可见 */
  color: #003366; /* 深蓝色 */

  /* 边框颜色设置为比背景稍深的蓝色，以提供视觉分隔 */
  border: 1px solid #87ceeb; /* 钢蓝色 */

  /* 边框圆角，使下拉框看起来更柔和 */
  border-radius: 4px;

  /* 移除左外边距，保持布局整洁 */
  margin-left: 0;
}
</style>
