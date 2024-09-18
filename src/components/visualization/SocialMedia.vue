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
      ref="chartDom"
      class="echarts"
      style="width: 450px; height: 300px"
    ></div>
  </div>
</template>
<script>
import axios from "axios";
import echarts from "echarts";
export default {
  name: "SocialMedia",
  data() {
    return {
      selected: "",
      chart: null,
      influences: [
        "多平台账号粉丝量",
        "bilibili网站评论倾向性",
        "YouTube评论倾向性",
      ],
    };
  },
  props: {
    selectedCity: String, // 声明selectedCity为String类型的prop
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
      console.log("selectedCity changed:", newVal);
    },
    selected: function (newVal, oldVal) {
      this.chart = null;
      if (newVal == "bilibili网站评论倾向性") {
        this.socialemotion(this.selectedCity);
      } else if (newVal == "多平台账号粉丝量") {
        this.socialMediafans(this.selectedCity);
      } else if (this.selected == "YouTube评论倾向性") {
        this.socialyoutube(this.selectedCity);
      }
      console.log("selected changed:", newVal);
    },
  },
  created() {
    this.selected = "多平台账号粉丝量";
  },
  methods: {
    async socialyoutube(cityname) {
      let params = new FormData();
      params.append("cityname", cityname);

      // console.log("params:", params);
      // console.log("cityname:", cityname);
      try {
        const response = await axios({
          url: "http://localhost:8081/index/visual/social/youtube",
          method: "post",
          data: params,
        });
        console.log(response.data); // 处理响应数据
        this.initChart2(response.data);
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
          url: "http://localhost:8081/index/visual/social/fans",
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
        console.log(platall);
        var plat = ["抖音", "微博"];
        this.chart = echarts.init(this.$refs.chartDom);
        const option = {
          title: {
            text: "不同平台不同类型账号的粉丝量对比（单位：万）",
            left: "center",
            textStyle: {
              fontSize: 16, //字体大小
              color: "#000", //字体颜色
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
            name: "amount",
            axisLabel: {
              show: true,
              textStyle: {
                fontsize: 10,
                color: "#000",
              },
            },
            show: true,
          },
          yAxis: [
            {
              name: "账号类型及平台",
              type: "category",
              axisLabel: {
                show: true,
                textStyle: {
                  fontsize: 10,
                  color: "#000",
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
              color: "#000", //字体颜色
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
        console.log("数据为空");
      }
    },
    async socialemotion(cityname) {
      let params = new FormData();
      params.append("cityname", cityname);
      //   console.log("params:", params);
      try {
        const response = await axios({
          url: "http://localhost:8081/index/visual/social/emotion",
          method: "post",
          data: params,
        });
        // console.log(response.data); // 处理响应数据
        this.initChart2(response.data);
      } catch (error) {
        console.error("Error:", error);
      }
    },

    initChart2(datas) {
      this.chart = echarts.init(this.$refs.chartDom);
      if (datas != null) {
        var tend = [];
        // console.log(datas[0].positiveNum);
        // console.log(datas);
        tend[0] = datas[0].positiveNum;
        tend[1] = datas[0].negativeNum;
        tend[2] = datas[0].neutralityNum;
        // console.log(tend);
        const option2 = {
          tooltip: {
            trigger: "item",
          },
          title: {
            text: "情绪分析",
            left: "center",
            textStyle: {
              fontSize: 16, //字体大小
              color: "#000", //字体颜色
            },
          },
          legend: {
            top: "5%",
            left: "center",
            textStyle: {
              fontSize: 13, //字体大小
              color: "#000", //字体颜色
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
                  itemStyle: { color: "#2f4554" },
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
        console.log("数据为空");
      }
    },
  },
  beforeDestroy() {
    if (!this.chart) {
      return;
    }
    this.chart.dispose();
    this.chart = null;
  },
};
</script>
<style>
.socialmedia {
  border: 1px solid white;
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
</style>
