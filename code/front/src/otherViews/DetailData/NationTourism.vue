<template>
  <div class="nationtourism">
    <div class="select-city">
      国际访客影响力
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
        v-show="chart == null"
        src="../../assets/image/暂无数据.png"
      />
    </div>
    <div
      v-else
      ref="chartDom"
      class="echarts"
      style="width: 100%; height: 100%"
    >
      <img
        class="imgNodata"
        v-show="chart == null"
        src="../../assets/image/暂无数据.png"
      />
    </div>
    <div v-show="isShowExplain" class="explain_detail">
      <ZhiPu :analyzedata="analyzedata" :Question="Question"></ZhiPu>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import * as echarts from "echarts";
import ZhiPu from "./ZhiPu.vue";
export default {
  name: "NationTourism",
  components: {
    ZhiPu,
  },
  data() {
    return {
      selected: "",
      chart: null,
      Question:
        "以下数据格式为{年份，城市，谷歌搜索量，来访旅游量}，我们不用管谷歌搜索量，针对该城市的每年来访旅游量进行分析，结合该城市的经济情况和时讯政治分析旅游量数据每年发生波动的原因，直接列出每年波动的原因最后总结即可，不用列出数据里已经提供过的内容，不用分点，直接分成两段，其中总结写为一段，控制在500字以内，不要空行",
      analyzedata: null,
      influences: ["国外入境旅游量时序图"],
    };
  },
  props: {
    selectedCity: String, // 声明selectedCity为String类型的prop
    isShowExplain: Boolean,
  },

  watch: {
    selectedCity: function (newVal, oldVal) {
      if (this.selected == "国外入境旅游量时序图") {
        (this.Question =
          "以下数据格式为{年份，城市，谷歌搜索量，来访旅游量}，我们不用管谷歌搜索量，针对该城市的每年来访旅游量进行分析，结合该城市的经济情况和时讯政治分析旅游量数据每年发生波动的原因，直接列出每年波动的原因最后总结即可，不用列出数据里已经提供过的内容，不用分点，直接分成两段，其中总结写为一段，控制在600字以内，不要空行"),
          this.tourism(newVal);
      }
      // console.log("selectedCity changed:", newVal);
    },
    selected: function (newVal, oldVal) {
      if (newVal == "国外入境旅游量时序图") {
        this.tourism(this.selectedCity);
        this.Question =
          "以下数据格式为{年份，城市，谷歌搜索量，来访旅游量}，我们不用管谷歌搜索量，针对该城市的每年来访旅游量进行分析，结合该城市的经济情况和时讯政治分析旅游量数据每年发生波动的原因，直接列出每年波动的原因最后总结即可，不用列出数据里已经提供过的内容，不用分点，直接分成两段，其中总结写为一段，控制在600字以内，不要空行";
        // console.log("selected changed:", newVal);
      }
    },
  },
  created() {
    this.selected = "国外入境旅游量时序图";
  },
  methods: {
    async tourism(cityname) {
      let params = new FormData();
      params.append("cityname", cityname);
      //   console.log("params:", params);
      try {
        const response = await axios({
          url: "http://localhost:82/index/visual/nation/tourism",
          method: "post",
          data: params,
        });
        // console.log(response.data); // 处理响应数据
        this.analyzedata = response.data;
        this.initChart(response.data);
      } catch (error) {
        console.error("Error:", error);
      }
    },
    initChart(datas) {
      if (datas != null && datas.length > 0) {
        this.chart = echarts.init(this.$refs.chartDom);
        var shuzu = [],
          nianfen = [];
        for (var i = 0; i < datas.length; i++) {
          shuzu[i] = datas[i].tourist / 100;
        }
        for (var j = 0; j < datas.length; j++) {
          nianfen[j] = datas[j].year;
        }
        const option = {
          title: {
            text: "国外入境旅游量",
            subtext: "（逐年递增）",
            textStyle: {
              fontSize: 18, // 字体大小
              color: "#fff", // 字体颜色改为白色
            },
          },
          xAxis: {
            name: "年份",
            nameTextStyle: {
              color: "#fff", // y轴名称字体颜色改为白色（注意：这里应该是xAxis的名称，所以描述为y轴是不准确的）
            },
            data: nianfen,
            axisLabel: {
              inside: true,
              color: "#fff", // 字体颜色改为白色
            },
            axisTick: {
              show: false,
            },
            axisLine: {
              show: false,
            },
            z: 10,
          },
          yAxis: {
            axisLine: {
              show: false,
            },
            axisTick: {
              show: false,
            },
            axisLabel: {
              color: "#fff", // 字体颜色改为白色
            },
          },
          dataZoom: [
            {
              type: "inside",
            },
          ],
          series: [
            {
              type: "bar",
              showBackground: true,
              itemStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: "#68c391" }, // 绿色起始颜色
                  { offset: 0.5, color: "#32a465" }, // 绿色中间颜色
                  { offset: 1, color: "#32a465" }, // 绿色结束颜色，与中间颜色相同以实现渐变效果
                ]),
              },
              emphasis: {
                itemStyle: {
                  color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    { offset: 0, color: "#50b37e" }, // 强调时的起始颜色，稍微深一些的绿色
                    { offset: 0.7, color: "#50b37e" },
                    { offset: 1, color: "#68c391" }, // 强调时的结束颜色，与起始颜色相近但稍浅
                  ]),
                },
              },
              data: shuzu,
            },
          ],
        };
        const zoomSize = 6;
        // 点击消失，但是会报错。。
        this.chart.on("click", function (params) {
          // console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
          this.chart.dispatchAction({
            type: "dataZoom",
            startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
            endValue:
              dataAxis[
                Math.min(params.dataIndex + zoomSize / 2, data.length - 1)
              ],
          });
        });
        this.chart.setOption(option);
      } else {
        this.chart.dispose();
        this.chart = null;
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
.nationtourism {
  height: 100%;
  width: 100%;
  position: relative;
}

.selectcity {
  /* 下拉框的样式 */
  width: 100%; /* 宽度可以根据需要调整 */
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
