<template>
  <div class="visualpage">
    <div class="select-city">
      <el-cascader
        size="large"
        :options="pcTextArr"
        v-model="selectedOptions"
        @change="handleChange"
      >
      </el-cascader>
      <!-- <select v-model="selectedCity" class="selectcity">
        <option disabled value="">请选择城市...</option> -->
      <!-- <option value="全国">全国</option> -->
      <!-- <option
          v-for="city in citydata"
          :key="city.cityId"
          :value="city.cityName"
        >
          {{ city.cityName }}
        </option> -->
      <!-- 可以根据需要添加更多城市选项 -->
      <!-- </select> -->
    </div>
    <div class="grid-container">
      <SearchEngine :selectedCity="selectedCity" class="grid-item" />
      <Conclusion :selectedCity="selectedCity" class="grid-item" />
      <SocialMedia :selectedCity="selectedCity" class="grid-item" />
      <NationTourism :selectedCity="selectedCity" class="grid-item" />
      <NetworkTrans :selectedCity="selectedCity" class="grid-item" />
      <MediaReport :selectedCity="selectedCity" class="grid-item" />
    </div>
    <!-- <div v-else class="chinaMap">
      <ChinaMap :selectedCity="selectedCity" />
    </div> -->
  </div>
</template>

<script>
// 具体可查看element-china-area-data的readme文档
import {
  provinceAndCityData,
  // pcTextArr,
  // regionData,
  // pcaTextArr,
  CodeToText,
} from "element-china-area-data";
import { pcTextArr } from "element-china-area-data";

import axios from "axios";
import SearchEngine from "../visualization/SearchEngine.vue";
import SocialMedia from "../visualization/SocialMedia.vue";
import NationTourism from "../visualization/NationTourism.vue";
import Conclusion from "../visualization/Conclusion.vue";
import NetworkTrans from "../visualization/NetworkTrans.vue";
// import ChinaMap from "../visualization/ChinaMap.vue";
import MediaReport from "../visualization/MediaReport.vue";
export default {
  name: "visual",
  components: {
    SearchEngine,
    SocialMedia,
    NationTourism,
    Conclusion,
    NetworkTrans,
    // ChinaMap,
    MediaReport,
  },
  data() {
    return {
      options: provinceAndCityData,
      selectedOptions: [],
      pcTextArr,
      selectedCity: "广州",
    };
  },
  watch: {
    selectedOptions: function (newVal, oldVal) {
      let newStr = newVal[1].substring(0, newVal[1].length - 1);
      if (newVal[0] == "北京市") {
        this.selectedCity = "北京";
      } else if (newVal[0] == "天津市") {
        this.selectedCity == "天津";
      } else if (newVal[0] == "重庆市") {
        this.selectedCity == "重庆";
      } else if (newVal[0] == "上海市") {
        this.selectedCity == "上海";
      } else {
        this.selectedCity = newStr;
      }
    },
  },

  created() {
    // this.getcities();
    this.selectedOptions = ["广东省", "广州市"];
  },
  methods: {
    handleChange() {
      var loc = "";
      for (let i = 0; i < this.selectedOptions.length; i++) {
        loc += CodeToText[this.selectedOptions[i]];
      }
      console.log(loc); //打印区域码所对应的属性值即中文地址
    },
    // ifnation() {
    //   if (this.selectCity == "全国") {
    //     return true;
    //   } else {
    //     return false;
    //   }
    // },
    // async getcities() {
    //   try {
    //     const response = await axios({
    //       url: "http://localhost:8081/index/visual",
    //       method: "get",
    //       // params: {
    //       //   getcityform: "getcityform",
    //       // },
    //     });
    //     this.citydata = response.data;
    //     // console.log(this.citydata);
    //     console.log(response.data);
    //   } catch (error) {
    //     console.error("Error:", error);
    //   }
    // },
  },
};
</script>

<style>
.el-cascader {
  width: 300px;
}
.visualpage {
  margin-top: 0;
  padding-top: 8%;
  display: grid;
  justify-content: center;
}

/* .select-city {
  /* 为下拉框容器设置样式（如果需要的话） 
} */

.selectcity {
  /* 下拉框的样式 */
  width: 300px; /* 宽度可以根据需要调整 */
  padding: 8px; /* 添加一些内边距以提高可读性 */
  border: 1px solid #ccc; /* 边框样式 */
  border-radius: 4px; /* 边框圆角 */
  /* background-color: #2e4f85; */
  /* text-align: center; */
  /* color: white; */
}
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 创建三列 */
  grid-auto-rows: minmax(
    100px auto
  ); /* 设置行高为至少100px，但可以根据内容自动调整 */
  grid-gap: 10px; /* 网格项之间的间隔 */
  padding: 10px; /* 容器内边距 */
}

.grid-item {
  /* 网格项的样式，可以根据需要自定义 */
  background-color: #f9f2eb;
  /* 边框：1px 实线 浅灰色 */
  border: 1px solid #d1c7bd;

  /* 圆角 */
  border-radius: 5px;

  /* 阴影 */
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);

  /* 内边距 */
  padding: 15px;

  /* 文本对齐和颜色 */
  text-align: left;
  color: #333;

  /* 字体样式（可选） */
  font-family: Arial, sans-serif;
  font-size: 16px;

  /* 边缘自动换行（如果需要） */
  margin: 10px auto;

  /* 可选：悬停效果 */
  transition: transform 0.2s ease;
  cursor: pointer;
  max-width: 490px;
  height: 360px;
}
.grid-item:hover {
  /* 悬停时稍微放大并降低阴影 */
  transform: scale(1.05);
  box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.15);
}
</style>
