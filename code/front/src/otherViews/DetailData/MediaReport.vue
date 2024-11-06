<template>
  <div class="mediareport">
    <div class="select-city">
      媒体报道影响力
      <select v-model="selected" class="selectcity">
        <option disabled value="">请选择二级影响因子...</option>
        <option v-for="item in influences" :key="item">{{ item }}</option>
      </select>
    </div>
    <!-- 如果需要展示分析结果的话，就占50%，不展示则为100% -->
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
  name: "MediaReport",
  props: {
    selectedCity: String, // 声明selectedCity为String类型的prop
    isShowExplain: Boolean,
  },
  components: {
    ZhiPu,
  },
  data() {
    return {
      selected: "",
      chart: null,
      analyzedata: null,
      Question:
        "以下是关于一个城市的纽约时报报道量的相关数据，请结合当地的时讯和经济政治等分析数据发生波动的原因，数据格式为{城市名，时间范围内纽约时报对该城市的报道次数，报道计算开始时间，报道计算终止时间}：直接列出每年波动的原因最后总结即可，不用列出数据里已经提供过的内容，不用分点，直接分成两段，其中总结写为一段，控制在500字以内",
      influences: ["纽约时报报道次数"],
    };
  },
  watch: {
    selectedCity: function (newVal, oldVal) {
      if (this.selected == "纽约时报报道次数") {
        this.Question =
          "以下是关于一个城市的纽约时报报道量的相关数据，请结合当地的时讯和经济政治等分析数据发生波动的原因，数据格式为{城市名，时间范围内纽约时报对该城市的报道次数，报道计算开始时间，报道计算终止时间}：直接列出每年波动的原因最后总结即可，不用列出数据里已经提供过的内容，不用分点，直接分成两段，其中总结写为一段，控制在600字以内，不要空行";
        this.newyork(newVal);
      }
      // console.log("selectedCity changed:", newVal);
    },
    selected: function (newVal, oldVal) {
      if (newVal == "纽约时报报道次数") {
        this.newyork(this.selectedCity);
      }
      // console.log("selected changed:", newVal);
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
        this.initChart(response.data);
        this.analyzedata = response.data;
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
  position: relative;
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
.explain_detail {
  position: absolute; /* 设置为绝对定位 */
  top: 0; /* 顶部与父元素对齐 */
  right: 0%; /* 右侧距离父元素右侧0% */
  width: 50%; /* 子元素的宽度 */
  height: 100%; /* 子元素的高度 */
}
</style>
