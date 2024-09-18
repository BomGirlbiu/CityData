<template>
  <div>
    <div class="container">
      <!-- 全国地图 机构趋势模块 -->
      <div class="china">
        <!-- 点击返回全国-->
        <div @click="returnCh">
          <img
            v-if="pyName !== 'china'"
            class="returnImg"
            src="@/assets/img/return.png"
          />
        </div>
        <div id="chinaMap" v-if="pyName === 'china'"></div>
        <div id="provinceMap" v-if="pyName !== 'china'">111</div>
      </div>
    </div>
  </div>
</template>
<script>
import { cityArr, totalMap } from "../../utils/mapData";
export default {
  name: "ChinaMap",
  components: {},
  data() {
    return {
      // 全省保费信息
      totalMap: null,
      // 各个城市的数据
      cityArr: null,
      myEchartsOfChina: null,
      // 默认选择的城市 这是拼音
      pyName: "china",
      // 保留一份省名的中文
      pyNameOfChinese: "",
    };
  },

  created() {
    // 拿到数据
    this.totalMap = totalMap;
    this.cityArr = cityArr;
    // 页面进来注册tooltip上面的点击事件 否则会报此事件undefined
    window.lookVideoGo = this.lookVideoGo;
  },

  // 页面挂载完成后调用
  mounted() {
    this.chinaMapFun();
  },
  watch: {
    pyName() {
      this.chinaMapFun();
    },
  },

  methods: {
    /*中国地图 参考文章：https://echarts.apache.org/zh/option.html#series-map*/
    chinaMapFun(cityName) {
      // 先处理数据 很重要
      let mapData = [];
      for (let i = 0; i < this.totalMap.length; i++) {
        let obj = { value: 0, datas: [] }; // 数组里面是多个对象
        obj.name = this.totalMap[i].comname2; // names属性时数据所对应的地图区域的名称，例如 '广东'，'浙江';参考文章： https://echarts.apache.org/zh/option.html#series-map.data
        obj.value = this.totalMap[i].achieveRate; // 该区域的数据值 number类型
        obj.datas[0] = this.totalMap[i].preium;
        obj.datas[1] = this.totalMap[i].target;

        //注意： 此行是模拟下面的省份用的 实际开发中每个省份的数据是后端返回的
        if (this.totalMap[i].children) {
          obj.children = this.totalMap[i].children;
        }
        mapData.push(obj);
      }

      // 这里进行筛选传进来的省份数据 模拟黑龙江省份下面的和黑河市
      if (this.pyNameOfChinese) {
        mapData = mapData.map((item) => {
          if (item.children) {
            return {
              name: item.children.comname2,
              value: item.children.achieveRate,
              datas: [item.children.preium, item.children.target],
            };
          }
        });
      }
      console.log("当前渲染的地图:", this.pyName);
      console.log("当前渲染的数据2：", mapData);

      // 1，初始化节点
      // 检测是否已经存在echarts实例，如果不存在，则不再去初始化
      if (this.pyName === "china") {
        this.myEchartsOfChina = this.$echarts.init(
          document.getElementById("chinaMap")
        );
      } else {
        this.myEchartsOfChina = this.$echarts.init(
          document.getElementById("provinceMap")
        );
      }

      // 显示加载动画
      this.myEchartsOfChina.showLoading();
      if (this.pyName === "china") {
        console.log("chinaMap");
        let province = require("../../../node_modules/echarts/map/json/china.json");
        // 注册地图数据
        this.$echarts.registerMap(this.pyName, province);
      } else {
        console.log("provinceMap");
        // 单独引入其他省份的地图  注意：registerMap方法的第一参数要和引入的省名相同
        let province = require("../../../node_modules/echarts/map/json/province/" +
          this.pyName +
          ".json");
        this.$echarts.registerMap(this.pyName, province);
      }
      this.myEchartsOfChina.hideLoading();

      //大地图的点击事件
      if (this.pyName == "china") {
        this.myEchartsOfChina.on("click", (params) => {
          this.lookVideoGo(params.name);
        });
      }
      /* 参考文档： https://echarts.apache.org/zh/option.html#series-map */
      // 设置整个中国地图的参数
      let options = {
        // backgroundColor: "rgba(0,0,0,0)",
        title: {
          show: false, // 是否显示标题组件
          text: "中国地图", // 主标题文本
          subtext: "注：展示当月和当年累计情况",
          left: "3%",
          top: "85%",
        },
        tooltip: {
          enterable: true, // 允许点击触发tooltip中的事件
          show: true, // 是否显示提示框组件，包括提示框浮层和 axisPointer。 [ default: true ]
          trigger: "item", // 触发类型。 [ default: 'item' ]
          //   triggerOn: "click", // 只有点击时才触发 不设置默认随鼠标移动并显示
          formatter: (array, returnData, callback) => {
            if (isNaN(array.value)) {
              if (this.cityArr.includes(array.name)) {
                return (
                  "保费: 暂无" +
                  "<br/>" +
                  "目标: 暂无" +
                  "<br/>" +
                  "保费达成率: 暂无"
                );
              } else {
                return "保费: 暂无" + "<br/>";
              }
            } else {
              let result =
                '<div style="display: flex"><div style="float:left;">保费: ' +
                array.data.datas[0] +
                "万元  <br/>  目标: " +
                array.data.datas[1] +
                "万元  <br/>  保费达成率: " +
                array.data.value +
                "%</div>" +
                '<div style="float:left; margin-left: 0.1rem;width: 0.05rem;height: 1rem; background: #D8D8D8;"></div>' +
                '<div style="float:left; margin-left: 0.1rem; "οnclick="lookVideoGo(\'' +
                array.name +
                "')\">&nbsp</div></div>";
              return result;
            }
          },
          backgroundColor: "rgba(50,50,50,0.7)", // tooltip 背景颜色 rgba
          // 文本设置
          textStyle: {
            color: "rgb(255,255,255)", // 值域文字颜色
            fontSize: 15,
          },
        },

        // 底部小导航图标
        visualMap: {
          // text: ['注：展示当月和当年累计情况'],
          orient: "horizontal",
          itemWidth: 15,
          textGap: 2,
          // calculable: false,
          show: true,
          left: "center",
          y: "bottom",
          splitList: [
            { end: 0, label: "无", color: "#DDDDDD" },
            { end: 30, color: "rgb(255,248,220)" },
            { start: 30, end: 60, label: "30-60", color: "rgb(252,235,207)" },
            { start: 60, end: 90, label: "60-90", color: "#FFDAB9" },
            { start: 90, end: 100, label: "90-100", color: "rgb(245,158,131)" }, // 245 158  131
            { start: 100, label: ">=100", color: "rgb(40,183,163)" }, // 40 183 163
          ],
        },
        backgroundColor: "rgba(255, 255, 255, 0.1)",//图表背景颜色

        series: [
          {
            name: "省份",
            type: "map", // 指定是地图类型
            map: this.pyName, // 和上面registerMap中的第一个参数值一致才可以正常加载地图
            zoom: 1.2,
            roam: true, // 是否开启平游或缩放
            geoIndex: 0,
            aspectScale: 0.75,
            scaleLimit: {
              // 滚轮缩放的极限控制
              min: 1,
              max: 2,
            },
            selectedMode: "single", // 选中模式，表示是否支持多个选中，默认关闭，支持布尔值和字符串，字符串取值可选'single'表示单选，或者'multiple'表示多选。
            itemStyle: {
              areaColor: "#FFFFFF",
              borderColor: "#0f0f0f",
              normal: { label: { show: true }, areaColor: "#DDDDDD" },
              emphasis: { label: { show: true } },
            },
            emphasis: {
              // 强调的样式，也就是鼠标移入后的样式==高亮状态下的多边形和标签样式。
              itemStyle: {
                areaColor: "#000000",
              },
            },
            label: {
              normal: {
                show: true, // 是否显示标签，这里显示的就是省份的名字。默认就是false
                textStyle: {
                  fontWeight: 300,
                  color: "#000000", // 值域文字颜色
                  fontSize: 12, // 文字的字体大 小
                },
              },
              emphasis: {
                show: false, // 在鼠标移入时，是否显示，如果不写，默认是显示的
              },
            },
            data: mapData, // 各省地图数据导入
          },
        ],
      };
      //点击事件

      // 设置各个省份地图的参数
      let options1 = {
        title: {
          show: false, // 是否显示标题组件
          subtext: "注：展示当月和当年累计情况",
          left: "3%",
          top: "85%",
        },
        tooltip: {
          enterable: true, // 允许点击触发tooltip中的事件
          show: true, // 是否显示提示框组件，包括提示框浮层和 axisPointer。 [ default: true ]
          trigger: "item", // 触发类型。 [default: "item",]
          backgroundColor: "rgba(50,50,50,0.7)", // tooltip 背景颜色 rgba
          // 文本设置
          textStyle: {
            color: "rgb(255,255,255)", // 值域文字颜色
            fontSize: 12,
          },
          formatter: (array, returnData, callback) => {
            console.log(array);
            if (isNaN(array.value)) {
              if (this.cityArr.includes(array.name)) {
                return (
                  "保费: 暂无" +
                  "<br/>" +
                  "目标: 暂无" +
                  "<br/>" +
                  "保费达成率: 暂无"
                );
              } else {
                return "保费: 暂无" + "<br/>";
              }
            } else {
              let result =
                '<div style="display: flex"><div style="float:left;">保费: ' +
                array.data.datas[0] +
                "万元  <br/>  目标: " +
                array.data.datas[1] +
                "万元  <br/>  保费达成率: " +
                array.data.value +
                "%</div>" +
                '<div style="float:left; margin-left: 0.1rem;width: 0.05rem;height: 1rem; background: #D8D8D8;"></div>' +
                '<div style="float:left; margin-left: 0.1rem; "οnclick="lookVideoGo(\'' +
                array.name +
                '\')"><p style="height:2rem; line-height:2rem;">详 情 >&nbsp</p></div></div>';
              return result;
            }
          },
        },
        // 底部小导航图标
        visualMap: {
          // text: ['注：展示当月和当年累计情况'],
          orient: "horizontal",
          itemWidth: 15,
          textGap: 2,
          // calculable: false,
          show: true,
          left: "center",
          y: "bottom",
          splitList: [
            { start: 6, label: ">=7", color: "#FFDAB9" },
            { start: 3, end: 6, label: "4-6", color: "rgb(245,158,131)" }, // 245 158  131
            { start: 1, end: 3, label: "1-3", color: "rgb(40,183,163)" }, // 40 183 163
            { end: 0, label: "无", color: "#DDDDDD" },
          ],
        },
        series: [
          {
            name: "省份", // 系列名称，用于tooltip的显示，legend 的图例筛选，在 setOption 更新数据和配置项时用于指定对应的系列。见上：可以在tooltip中获取到
            type: "map", // 指定是地图类型
            map: this.pyName, // 和上面registerMap中的一直
            zoom: 1.2,
            selectedMode: "single", // 选中模式，表示是否支持多个选中，默认关闭，支持布尔值和字符串，字符串取值可选'single'表示单选，或者'multiple'表示多选。
            itemStyle: {
              areaColor: "#000000",
              borderColor: "#0f0f0f",
              normal: { label: { show: true }, areaColor: "#DDDDDD" },
              emphasis: { label: { show: true } },
            },
            emphasis: {
              // 强调的样式，也就是鼠标移入后的样式==高亮状态下的多边形和标签样式。
              itemStyle: {
                areaColor: "#ffffff",
              },
            },
            label: {
              normal: {
                show: true, // 是否显示标签，这里显示的就是省份的名字。默认就是false
                textStyle: {
                  fontWeight: 300,
                  color: "#000000", // 值域文字颜色
                  fontSize: 12, // 文字的字体大 小
                },
              },
              emphasis: {
                show: false, // 在鼠标移入时，是否显示，如果不写，默认是显示的
              },
            },
            // 数据对不上 省下面的地区对不上
            data: mapData,
          },
        ],
      };
      // 判断是否是各个省份
      if (this.pyName === "china") {
        this.myEchartsOfChina.setOption(options);
      } else {
        this.myEchartsOfChina.setOption(options1);
      }
    },

    /* 传过来的参数是省份名 */
    lookVideoGo(cityName) {
      // 保留一份中文
      this.pyNameOfChinese = cityName;
      // this.myEchartsOfChina.clear(); // 清空当前实例，会移除实例中所有的组件和图表。
      this.myEchartsOfChina.dispose(); // 销毁后实例无法在使用

      // 获取城市拼音
      // 获取城市拼音
      for (var i = 0, len = this.cityArr[0].length; i < len; i++) {
        if (cityName === this.cityArr[0][i]) {
          // 获取得城市拼音
          this.pyName = this.cityArr[1][i];
          // 使用nextTick Api 防止echarts初始化时避免节点不存在的报错
          this.$nextTick(() => {
            this.chinaMapFun(this.pyName);
          });
          break;
        } else {
          console.warn("没有找到此城市的拼音");
        }
      }
    },
    /* 点击返回全国 */
    returnCh() {
      // this.myEchartsOfChina.clear(); // 清空当前实例，会移除实例中所有的组件和图表。
      this.myEchartsOfChina.dispose(); // 销毁后实例 这里使用dispose防止残留
      this.pyName = "china";
      this.pyNameOfChinese = "";

      // 使用nextTick Api 防止echarts初始化时避免节点不存在的报错
      this.$nextTick(() => {
        this.chinaMapFun();
      });
    },
  },
};
</script>
<style lang="scss" scoped>
.container {
  width: 100%;
  // margin: 0 auto;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-direction: row;
  flex-wrap: wrap;
  #chinaMap,
  #provinceMap {
    width: 1000px;
    height: 580px;
    margin-right: 30px;
    margin-top: 20px;
  }
  .china {
  }
  // 返回箭头
  .returnImg {
    cursor: pointer;
    display: block;
    width: 25px;
  }
}
</style>
