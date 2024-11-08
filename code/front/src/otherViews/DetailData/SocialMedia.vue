<template>
  <div class="socialmedia">
    <div class="select-city">
      社交媒体影响力
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
  name: "SocialMedia",
  components: { ZhiPu },
  data() {
    return {
      selected: "",
      chart: null,
      influences: [
        "多平台账号粉丝量",
        "bilibili网站评论倾向性",
        "YouTube评论倾向性",
      ],
      Question:
        "以下数据为" +
        "的各个社交平台的官方媒体账号粉丝量，单位为万，{该城市政务类账号，该城市文化类账号，该城市新闻类账号，社交平台}，将其理解为大众对该城市各个方面的关注度，分析为什么大众对这些方面感兴趣，最后总结，一共在500字以内，可以在回答中出现已知的数据",
      analyzedata: null,
    };
  },
  props: {
    selectedCity: String, // 声明selectedCity为String类型的prop
    isShowExplain: Boolean,
  },

  watch: {
    selectedCity: function (newVal, oldVal) {
      this.chart = null;
      if (this.selected == "bilibili网站评论倾向性") {
        this.socialemotion(newVal);
      } else if (this.selected == "多平台账号粉丝量") {
        this.socialMediafans(newVal);
      } else if (this.selected == "YouTube评论倾向性") {
        this.socialyoutube(newVal);
      }
      // console.log("selectedCity changed:", newVal);
    },
    selected: function (newVal, oldVal) {
      this.chart = null;
      if (newVal == "bilibili网站评论倾向性") {
        this.Question =
          "以下数据格式为" +
          "{城市名，消极评论数，中立评论数，社交平台，积极评论数}，具体解释为在该社交平台上，选取较为热门的帖子，其中的各种情绪的评论数，分析在该平台上对该城市的情感为什么是这种走向，并总结，不超过500字，清晰明了，不要加不确定的词汇";

        this.socialemotion(this.selectedCity);
      } else if (newVal == "多平台账号粉丝量") {
        this.Question =
          "以下数据为" +
          "的各个社交平台的官方媒体账号粉丝量，单位为万，{城市id，城市名，该城市政务类账号，该城市文化类账号，该城市新闻类账号，社交平台}，将其理解为大众对该城市各个方面的关注度，分析为什么大众对这些方面感兴趣，最后总结，一共在500字以内，可以在回答中出现已知的数据";

        this.socialMediafans(this.selectedCity);
      } else if (this.selected == "YouTube评论倾向性") {
        this.socialyoutube(this.selectedCity);
        this.Question =
          "以下数据格式为" +
          this.selectedCity +
          "{快乐评论数，伤心评论数，生气评论数，害怕评论数，惊喜评论数，喜爱评论数，恐慌评论数}，具体解释为在youtube社交平台上，选取较为热门的帖子，其中的各种情绪的评论数，分析在该平台上对该城市的情感为什么是这种走向，并总结，不超过500字，清晰明了，不要加不确定的词汇，不要在回答中出现我们给的明确数据";
      }
      // console.log("selected changed:", newVal);
    },
  },
  created() {
    this.selected = "多平台账号粉丝量";
  },
  methods: {
    async socialyoutube(cityname) {
      let params = new FormData();
      params.append("cityname", cityname + "市");

      // console.log("params:", params);
      // console.log("cityname:", cityname);
      try {
        const response = await axios({
          url: "http://localhost:82/index/visual/social/youtube",
          method: "post",
          data: params,
        });
        console.log(response.data); // 处理响应数据
        this.analyzedata = response.data;

        this.initChartyoutube(response.data);
      } catch (error) {
        console.error("Error:", error);
      }
    },
    async socialMediafans(cityname) {
      let params = new FormData();
      params.append("cityname", cityname);
      //   console.log("params:", params);
      try {
        const response = await axios({
          url: "http://localhost:82/index/visual/social/fans",
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
        var platall = [];
        for (var i = 0; i < datas.length; i++) {
          platall[i] = new Array(4);
          platall[i] = [
            datas[i].govern,
            datas[i].culture,
            datas[i].news,
            datas[i].plat,
          ];
        }
        // console.log(platall);
        var plat = ["抖音", "微博"];
        this.chart = echarts.init(this.$refs.chartDom);
        const option = {
          title: {
            text: "不同平台不同类型账号的粉丝量对比（单位：万）",
            left: "center",
            textStyle: {
              fontSize: 16, //字体大小
              color: "#fff", //字体颜色
            },
          },
          dataset: {
            source: [
              ["score", "amount", "product"],
              // 相同类的第一个指数相同
              //这个类的维度越重要，颜色就越深，表现在score越大
              //“政务类”前需要加上平台名称
              [85.3, platall[0][0], plat[0] + "政务类"],
              [58.3, platall[0][1], plat[0] + "文化类"],
              [22.3, platall[0][2], plat[0] + "媒体类"],
              [85.3, platall[1][0], plat[1] + "政务类"],
              [58.3, platall[1][1], plat[1] + "文化类"],
              [22.3, platall[1][2], plat[1] + "媒体类"],
            ],
          },
          grid: { containLabel: true },
          xAxis: {
            axisLine: {
              lineStyle: {
                color: "#FFF", // 将轴线颜色改为白色
              },
            },
            name: "粉丝量",
            axisLabel: {
              show: true,
              textStyle: {
                fontsize: 10,
                color: "#fff",
              },
            },
            show: true,
          },
          yAxis: [
            {
              axisLine: {
                lineStyle: {
                  color: "#FFF", // 将轴线颜色改为白色
                },
              },
              name: "账号类型及平台",
              type: "category",
              axisLabel: {
                show: true,
                textStyle: {
                  fontsize: 10,
                  color: "#fff",
                },
              },
              show: true,
            },
          ],
          visualMap: {
            show: true,
            orient: "horizontal",
            left: "center",
            min: 10,
            max: 100,
            text: ["政务类", "媒体类"],
            textStyle: {
              fontSize: 12, //字体大小
              color: "#fff", //字体颜色
            },
            // Map the score column to color
            dimension: 0,
            inRange: {
              color: ["#65B581", "#FFCE34", "#FD665F"],
            },
          },
          series: [
            {
              type: "bar",
              encode: {
                // Map the "amount" column to X axis.
                x: "amount",
                // Map the "product" column to Y axis
                y: "product",
              },
            },
          ],
        };
        this.chart.setOption(option);
        // this.chart.setOption(option);
      } else {
        this.chart.dispose();
        this.chart = null;
        console.log("数据为空");
      }
    },
    async socialemotion(cityname) {
      let params = new FormData();
      params.append("cityname", cityname);
      //   console.log("params:", params);
      try {
        const response = await axios({
          url: "http://localhost:82/index/visual/social/emotion",
          method: "post",
          data: params,
        });
        // console.log(response.data); // 处理响应数据
        this.initChart2(response.data);
        this.analyzedata = response.data;
      } catch (error) {
        console.error("Error:", error);
      }
    },

    initChart2(datas) {
      this.chart = echarts.init(this.$refs.chartDom);
      if (datas != null && datas.length > 0) {
        var tend = [];
        // console.log(datas[0].positiveNum);
        // console.log(datas);
        tend[0] = datas[0].positiveNum;
        tend[1] = datas[0].negativeNum;
        tend[2] = datas[0].neutralityNum;
        // console.log(tend);
        this.analyzedata = tend;
        const option2 = {
          tooltip: {
            trigger: "item",
          },
          title: {
            text: "情绪分析",
            left: "center",
            textStyle: {
              fontSize: 13, //字体大小
              color: "#fff", //字体颜色
            },
          },
          legend: {
            top: "5%",
            left: "center",
            textStyle: {
              fontSize: 13, //字体大小
              color: "#fff", //字体颜色
            },
          },
          xAxis: { show: false },
          yAxis: { show: false },
          visualMap: { show: false },
          series: [
            {
              name: "Access From",
              type: "pie",
              radius: ["40%", "70%"],
              avoidLabelOverlap: true,
              itemStyle: {
                borderRadius: 10,
                borderColor: "#fff",
                borderWidth: 2,
                color: "#000",
              },
              label: {
                show: false,
                position: "center",
              },
              emphasis: {
                label: {
                  show: true,
                  fontSize: 40,
                  fontWeight: "bold",
                },
              },

              labelLine: {
                show: false,
              },
              data: [
                {
                  value: tend[0],
                  name: "积极情绪",
                  itemStyle: { color: "#2f4554", fontSize: 10 },
                },
                {
                  value: tend[1],
                  name: "消极情绪",
                  itemStyle: { color: "#61a0a8" },
                },
                {
                  value: tend[2],
                  name: "中立",
                  itemStyle: { color: "#d48265" },
                },
              ],
            },
          ],
        };
        this.chart.setOption(option2);
      } else {
        this.chart.dispose();
        this.chart = null;
        // console.log("数据为空");
      }
    },
    initChartyoutube(datas) {
      this.chart = echarts.init(this.$refs.chartDom);
      if (datas != null && datas.length > 0) {
        var tend = [];
        // console.log(datas[0].positiveNum);
        // console.log(datas);
        tend[0] = datas[0].joyNum;
        tend[1] = datas[0].sadnessNum;
        tend[2] = datas[0].angerNum;
        tend[3] = datas[0].fearNum;
        tend[4] = datas[0].surpriseNum;
        tend[5] = datas[0].loveNum;
        tend[6] = datas[0].disgustNum;
        // console.log(tend);
        this.analyzedata = tend;
        const option2 = {
          tooltip: {
            trigger: "item",
          },
          title: {
            text: "情绪分析",
            left: "center",
            textStyle: {
              fontSize: 13, //字体大小
              color: "#fff", //字体颜色
            },
          },
          legend: {
            top: "5%",
            left: "center",
            textStyle: {
              fontSize: 13, //字体大小
              color: "#fff", //字体颜色
            },
          },
          xAxis: { show: false },
          yAxis: { show: false },
          visualMap: { show: false },
          series: [
            {
              name: "Access From",
              type: "pie",
              radius: ["40%", "70%"],
              avoidLabelOverlap: true,
              itemStyle: {
                borderRadius: 10,
                borderColor: "#fff",
                borderWidth: 2,
                color: "#000",
              },
              label: {
                show: false,
                position: "center",
              },
              emphasis: {
                label: {
                  show: true,
                  fontSize: 40,
                  fontWeight: "bold",
                },
              },

              labelLine: {
                show: false,
              },
              data: [
                {
                  value: tend[0],
                  name: "喜悦",
                  itemStyle: { color: "#2f4554", fontSize: 10 },
                },
                {
                  value: tend[1],
                  name: "悲观",
                  itemStyle: { color: "#61a0a8" },
                },
                {
                  value: tend[2],
                  name: "生气",
                  // itemStyle: { color: "#d48265" },
                },
                {
                  value: tend[3],
                  name: "恐惧",
                  // itemStyle: { color: "#d48265" },
                },
                {
                  value: tend[4],
                  name: "惊喜",
                  // itemStyle: { color: "#d48265" },
                },
                {
                  value: tend[5],
                  name: "喜爱",
                  // itemStyle: { color: "#d48265" },
                },
                {
                  value: tend[6],
                  name: "恐慌",
                  itemStyle: { color: "#d48265" },
                },
              ],
            },
          ],
        };
        this.chart.setOption(option2);
      } else {
        this.chart.dispose();
        this.chart = null;
        // console.log("数据为空");
      }
    },
  },
  beforeDestroy() {
    this.chart.dispose();
  },
};
</script>
<style>
.socialmedia {
  height: 90%;
  width: 100%;
  position: relative;
}
/* .select-city {
  /* 为下拉框容器设置样式（如果需要的话）
}
*/

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
  width: 40%; /* 子元素的宽度 */
  height: 100%; /* 子元素的高度 */
}
</style>
