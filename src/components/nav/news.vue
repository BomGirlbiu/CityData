<template>
  <div class="news">
    <div class="jieshao">
        {{text}}
    </div>

    <el-form :inline="true" :model="formInline" class="demo-form-inline">
      <el-form-item prop="province">
        <el-input
          v-model="formInline.province"
          @input="changeMessage"
          placeholder="输入查询省份"
        ></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">查询</el-button>
      </el-form-item>
    </el-form>
    <div class="waterfall">
      <div class="waterfall-item" v-for="(item, index) in items" :key="index">
        <div class="waterfall-content">
          <router-link
            :to="{ path: '/index/' + item.city }"
            style="color: rgb(236 236 255); font-size: 20px"
            >{{ item.city }}</router-link
          >
          <div class="content">
            <el-card class="hover-shadow" shadow="never">
              <div class="demo-image">
                <!-- <span class="demonstration">{{ item.city }}</span> -->
                <el-image
                  style="width: 400px; height: 300px; margin: 2px"
                  :src="item.imagesURL"
                  @click="goToCity(item.city)"
                ></el-image>
              </div>
            </el-card>
          </div>
        </div>
      </div>
      <div v-if="isLoading" class="loading-text">加载中...</div>
    </div>
  </div>
</template>
 
<script>
import axios from "axios";
export default {
  data() {
    return {
      titleText:
        "中国城市众多，各具特色。根据中国统计年鉴，不计港澳台地区， 我国共有4个直辖市、15个副省级市、278个普通地级市、388个县级市， 共计685个城市。 在这685个城市里，只有105个大城市按行政级别可分为直辖市、副省级城市、省会城市、地级市、县级市等。 该页面您可以查看到中国的绝大多数城市近期相关情报。 中国城市将继续在经济发展、文化繁荣、科技创新和生态保护等方面取得新的成就。随着“一带一路”倡议的推进和全球经济的深度融合， 中国城市将更加开放包容，与世界各地的城市加强交流与合作，共同推动全球经济的繁荣与发展。",
      index: 0,
      text: '',
      formInline: {
        province: "湖南省", //默认显示
      },
      columnWidth: 200, // 列宽
      columnNum: 3, // 列数
      items: [], // 瀑布流数据
      isLoading: false, // 是否正在加载
      page: 1, // 当前页
      pageSize: 10, // 每页数据量
    };
  },
  created() {
    this.loadData();
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeDestroy() {
    // 修正生命周期钩子，通常使用beforeDestroy而不是destroyed
    window.removeEventListener("scroll", this.handleScroll);
  },
  mounted() {
    setInterval(() => {
      this.autoTyping()
    }, 30);
  },
  methods: {
    autoTyping() {
      this.index ++
      this.text = this.titleText.slice(0, this.index);
    },
    onSubmit() {
      console.log("submit!");
      this.loadData();
    },
    changeMessage() {
      this.$forceUpdate();
    },
    goToCity(city) {
      this.$router.push({ path: `/index/${city}` });
    },
    async loadData() {
      if (this.isLoading) return;
      try {
        this.isLoading = true;
        const response = await axios.get(
          "http://localhost:8081/index/news/" + this.formInline.province
        );
        console.log(response);
        this.items = response.data;
      } catch (error) {
        console.error("Error loading data:", error);
      } finally {
        this.isLoading = false;
      }
    },
    handleScroll() {
      const { scrollTop, scrollHeight, clientHeight } =
        document.documentElement;
      const scrollBottom = scrollHeight - clientHeight - scrollTop;
      if (scrollBottom < 50 && !this.isLoading) {
        this.loadData();
      }
    },
  },
};
</script>
 
<style lang="scss" scoped>
.news {
  padding-top: 3%;
  color: #d3d3d3;
  .jieshao {
    // padding-bottom: 2%;
    position: relative;
    // padding-left: 10%;
    // padding-right: 10%;
    text-indent: 4em;
    text-align: left;
    width: 80%;
    height: 100px;
    margin-left: 10%;
    margin-right: 10%;
    margin-top: 2%;
    margin-bottom: 2%;
  }
  // 输入框
  ::v-deep .el-input__inner {
    background-color: rgb(255, 255, 255, 0.1);
    border: 0px solid rgba(255, 255, 255, 0.5);
    color: azure;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
      "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  }
  .el-button--primary {
    background-color: rgba(4, 67, 143, 0.549);
    border-color: rgb(255, 255, 255, 0.1);
  }
  .el-button--primary:focus,
  .el-button--primary:hover {
    background: #031e4f;
  }
  .waterfall {
    position: relative;
    margin-left: 10%; /* 列间隔的一半，这里以200px列宽为例 */
  }
  .waterfall-item {
    float: left;
    width: 421px;
    margin-left: 1%; /* 列间隔的一半 */
    margin-bottom: 10px; /* 列间距 */
  }
  .waterfall-content {
    border: 1px solid rgba(255, 255, 255, 0.5);
    border-right: 1px solid rgba(255, 255, 255, 0.2);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);

    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 5px; /* 列内间距 */
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.1);
  }
  .loading-text {
    text-align: center;
    margin-top: 10px;
  }
  .hover-shadow {
    margin: 5%;
    background: rgba(255, 255, 255, 0.1);
    border: 0px solid rgba(255, 255, 255, 0.5);
    color: #dae7ff;
  }
  .hover-shadow:hover {
    box-shadow: 0 2px 12px 0 rgb(255, 255, 255);
    // box-shadow: 0 2px 12px 0 rgb(0, 3, 91);
  }
  .el-card__body,
  .el-main {
    padding: 1%;
    height: 200px;
  }
}
</style>