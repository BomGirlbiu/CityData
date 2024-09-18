<template>
  <div class="search">
    <div class="select-city">
      搜索引擎影响力
      <select v-model="selected" class="selectcity">
        <option disabled value="">请选择二级影响因子...</option>
        <option v-for="item in influences" :key="item">{{ item }}</option>
      </select>
    </div>
    <div
      ref="chartDom"
      class="echarts"
      style="width: 450px; height: 300px"
    ></div>
  </div>
</template>
<script>
import axios from "axios";
import echarts, { graphic } from "echarts";
export default {
  name: "SearchEngine",
  data() {
    return {
      selected: "",
      chart: null,
      influences: ["搜索量影响力"],
    };
  },
  props: {
    selectedCity: String, // 声明selectedCity为String类型的prop
  },

  watch: {
    selectedCity: function (newVal, oldVal) {
      this.chart = null;
      if (this.selected == "搜索量影响力") {
        this.googleSearch(newVal);
      }
      console.log("selectedCity changed:", newVal);
    },
    selected: function (newVal, oldVal) {
      this.chart = null;
      if (newVal == "搜索量影响力") {
        this.googleSearch(this.selectedCity);
      }
      console.log("selected changed:", newVal);
    },
  },
  created() {
    this.selected = "搜索量影响力";
  },
  methods: {
    async googleSearch(cityname) {
      let params = new FormData();
      params.append("cityname", cityname);
      // console.log("params:", params);
      try {
        const response = await axios({
          url: "http://localhost:8081/index/visual/search/google",
          method: "post",
          data: params,
        });
        // console.log(response.data); // 处理响应数据
        this.initChart(response.data);
      } catch (error) {
        console.error("Error:", error);
      }
    },
    initChart(datas) {
      if (datas != null && datas.length > 0) {
        // console.log("我有数据");
        var counts = [];
        var year = [];
        for (var i = 0; i < datas.length; i++) {
          counts[i] = datas[i].counts;
          year[i] = datas[i].week;
        }
        this.chart = echarts.init(this.$refs.chartDom);
        const option = {
          title: {
            text: "google城市搜索量",
            left: "center",
            textStyle: {
              fontSize: 16, //字体大小
              color: "#000", //字体颜色
            },
          },
          grid: {
            bottom: 80,
          },
          toolbox: {
            feature: {
              dataZoom: {
                yAxisIndex: "none",
              },
              restore: {},
              saveAsImage: {},
            },
          },
          tooltip: {
            trigger: "axis",
            axisPointer: {
              type: "cross",
              animation: false,
              label: {
                backgroundColor: "#505765",
              },
            },
          },
          legend: {
            data: ["Search volume"],
            left: 10,
            textStyle: {
              fontSize: 15, //字体大小
              color: "#000", //字体颜色
            },
          },
          dataZoom: [
            {
              show: true,
              realtime: true,
              start: 65,
              end: 85,
            },
            {
              type: "inside",
              realtime: true,
              start: 65,
              end: 85,
            },
          ],
          xAxis: [
            {
              type: "category",
              boundaryGap: false,
              axisLine: { onZero: false },
              axisLabel: {
                show: true,
                textStyle: {
                  color: "#000",
                },
              },
              // prettier-ignore
              data: year.map(function (str) {
											return str.replace(' ', '\n');
										}),
            },
          ],
          yAxis: [
            {
              name: "Search volume(次数)",
              type: "value",
              axisLabel: {
                show: true,
                textStyle: {
                  color: "#fff",
                },
              },
            },
          ],
          series: [
            {
              name: "Search volume",
              type: "line",
              areaStyle: {},
              lineStyle: {
                width: 1,
              },
              emphasis: {
                focus: "series",
              },
              markArea: {
                silent: true,
                itemStyle: {
                  opacity: 0.3,
                },
                data: [
                  [
                    {
                      xAxis: "2023/6/11",
                    },
                    {
                      xAxis: "2024/6/30",
                    },
                  ],
                ],
              },
              // prettier-ignore
              data:counts,
            },
          ],
        };
        this.chart.setOption(option);
      } else {
        this.chart = null;
      }
    },
  },
};
</script>
<style>
.search {
  border: 1px solid white;
}
/* .select-city {
  /* 为下拉框容器设置样式（如果需要的话） 
} */

.selectcity {
  /* 下拉框的样式 */
  width: 30%; /* 宽度可以根据需要调整 */
  padding: 8px; /* 添加一些内边距以提高可读性 */
  border: 1px solid #ccc; /* 边框样式 */
  border-radius: 4px; /* 边框圆角 */
}
</style>
