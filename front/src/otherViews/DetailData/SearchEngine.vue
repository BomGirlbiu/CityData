<template>
  <div class="search">
    <div class="select-city">
      搜索引擎影响力
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
// import echarts, { graphic } from "echarts";
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
          url: "http://localhost:82/index/visual/search/google",
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
              fontSize: 16, // 字体大小
              color: "#fff", // 字体颜色改为白色
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
                textStyle: {
                  color: "#fff", // tooltip 标签字体颜色改为白色
                },
              },
            },
          },
          legend: {
            data: ["Search volume"],
            left: 10,
            textStyle: {
              fontSize: 10, // 字体大小
              color: "#fff", // 图例字体颜色改为白色
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
              name: "时间",
              type: "value",
              nameTextStyle: {
                color: "#fff", // y轴名称字体颜色改为白色
              },
              type: "category",
              boundaryGap: false,
              axisLine: { onZero: false },
              axisLabel: {
                show: true,
                textStyle: {
                  color: "#fff", // x轴标签字体颜色改为白色
                },
              },
              data: year.map(function (str) {
                return str.replace(" ", "\n");
              }),
            },
          ],
          yAxis: [
            {
              name: "Search volume(次数)",
              type: "value",
              nameTextStyle: {
                color: "#fff", // y轴名称字体颜色改为白色
              },
              axisLabel: {
                show: true,
                textStyle: {
                  color: "#fff", // y轴标签字体颜色改为白色
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
                label: {
                  textStyle: {
                    color: "#fff", // markArea 标签字体颜色（如果需要的话）改为白色
                  },
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
              data: counts,
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
};
</script>
<style>
.search {
  height: 90%;
  /* 确保search容器的样式不会干扰内部元素的对齐 */
}

.select-city {
  /* 设置select-city div的文本对齐方式为左对齐 */
  text-align: left;
  /* 如果需要，可以添加其他样式，如padding, margin等 */
  margin-bottom: 10px; /* 例如，添加一些底部外边距以分隔元素 */
}

.selectcity {
  /* 下拉框的样式，这里主要是宽度和边框等样式 */
  width: 30%; /* 根据需要调整宽度 */
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>
