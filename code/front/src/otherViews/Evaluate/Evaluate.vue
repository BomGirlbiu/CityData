<template>
    <div class="evaluate">
      <div class="jieshao">
        {{ text }}
      </div>
      <div ref="chartDom" class="echarts"></div>
      <el-table
        ref="multipleTable"
        :row-key="rowKey"
        :data="compData"
        style="width: 100%"
        :header-cell-style="{
          background: '#16457c',
          color: 'white',
          fontSize: '18px',
        }"
        :default-sort="{ prop: 'date', order: 'descending' }"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55" :reserve-selection="true">
        </el-table-column>
        <el-table-column prop="cityName" label="城市" sortable width="120">
        </el-table-column>
        <el-table-column
          prop="totalrate"
          label="综合传播指数"
          sortable
          width="180"
        >
        </el-table-column>
        <el-table-column
          prop="network"
          label="网络传播影响力"
          sortable
          width="180"
        >
        </el-table-column>
        <el-table-column
          prop="mediatr"
          label="媒体报道影响力"
          sortable
          width="180"
        >
        </el-table-column>
        <el-table-column
          prop="social"
          label="社交媒体影响力"
          sortable
          width="180"
        >
        </el-table-column>
        <el-table-column
          prop="tourism"
          label="国际访客影响力"
          sortable
          width="180"
        >
        </el-table-column>
        <el-table-column
          prop="searchin"
          label="搜索引擎影响力"
          sortable
          width="200"
        >
        </el-table-column>
      </el-table>
      <!-- 分页功能的实现 -->
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[5, 10, 20, 30, 50]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination>
      <div style="margin-top: 10px; margin-bottom: 20px">
        <el-button @click="showSelection()">查看</el-button>
        <el-button @click="toggleSelection()">重置</el-button>
      </div>
      <div v-if="isLoading" class="loading-text">加载中...</div>
    </div>
  </template>
  
  <script>
  // import * as echarts from 'echarts';
  import axios from "axios";
  import "echarts/theme/idea";
  import * as echarts from "echarts";
  export default {
    name: "CityInfluenceChart",
    data() {
      return {
        chart: null,
        titleText:
          "对于中国城市国际传播指数，在指标选取层面，我们将网络传播影响力、媒体报道影响力、社交媒体影响力、搜索引擎影响力、国际访客影响力5个基本的考察维度作为一级指标，使用熵值法确定各级指标的具体权重并计算得到各个城市的综合传播指数。关于数据来源，网络传播影响力和社交媒体影响力数据来自google、抖音、微博等社交媒体平台，媒体报道影响力数据来自纽约时报，搜索引擎响力数据则取自官网出入境公开文件。",
        index: 0,
        text: "",
        allCityList: [], //记录初始数据
        cityList: [], // 所有城市数据，用于显示列表
        isLoading: false, // 是否正在加载
        currentPage: 1, //当前页数
        pageSize: 10, // 每页显示条数
        total: 0, // 总条数
        selectedCity: "",
        multipleSelection: [], //记录选中的行
      };
    },
    created() {
      this.fetchCityData(); // 在组件创建时调用数据获取方法
      // console.log("created被调用了")
      //   console.log("created被调用了"+this.allCityList)
    },
    computed: {
      compData() {
        return this.cityList.slice(
          (this.currentPage - 1) * this.pageSize,
          this.currentPage * this.pageSize
        );
      },
    },
    mounted() {
      setInterval(() => {
        this.autoTyping();
      }, 30);
    },
    methods: {
      autoTyping() {
        this.index++;
        this.text = this.titleText.slice(0, this.index);
      },
      async fetchCityData() {
        this.currentPage = 1;
        if (this.isLoading) return;
        try {
          this.isLoading = true;
          const response = await axios.get(
            "http://localhost:82/index/evaluate"
          );
          console.log(response);
          this.cityList = response.data.list;
          this.allCityList = this.cityList; //创建组件的时候将初始数据赋值
          this.total = response.data.total;
          // 假设后端返回的对象中有一个items数组
          // this.cityList = [...this.cityList, ...response.data]; // 假设后端返回的对象中有一个items数组
          //  this.cityList = response.data;  // 假设 API 返回的数据格式直接对应 cityList
          this.initChart(); // 数据获取后初始化图表
        } catch (error) {
          console.error("Error loading data:", error);
        } finally {
          this.isLoading = false;
        }
      },
      //
      initChart() {
        this.currentPage = 1;
  
        if (!this.cityList || this.cityList.length === 0) return;
        this.chart = echarts.init(this.$refs.chartDom, "idea");
  
        const option = {
          backgroundColor: "rgba(255, 255, 255, 0.1)",
          title: {
            text: "{text1|中国城市传播指数大数据分析}{text2|(综合分析结果)}",
            textStyle: {
              rich: {
                text1: {
                  color: "#ffffff", //标题颜色
                  fontSize: 16,
                },
                text2: {
                  color: "#ffffff", //标题颜色
                  fontSize: 12,
                },
              },
            },
            left: "center",
            zlevel: 1,
          },
          color: [
            "#3fb1e3",
            "#6be6c1",
            "#626c91",
            "#a0a7e6",
            "#c4ebad",
            "#96dee8",
          ],
          graph: {
            color: [
              "#3fb1e3",
              "#6be6c1",
              "#626c91",
              "#a0a7e6",
              "#c4ebad",
              "#96dee8",
            ],
          },
          tooltip: {
            trigger: "axis",
            axisPointer: {
              type: "cross",
              label: {
                backgroundColor: "#6be6c1", //鼠标移动颜色
              },
            },
          },
          legend: {
            data: [
              "网络传播影响力",
              "媒体报道影响力",
              "社交媒体影响力",
              "国际访客影响力",
              "搜索引擎影响力",
            ],
            top: "5%", //标注距离顶部的距离
          },
          toolbox: {
            feature: {
              saveAsImage: {},
            },
          },
          grid: {
            left: "3%",
            right: "4%",
            bottom: "3%",
            containLabel: true,
          },
  
          xAxis: [
            {
              type: "category",
              boundaryGap: false,
              // color:'#ffffff',
              data: this.cityList.map((city) => city.cityName), // 假设每个城市对象都有 cityName 属性
            },
          ],
          yAxis: [
            {
              type: "value",
            },
          ],
          series: [
            {
              name: "网络传播影响力",
              type: "line",
              stack: "总量",
              areaStyle: {},
              data: this.cityList.map((city) => city.network),
            },
            {
              name: "媒体报道影响力",
              type: "line",
              stack: "总量",
              areaStyle: {},
              data: this.cityList.map((city) => city.mediatr),
            },
            {
              name: "社交媒体影响力",
              type: "line",
              stack: "总量",
              areaStyle: {},
              data: this.cityList.map((city) => city.social),
            },
            {
              name: "国际访客影响力",
              type: "line",
              stack: "总量",
              areaStyle: {},
              data: this.cityList.map((city) => city.tourism),
            },
            {
              name: "搜索引擎影响力",
              type: "line",
              stack: "总量",
              label: {
                normal: {
                  show: true,
                  position: "top",
                },
              },
              areaStyle: {},
              data: this.cityList.map((city) => city.searchin),
            },
          ],
  
          // ...（其他图表配置）
        };
  
        this.chart.setOption(option);
      },
      // 取消选择
      toggleSelection() {
        this.cityList = this.allCityList;
        console.log("toggleSelection全部数据" + this.allCityList);
        this.fetchCityData(); // 在组件创建时调用数据获取方法
        this.initChart();
        this.$refs.multipleTable.clearSelection();
      },
      rowKey(row) {
        return row.cityName;
      },
      // 选中
      handleSelectionChange(val) {
        this.multipleSelection = val;
        this.selectedCity = this.multipleSelection.map((item) => item.cityName);
        console.log(this.selectedCity);
        console.log(typeof this.selectedCity); // "object"
      },
      showSelection() {
        console.log("lll", this.selectedCity);
        axios
          .post("http://localhost:82/index/evaluate", {
            cities: this.selectedCity, // 将selectedCity作为请求体的一部分发送
          })
          .then((response) => {
            // 处理成功的响应
            this.cityList = response.data.list;
            this.total = response.data.total;
            this.initChart(); // 数据获取后初始化图表
            console.log("Cities sent successfully", response.data);
          })
          .catch((error) => {
            // 处理请求错误
            console.error("Error sending cities:", error);
          });
      },
      handleSizeChange(val) {
        this.pageSize = val;
        this.currentPage = 1;
      },
      handleCurrentChange(val) {
        this.currentPage = val;
      },
    },
    beforeDestroy() {
      if (this.chart) {
        this.chart.dispose();
      }
    },
  };
  </script>
  <style lang="scss" scope>
  .evaluate {
    margin: 0;
    padding-top: 8%;
    display: grid;
    justify-content: center;
  background-color: #1e3c72; /* 深蓝色背景 */
  color: #ffffff; /* 白色文字 */
  font-family: "Arial", sans-serif; /* 简洁的字体 */
  }
  
  .jieshao {
    width: 1200px;
    text-indent: 4em;
    height: 150px;
    text-align: left;
    // padding: 20%;
    font-size: 20px;
    font-style: bold;
  }
  .echarts {
    width: 100%;
    height: 600px;
    margin-bottom: 3%;
  }
  // 表单外观样式
  .el-table {
    border-radius: 10px;
    padding: 1%;
    background: rgb(255, 255, 255, 0.1);
    box-shadow: 0 25px 45px rgb(0, 0, 0, 0.1);
    border-right: 1px solid rgb(255, 255, 255, 0.2);
    border-bottom: 1px solid rgb(255, 255, 255, 0.2);
  }
  .el-table td.el-table__cell,
  .el-table th.el-table__cell.is-leaf {
    background: rgb(44 118 204 / 77%);
  }
  .el-table__body tr:nth-child(even) {
    background: #1b4f8e; /* 偶数行（斑马线）的默认背景色 */
  }
  // 表格行
  .el-table td.el-table__cell,
  .el-table th.el-table__cell.is-leaf {
    border-bottom: 1px solid #93a1c0;
  }
  // 表格内容
  .el-table td.el-table__cell div {
    color: white;
    font-size: large;
  }
  // hover样式
  .el-table--enable-row-hover .el-table__body tr:hover > td {
    background-color: #133660 !important;
  }
  // 分页样式
  .el-pagination__total {
    color: white;
    font-size: 13px;
  }
  .el-pagination__jump {
    color: white;
  }
  .el-input__inner {
    background: rgba(255, 255, 255, 0);
  }
  .el-pagination__sizes .el-input .el-input__inner {
    color: white;
    border: none;
  }
  .el-pagination__editor.el-input .el-input__inner {
    border: none;
    color: white;
  }
  .el-pager li {
    background: rgba(255, 255, 255, 0);
  }
  .el-pager li.active {
    color: #133660;
  }
  .el-pagination button:disabled {
    background: rgba(255, 255, 255, 0);
  }
  .el-button {
    background: rgb(255, 255, 255, 0.1);
    border: none;
    color: white;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
      "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  }
  .el-button:focus,
  .el-button:hover {
    background: #133660;
  }
  // prev和next箭头不能点击的样式
  ::v-deep .el-pagination button:disabled {
    background-color: rgba(243, 119, 119, 0);
    color: gray;
  }
  .el-pagination .btn-next,
  .el-pagination .btn-prev {
    background-color: #13366000;
  }
  </style>
  