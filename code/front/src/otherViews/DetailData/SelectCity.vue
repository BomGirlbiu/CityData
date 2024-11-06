<template>
  <div class="linkage">
    <div>
      <el-select
        v-model="selectProvince"
        filterable
        size="small"
        @change="selectProvinceFun($event)"
        placeholder="请选择省份"
      >
        <el-option value="" label="请选择省份"></el-option>
        <el-option
          :value="item"
          :label="item.label"
          v-for="(item, index) in city"
          :key="index"
        ></el-option>
      </el-select>
    </div>
    <div>
      <el-select
        v-model="selectCity"
        filterable
        size="small"
        @change="selectCityFun($event)"
        placeholder="请选择城市"
      >
        <el-option value="" label="请选择城市"></el-option>
        <el-option
          :value="item"
          :label="item.label"
          v-for="(item, index) in cityList"
          :key="index"
        ></el-option>
      </el-select>
    </div>
    <div>
      <!-- <el-select
        v-model="selectArea"
        filterable
        size="small"
        @change="selectAreaFun($event)"
        placeholder="请选择区县"
      >
        <el-option value="" label="请选择区县"></el-option>
        <el-option
          :value="item"
          :label="item.label"
          v-for="(item, index) in areaList"
          :key="index"
        ></el-option>
      </el-select> -->
    </div>
    <el-button
      @click="sendCityToParent"
      size="small"
      icon="el-icon-search"
      circle
    ></el-button>
  </div>
</template>
<script>
import city from "../../assets/json/city.json";
export default {
  name: "linkage",
  data() {
    return {
      // 整个省市县数据
      city: city,
      // 被选中的市数据
      cityList: [],
      // 被选中的县数据
      areaList: [],
      selectProvince: {},
      selectCity: { children: [], label: "北京城区", value: "110100" },
      selectArea: {},
    };
  },
  mounted() {},
  methods: {
    sendCityToParent() {
      this.$emit("citydata", this.selectCity.label);
    },
    // 省份 市 县联动
    selectProvinceFun(event) {
      console.log(event);
      if (event) {
        this.cityList = event.children;
      } else {
        this.cityList = [];
      }
      this.areaList = [];
      this.$emit("getLawyerListInfo", [event.label, "province"]);
    },
    selectCityFun(event) {
      console.log(event);
      if (event) {
        this.areaList = event.children;
      } else {
        this.areaList = [];
      }
      this.$emit("getLawyerListInfo", [event.label, "city"]);
    },
    selectAreaFun(event) {
      console.log(event);
      this.$emit("getLawyerListInfo", [event.label, "area"]);
    },
  },
};
</script>
<style lang="scss" scoped>
.linkage {
  display: flex;
  div {
    margin-right: 5px;
  }
}
</style>
