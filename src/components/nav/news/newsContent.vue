<template>
  <div class="all">
    <div class="card">
      <div class="newsContent">
        <!-- <el-button type="primary" icon="el-icon-arrow-left"></el-button> -->
        <router-link
          to="/index/news"
          style="display: flex; padding-top: 1%; padding-left: 2%"
          >返回</router-link
        >

        <div class="newsTitle">
          <h3>{{ city }}热点新闻</h3>
          <p style="text-align: left; text-indent: 2em; margin-top: 1%">
            关于数据来源， 网络传播影响力和社交媒体影响力数据来自google、
            抖音、微博等社交
            媒体平台，媒体报道影响力数据来自纽约时报，搜索引擎影响力数据源于谷歌趋势指数
            （Google Trends），国际访客影响力数据则取自官网出入境公开文件。<br /><br />
          </p>
        </div>

        <el-row style="height: 100%;">
          <!-- 布局左部 -->
            <el-col :span="18" class="leftcol" style="height: 850px">
              <div class="slid">
                <el-carousel indicator-position="outside">
                  <el-carousel-item v-for="item in imagesItems" :key="item">
                    <!-- <h3>{{ image.im }}</h3> -->
                    <img :src="item.imagesURL" alt="暂无图片" />
                  </el-carousel-item>
                </el-carousel>
              </div>

              <!-- <div class="video-container">
                <el-row :gutter="20">
                  <el-col :span="8" v-for="item in paginatedVideos" :key="item">
                    <div class="video-item">
                      <div class="video-image">
                        <img
                          @click="openVideoInNewTab(item.videoURL)"
                          :src="item.videoImageURL"
                          alt="视频封面"
                        />
                      </div>
                      <div class="video-title-container">
                        <div class="video-title">{{ item.videoTitle }}</div>
                      </div>
                    </div>
                  </el-col>
                </el-row>
              </div> -->
  <div class="video-container">
    <el-row :gutter="20">
      <el-col :span="12" v-for="(item, index) in paginatedVideos" :key="index">
        <div class="video-item">
          <div class="video-image">
            <img
              @click="openVideoInNewTab(item.videoURL)"
              :src="item.videoImageURL"
              alt="视频封面"
            />
          </div>
          <div class="video-title-container">
            <div class="video-title">{{ item.videoTitle }}</div>
          </div>
        </div>
      </el-col>

      <!-- 占位符，用于保持2x2布局 -->
      <el-col :span="12" v-for="n in emptySlots" :key="'empty-' + n">
        <div class="video-item placeholder">
          <!-- 留空，但保持与视频项相同的结构 -->
          <div class="video-image"></div>
          <div class="video-title-container"></div>
        </div>
      </el-col>
    </el-row>
  </div>

              <div class="page">
                <el-pagination
                  @size-change="handleVideoSizeChange"
                  @current-change="handleVideoCurrentChange"
                  :current-page="currentVideoPage"
                  :page-sizes="[4]"
                  :page-size="pageVideoSize"
                  layout="total, prev, pager, next"
                  :total="videoTotal"
                >
                </el-pagination>
              </div>
            </el-col>

          <!-- 布局右部 -->
          <!-- <el-col :span="6" id="newslist">
            <div class="listcontent">
              <el-table
                :data="compData"
                stripe
                id="newstable"
                :header-cell-style="{ background: '#16457c', color: 'white' }"
              >
                <el-table-column
                  prop="title"
                  label="新闻标题"
                  :formatter="formatTitle"
                  style="color: black"
                >
                  <template slot-scope="scope">
                    <a
                      :href="scope.row.newsURL"
                      target="_blank"
                      style="color: black"
                      class="news-link"
                    >
                      {{ scope.row.title }}
                    </a>
                  </template>
                </el-table-column>
              </el-table>
            </div>
            <div class="page">
              <el-pagination
                small
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page="currentPage"
                :page-sizes="[5, 10, 15, 20, 30, 50]"
                :page-size="pageSize"
                layout="total, sizes, prev, pager, next"
                :total="total"
              >
              </el-pagination>
            </div>
          </el-col> -->
