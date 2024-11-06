<template>
  <div class="conclusion">
    <div
      v-if="isShowExplain"
      ref="chartDom"
      class="echarts"
      style="width: 38%; height: 100%"
    >
      <img
        class="imgNodata"
        v-show="chartall == null"
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
        v-show="chartall == null"
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
export default {
  name: "Conclusion",
  components: {
    ZhiPu: () => import("./ZhiPu.vue"),
  },
  data() {
    return {
      chartall: null,
      analyzedata: null,
      Question:
        "以下数据的结构为{城市名，城市id，媒体报道影响力，网络传播影响力，搜索引擎影响力，社交媒体影响力，综合影响力，国际访客影响力}，分析该城市这些数据高低的原因，控制在500字以内，不用重复已知内容，直接陈列原因即可",
    };
  },
  props: {
    selectedCity: String, // 声明selectedCity为String类型的prop
    isShowExplain: Boolean,
  },

  watch: {
    selectedCity: function (newVal, oldVal) {
      this.tourism(newVal);
      this.Question =
        "以下数据的结构为{城市名，城市id，媒体报道影响力，网络传播影响力，搜索引擎影响力，社交媒体影响力，综合影响力，国际访客影响力}，分析该城市这些数据高低的原因，控制在500字以内，不用重复已知内容";
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
          url: "http://localhost:82/index/visual/conclusion",
          method: "post",
          data: params,
        });
        this.initChart(response.data);
        // console.log(response.data);
        this.analyzedata = response.data;
      } catch (error) {
        console.error("Error:", error);
      }
    },
    initChart(datas) {
      if (datas != null && datas.length > 0) {
        var rate = [];
        rate[0] = datas[0].network;
        rate[1] = datas[0].mediatr;
        rate[2] = datas[0].social;
        rate[3] = datas[0].tourism;
        rate[4] = datas[0].searchin;
        this.chartall = echarts.init(this.$refs.chartDom);
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
                  // name: "指数大小",
                  // areaStyle: {
                  //   color: "rgba(255, 228, 52, 0.6)",
                  // },
                },
              ],
            },
          ],
        };
        this.chartall.setOption(option);
      } else {
        this.chartall.dispose();
        this.chartall = null;
      }
    },
  },
};
</script>
<style>
.echarts {
}
.conclusion {
  height: 100%;
  width: 100%;
  position: relative;
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

.imgNodata {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); /* 水平和垂直居中 */
  max-width: 100%;
  height: auto;
  z-index: 100;
}
.explain_detail {
  position: absolute; /* 设置为绝对定位 */
  top: 0; /* 顶部与父元素对齐 */
  right: 0%; /* 右侧距离父元素右侧0% */
  width: 50%; /* 子元素的宽度 */
  height: 100%; /* 子元素的高度 */
  /* background-color: aquamarine; */
}
</style>