<el-col style="width: 50%; height: 850px" id="newslist">
  <div class="listcontent" style="height: 850px; max-height: 850px; overflow-y: auto;">
    <!-- 直接使用 items 而不是 compData -->
    <el-table
      :data="items"  
      stripe
      id="newstable"
      :header-cell-style="{ background: '#16457c', color: 'white' }"
    >
      <el-table-column
        prop="title"
        label="新闻标题"
        :formatter="formatTitle"
        style="color: black"
      >
        <template slot-scope="scope">
          <a
            :href="scope.row.newsURL"
            target="_blank"
            style="color: black"
            class="news-link"
          >
            {{ scope.row.title }}
          </a>
        </template>
      </el-table-column>
    </el-table>
  </div>
</el-col>        
        </el-row>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
export default {
  data() {
    return {
      items: [], // 瀑布流数据
      videos: [],
      imagesItems: [], //轮播图数据
      currentPage: 1, //当前页数
      currentVideoPage: 1, //当前页数
      pageSize: 10, // 每页显示条数
      pageVideoSize: 4, // 每页显示条数
      total: 0, // 总条数
      videoTotal: 0, // 总条数
    };
  },
  props: ["city"], //传递路由参数
  created() {
    this.loadData();
  },
  computed: {
    compData() {
      return this.items.slice(
        (this.currentPage - 1) * this.pageSize,
        this.currentPage * this.pageSize
      );
    },
    paginatedVideos() {
      const start = (this.currentVideoPage - 1) * this.pageVideoSize;
      const end = start + this.pageVideoSize;
      return this.videos.slice(start, end);
    },
    emptySlots() {
      return this.paginatedVideos.length < 4 ? 4 - this.paginatedVideos.length : 0;
    }    
  },

  methods: {
    handleSizeChange(val) {
      this.pageSize = val;
      this.currentPage = 1;
    },

    handleCurrentChange(val) {
      this.currentPage = val;
    },
    // 处理每页条数变化
    handleVideoSizeChange(val) {
      this.pageVideoSize = val;
      this.currentVideoPage = 1; // 通常页码会重置为第一页
    },
    // 处理当前页码变化
    handleVideoCurrentChange(val) {
      this.currentVideoPage = val;
    },
    openVideoInNewTab(videoURL) {
      window.open(videoURL, "_blank");
    },
    async loadData() {
      try {
        const response = await axios.post(
          "http://localhost:8081/index/" + this.city
        );
        console.log(response);
        this.items = response.data.cityNewsList; // 假设后端返回的对象中有一个items数组
        this.videos = response.data.cityVideolist; // 假设后端返回的对象中有一个items数组
        this.imagesItems = response.data.cityImagesList;
        this.total = response.data.total;
        this.videoTotal = response.data.videoTotal;
      } catch (error) {
        console.error("Error loading data:", error);
      } finally {
        this.isLoading = false;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap");
.video-item {
  height: 200px; /* 设置统一的高度 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #f0f0f000; /* 背景色，可选 */
  border-radius: 15px;
}

.video-image {
  width: 100%;
  height: 80%;
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  overflow: hidden;
}

.video-image img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover; /* 保持图片覆盖整个容器 */
  cursor: pointer;
  border-radius: 15px;
}

.video-title-container {
  width: 100%;
  text-align: center;
  background-color: #0074c700;
  color: white;
  margin-top: 5px;
}

.video-title {
  font-size: 14px;
}

.placeholder {
  visibility: hidden; /* 使占位符不可见但保持空间 */
}

* {
  margin: 0;

  padding: 0;
  box-sizing: border-box;
  // font-family: "Poppins", sans-serif;
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  color: white;
  // 整体背景
  .all {
    background: linear-gradient(#040228 0%, #0075c7 40%);
    min-height: 100vh;
    padding: 10%;
    /* overflow: hidden; */
  }

  //   内容
  .card {
    // background-color: rgb(189, 73, 73);
    background: rgb(255, 255, 255, 0.1);

    margin: 2%;
    // background: #75ad73ab;

    border-radius: 10px;
    // display: flex;
    // justify-content: center;
    align-items: center;
    backdrop-filter: blur(5px);
    box-shadow: 0 25px 45px rgb(0, 0, 0, 0.1);
    // border: 1px solid rgb(255, 255, 255, 0.5);
    border-right: 1px solid rgb(255, 255, 255, 0.2);
    border-bottom: 1px solid rgb(255, 255, 255, 0.2);
  }
  * #newstable[data-v-07a0a166] {
    background-color: rgba(0, 0, 0, 0);
    border: none;
  }
  .newsContent {
    padding: 1%;
    margin: 2%;
    background-color: #02315bab;
  }
  .newsTitle {
    // width: 100%;
    height: 20%;
    background-color: rbg(102 121 138 / 0%);
    margin: 1%;
  }
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  // 轮播图背景
  .bg-purple {
    background: #16457c;
  }
  // 表单外颜色
  #newslist {
    background: #1e356a;
  }
  .listcontent {
    padding: 2%;
  }
  .slid {
    padding: 1%;
  }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #2765bd;
  }

  .el-carousel__item:nth-child(2n + 1) {
    background-color: #28578c;
  }
  .el-pagination {
    position: relative;
  }
  // 表单样式
  #newstable {
    background-color: #932121;
    /* 自定义表格边框颜色 */
    border: 1px solid #4262ad;
    width: 100%;
    color: rgb(0, 0, 0);
  }

  .news-link:hover {
    color: #66b1ff;
  }
  // .video {
  //   display: flex;
  //   height: 100%;
  //   padding: 2%;
  //   justify-content: space-between; /* 子元素之间的间隔相等 */
  //   /* 或者使用 space-around 如果希望首尾两边也有空间 */
  // }
  .video-container {
    // margin-bottom: 20px;  s
  }

  .video-item {
    position: sticky;
    // height: 13vh; /* 使用padding-top hack保持正方形 */
    width: initial;
    // padding-top: 100%; /* 高度是宽度的100%，即正方形 */
    overflow: hidden;
    background-color: #f0f0f000; /* 背景色，可选 */
  }
  // * .video-title[data-v-07a0a166]{
  //   overflow: hidden;

  // }

  .video-image {
    // position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 80%;
    display: flex;
    align-items: center; /* 垂直居中 */
    justify-content: center; /* 水平居中 */
    overflow: hidden;
  }

  .video-image img {
    max-width: 100%;
    max-height: 100%;
    object-fit: cover; /* 保持图片覆盖整个容器 */
    cursor: pointer;
    border-radius: 15px;
    margin-bottom: 0%;
    margin-top: 0%;
  }
  .video-title-container {
    width: 100%; /* 或其他适合您设计的宽度 */
    overflow: hidden;
    white-space: nowrap;
    background-color: #0074c700;
    position: relative;
  }
  .video-title {
    // position: absolute;
    top: 89px;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 20px;
    background-color: rgba(0, 0, 0, 0); /* 半透明背景 */
    color: white;
    text-align: center;
    // padding: 5px 0;
    // margin-top: 105px;
    font-size: 14px; /* 或您希望的字体大小 */

    white-space: nowrap; /* 防止文本换行 */
    // overflow: hidden; /* 隐藏超出容器的部分 */
    box-sizing: border-box;
    // position: relative;
    line-height: 20px; /* 保持文本垂直居中 */
    animation: none; /* 应用动画，持续时间、速度和循环次数 */
  }
  .video-title-container:hover .video-title {
    /* 当鼠标悬停时，应用动画 */
    animation: scrollText 10s linear forwards; /* forwards表示动画完成后保留最后一帧的状态 */
  }
  @keyframes scrollText {
    0% {
      transform: translateX(0);
    }
    100% {
      /* 根据文本长度和容器宽度调整这个值，以确保文本能够完全滚动过去 */
      /* 注意：这里是一个简化的示例，实际中您可能需要动态计算这个值 */
      transform: translateX(-100%); /* 假设文本足够长，可以滚动整个容器的宽度 */
    }
  }
  .leftcol {
    background-color: #1e356a;
    padding: 1%;
  }
  .left {
    background: beige;
    width: 100%;
    height: 100%;
  }
  .center {
    background-color: rgb(165, 165, 68);
    width: 100%;
    height: 100%;
  }
  .right {
    background-color: beige;
    width: 100%;
    height: 100%;
  }
  .el-pagination {
    background-color: #f0f2f5;
    // padding: 2%;
    margin: 2%;
    .el-input__inner {
      height: 100%;
    }
    .el-pager li {
      color: #040228;
    }
  }
  * .el-col[data-v-07a0a166] {
    width: 50%;
  }
  .el-col el-col-8 {
    padding-left: 0%;
    padding-right: 0%;
  }
  .el-table .cell {
    text-align: center;
  }
  // 设置表头内容居中
  ::v-deep .el-table th.el-table__cell > .cell {
    text-align: center;
    font-weight: bold;
    font-size: 25px;
  }

  ::v-deep .el-table td.el-table__cell div {
    text-align: left;
    font-weight: bold;
    //  background-color: #16467c6a;
  }
  ::v-deep .el-table--enable-row-transition .el-table__body td.el-table__cell {
    background-color: #2fa3f6ad;
  }
  ::v-deep
    .el-table--striped
    .el-table__body
    tr.el-table__row--striped
    td.el-table__cell {
    background-color: #1a519dad;
  }
  ::v-deep .el-table__body tr.hover-row.current-row > td,
  .el-table__body tr.hover-row.el-table__row--striped.current-row > td,
  .el-table__body tr.hover-row.el-table__row--striped > td,
  .el-table__body tr.hover-row > td {
    background-color: red;
  }
  ::v-deep .el-input--mini .el-input__inner {
    height: 100%;
  }
  ::v-deep .el-pagination__total {
    color: white;
    // font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",
    //   sans-serif;
  }

  .el-pagination[data-v-07a0a166] {
    background-color: #0074c700;
  }
  ::v-deep .el-pagination .el-select .el-input {
    background-color: #0074c700;
  }
  ::v-deep .el-pagination .el-select .el-input .el-input__inner {
    background-color: #0074c700;
    border: none;
    color: aliceblue;
  }
  ::v-deep .el-pagination button:disabled {
    background-color: #0074c700;
  }
  ::v-deep .el-pager li.active {
    background-color: #0074c700;
  }
  ::v-deep .el-pager li {
    background-color: #0074c700;
  }

  .el-pagination .btn-next,
  .el-pagination .btn-prev {
    background: #0074c700;
  }
  * .el-carousel__item[data-v-07a0a166]:nth-child(2n + 1) {
    background-color: #28578c00;
  }
  * .el-carousel__item[data-v-07a0a166]:nth-child(2n) {
    background-color: #28578c00;
  }

  ::v-deep .el-pagination .btn-next,
  ::v-deep .el-pagination .btn-prev {
    background: r !important;
    background-color: rgba(243, 119, 119, 0);
    color: white;
  }
  // prev和next箭头不能点击的样式
  ::v-deep .el-pagination button:disabled {
    background-color: rgba(243, 119, 119, 0);
    color: gray;
  }
  // 页码样式
  ::v-deep .el-pager li {
    background-color: transparent !important;
  }
  // active的页码样式
  ::v-deep .el-pager li.active {
    color: #4069ab !important;
  }
  ::v-deep {
    .is-horizontal {
        height: 0px;
        left: 0px;
        display: none;
    }
 
    ::-webkit-scrollbar-thumb {
        background-color: #2a169b;
    }
}
}
</style>
