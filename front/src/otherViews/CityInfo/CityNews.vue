<template>
  <div class="city-news">
    <!-- 新页面的内容 -->
    <div class="news-header">
      <div class="bar">
        <nav-item />
      </div>
      <div class="channel">
        <el-button
          v-for="(btnText, index) in this.buttonData"
          :key="index"
          @click="showCityInfo(btnText)"
        >
          {{ btnText }}
        </el-button>
      </div>
    </div>
    <div class="news-body">
      <div class="middle">
        <div class="title">
          <h1>{{this.currentCity}}</h1>
        </div>
        <el-row style="height: 100%">
          <el-col :span="16" class="leftcol" style="height: 650px">
            <div class="slid">
              <el-carousel indicator-position="outside" height="580px">
                <el-carousel-item
                  v-for="item in this.imagesItems"
                  :key="item.imagesURL"
                >
                  <img
                    :src="item.imagesURL"
                    style="width: 100%; height: 100%"
                    alt="暂无图片"
                  />
                </el-carousel-item>
              </el-carousel>
            </div>
          </el-col>
          <el-col style="width: 30%; height: 650px" id="newslist">
            <div
              class="listcontent"
              style="height: 600px; max-height: 850px; overflow-y: auto"
            >
              <!-- 直接使用 items 而不是 compData -->
              <el-table
                :data="items"
                stripe
                id="newstable"
                :header-cell-style="{ background: 'white', color: 'white' }"
              >
                <el-table-column
                  prop="title"
                  label="新闻标题"
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
        <div class="grid">
          <div class="sub-grid sub-grid-1">
            <article class="card">
              <figure>
                <img
                  width="1600"
                  height="900"
                  src="https://assets.codepen.io/162656/beach2.jpg"
                  alt=""
                />
                <figcaption>
                  <div>
                    Santorini, Greece
                    <span
                      >by
                      <a
                        href="https://unsplash.com/photos/white-sun-lounger-lot-KrGbdPfIYD4"
                        target="_blank"
                        >Khamkéo</a
                      >
                    </span>
                  </div>
                </figcaption>
              </figure>
            </article>
            <article class="card">
              <figure>
                <img
                  width="1600"
                  height="1067"
                  src="https://assets.codepen.io/162656/beach6.jpg"
                  alt=""
                />
                <figcaption>
                  <div>
                    Kvalvika Beach, Moskenes, Norway
                    <span
                      >by
                      <a
                        href="https://unsplash.com/photos/beach-near-mountain-range-wnRvXXzZK7w"
                        target="_blank"
                      ></a
                      >Martine Jacobsen
                    </span>
                  </div>
                </figcaption>
              </figure>
            </article>
            <article class="card">
              <figure>
                <img
                  width="1600"
                  height="1036"
                  src="https://assets.codepen.io/162656/beach3.jpg"
                  alt=""
                />
                <figcaption>
                  <div>
                    San Lorenzo, Italy
                    <span
                      >by
                      <a
                        href="https://unsplash.com/photos/photo-of-seashore-d7M5Xramf8g"
                        target="_blank"
                        >Camille Minouflet</a
                      >
                    </span>
                  </div>
                </figcaption>
              </figure>
            </article>
          </div>
          <article class="card">
            <figure>
              <img
                width="1600"
                height="900"
                src="https://assets.codepen.io/162656/beach4.jpg"
                alt=""
              />
              <figcaption>
                <div>
                  McWay Falls, California, USA
                  <span
                    >by
                    <a
                      href="https://unsplash.com/photos/aerial-photography-of-boulders-on-body-of-water-07mSKrzKiRw"
                      target="_blank"
                      >Chor Tsang</a
                    >
                  </span>
                </div>
              </figcaption>
            </figure>
          </article>
          <div class="sub-grid sub-grid-2">
            <article class="card">
              <figure>
                <img
                  width="1600"
                  height="1064"
                  src="https://assets.codepen.io/162656/beach5.jpg"
                  alt=""
                />
                <figcaption>
                  <div>
                    Inisheer, County Galway, Ireland
                    <span
                      >by
                      <a
                        href="https://unsplash.com/photos/a-beach-with-a-boat-on-it-and-people-walking-on-it-Il4WLGeMsUk"
                        target="_blank"
                        >Ulrike R. Donohue</a
                      >
                    </span>
                  </div>
                </figcaption>
              </figure>
            </article>
            <article class="card">
              <figure>
                <img
                  width="1600"
                  height="898"
                  src="https://assets.codepen.io/162656/beach1.jpg"
                  alt=""
                />
                <figcaption>
                  <div>
                    Beaches, Jacksonville Beach, Florida, United States
                    <span
                      >by
                      <a
                        href="https://unsplash.com/photos/man-surfing-on-waves-L5aI2jU0i50"
                        target="_blank"
                        >Lance Asper</a
                      >
                    </span>
                  </div>
                </figcaption>
              </figure>
            </article>
          </div>
        </div>
      </div>
    </div>
    <div class="news-video">
      <ul class="video-cards">
        <li
          class="video-cards_item"
          v-for="(item, index) in this.videos"
          :key="index"
        >
          <div class="video-card">
            <div class="video-card_image">
              <img
                @click="openVideoInNewTab(item.videoURL)"
                :src="item.videoImageURL"
                alt="视频封面"
              />
            </div>
            <div class="video-card_content">
              <h2 class="video-card_title">{{ item.videoTitle }}</h2>
              <button class="btn card_btn">Read More</button>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavItem from "../NavItem.vue";
export default {
  name: "CityNews",
  components: {
    NavItem,
  },
  data() {
    return {
      currentCity: "", //
      buttonData: [],
      items: [], // 瀑布流数据
      videos: [],
      imagesItems: [], //轮播图数据
      currentPage: 1, //当前页数
      pageSize: 10, // 每页显示条数
      total: 0, // 总条数
      videoTotal: 0, // 总条数
    };
  },
  created() {
    this.loadButton();
  },
  methods: {
    openVideoInNewTab(url) {
      window.open(url, "_blank");
    },
    // 加载城市信息
    async loadData() {
      try {
        const response = await axios.post(
          "http://localhost:8081/CityNews/" + this.currentCity
        );
        console.log(response);
        console.log( "http://localhost:8081/CityNews/" + this.currentCity);

        this.items = response.data.cityNewsList; // 假设后端返回的对象中有一个items数组
        this.videos = response.data.cityVideolist; // 假设后端返回的对象中有一个items数组
        this.imagesItems = response.data.citySliderList;
        console.log(this.imagesItems);
        this.total = response.data.cityNewsListTotal;
        this.videoTotal = response.data.videoTotal;
      } catch (error) {
        console.error("Error loading data:", error);
      } finally {
        this.isLoading = false;
      }
    },
    // 加载城市按钮选项
    async loadButton() {
      try {
        const response = await axios.get(
          "http://localhost:8081/CityNews/" + this.$store.state.currentProvince
        );
        this.buttonData = response.data;
        this.currentCity = this.buttonData[0];
        this.loadData();
        console.log(this.currentCity)
      } catch (error) {
        console.error("Error loading data:", error);
      } finally {
        this.isLoading = false;
      }
    },
    // 点击按钮实现切换城市信息
    showCityInfo(btnText) {
      this.currentCity = btnText;
      this.loadData();
    },
  },
};
</script>
<style lang="scss" scope>

// 背景颜色
body {
  font-family: "Quicksand", serif;
  font-style: normal;
  font-weight: 400;
  letter-spacing: 0;
  // padding: 1rem;
  background: linear-gradient(
    to right,
    rgb(173, 169, 150),
    rgb(242, 242, 242),
    rgb(219, 219, 219),
    rgb(234, 234, 234)
  );
   box-sizing: border-box;
}

.city-news {
  height: 100%;
  width: 100%;
}
.news-header {
  height: 100px;

  // 标题
  .bar {
    width: 100%;
    position: absolute;
    background-color: rgba(255, 255, 255, 0.486);
    z-index: 2; /* 设置较高的z-index值 */
    .title h1 {
      font-family: "chenguangrong";
    }
    .user {
      float: right;
      margin-right: 50px;
    }
  }
  // channel
  .channel {
    position: relative;
    margin-top: 120px;
  }
}
.news-body {
  margin-left: 60px;
  margin-right: 60px;
}
.news-video {
  margin-top: 30px;
  margin-left: 60px;
  margin-right: 60px;
}

// 表单外颜色
#newslist {
  background: #ffffff;
}
.listcontent {
  padding: 2%;
}
.slid {
  padding: 1%;
  height: 600px;
}
.el-carousel__item.is-active {
  z-index: 0;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}

// 表单样式
#newstable {
  border: 2px solid #000000;
  width: 100%;
}
// 轮播图背景
.leftcol {
  background: linear-gradient(to bottom left, #8e9eab 40%, #eef2f3 100%);

  padding: 1%;
  margin-left: 2%;
}
// 设置表格内容居中
.el-table .cell {
  text-align: left;
}

// 标题样式
.middle-title {
  width: 100%;
  height: 130px;
}

// 组件
/* RESET STYLES
–––––––––––––––––––––––––––––––––––––––––––––––––– */
@import url("https://fonts.googleapis.com/css2?family=Bitter:ital,wght@0,100..900;1,100..900&display=swap");

:root {
  --height: 50vh; //修改高度
  --half-height: calc(var(--height) / 2);
  --transition: all 1s;
}
a {
  color: inherit;
}
.notification {
  display: none;
  position: absolute;
  top: 0;
  right: 0;
  padding: 10px;
  font-size: 0.85em;
  background: #e9c46a;
}

/* MAIN STYLES
–––––––––––––––––––––––––––––––––––––––––––––––––– */
.grid,
.sub-grid,
.grid .card {
  transition: var(--transition);
}

.grid {
  max-width: 100%;
  margin: 30px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.35);
}

.card {
  cursor: pointer;

  figure,
  img {
    width: 100%;
    height: 100%;
  }

  figure {
    position: relative;
    margin: 0;
    overflow: hidden;
  }

  img {
    object-fit: cover;
    background: #333;
  }

  figcaption {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: grid;
    place-items: center;
    font-size: 1.5em;
    line-height: 1.3;
    text-align: center;
    padding: 10px;
    color: white;
    background: rgba(0, 0, 0, 0.5);

    span {
      display: block;
      font-size: 0.75em;
    }
  }
}

@media (max-width: 899px) {
  .card {
    height: var(--half-height);
  }
}

@media (min-width: 900px) {
  .grid,
  .sub-grid {
    display: grid;
  }

  .grid {
    grid-template-columns: 2fr 1fr 1fr;
  }

  .sub-grid {
    grid-template-rows: var(--half-height) var(--half-height);
  }

  .sub-grid-1 {
    grid-template-columns: 1fr 1fr auto;
  }

  .sub-grid-1 .card:last-child {
    grid-column: 1/-1;
  }

  /*.sub-grid-2 {
    grid-template-columns: 1fr;
  }*/

  .grid > .card {
    height: var(--height);
  }
}

@media (hover: hover) and (min-width: 900px) {
  .notification {
    display: block;
  }

  .grid:has(.sub-grid-1 .card:first-of-type:hover) .sub-grid-1 {
    grid-template-columns: 1fr 0fr auto;
  }

  .grid:has(.sub-grid-1 .card:nth-of-type(2):hover) .sub-grid-1 {
    grid-template-columns: 0fr 1fr auto;
  }

  .grid:has(.sub-grid-1 .card:last-of-type:hover) .sub-grid-1 {
    grid-template-rows: 0 var(--height);
  }

  .grid:has(> .card:hover) {
    grid-template-columns: 0fr 1fr 0fr;
  }

  .grid:has(.sub-grid-2 .card:first-of-type:hover) .sub-grid-2 {
    grid-template-rows: var(--height) 0;
  }

  .grid:has(.sub-grid-2 .card:last-of-type:hover) .sub-grid-2 {
    grid-template-rows: 0 var(--height);
  }

  .card {
    filter: grayscale(1);

    figcaption {
      opacity: 0;
    }

    &:hover {
      filter: grayscale(0);

      figcaption {
        opacity: 1;
        transition: opacity 0.5s 0.5s;
      }
    }
  }
}

/* FOOTER STYLES
–––––––––––––––––––––––––––––––––––––––––––––––––– */
.page-footer {
  position: fixed;
  right: 0;
  bottom: 50px;
  display: flex;
  align-items: center;
  padding: 5px;
  font-size: 0.9em;
  background: white;
}

.page-footer a {
  display: flex;
  margin-left: 4px;
}

// 网格布局
/* Font */
@import url("https://fonts.googleapis.com/css?family=Quicksand:400,700");



.main {
  max-width: 1200px;
  margin: 0 auto;
}

h1 {
  font-size: 24px;
  font-weight: 400;
  text-align: center;
}

img {
  height: auto;
  max-width: 100%;
  vertical-align: middle;
}

.btn {
  color: #ffffff;
  padding: 0.8rem;
  font-size: 14px;
  text-transform: uppercase;
  border-radius: 4px;
  font-weight: 400;
  display: block;
  width: 100%;
  cursor: pointer;
  border: 1px solid rgba(255, 255, 255, 0.2);
  background: transparent;
}

.btn:hover {
  background-color: rgba(188, 105, 105, 0.12);
}

.video-cards {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  margin: 0;
  padding: 0;
}

.video-cards_item {
  display: flex;
  padding: 1rem;
}

@media (min-width: 40rem) {
  .video-cards_item {
    width: 50%;
  }
}

@media (min-width: 56rem) {
  .video-cards_item {
    width: 33.3333%;
  }
}

.video-card {
  background: linear-gradient(to bottom left, #8e9eab 40%, #eef2f3 100%);

  border-radius: 0.25rem;
  box-shadow: 0 20px 40px -14px rgba(0, 0, 0, 0.25);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.video-card_content {
  padding: 1rem;
  background: linear-gradient(to bottom left, #8e9eab 40%, #eef2f3 100%);
}

.video-card_title {
  color: #ffffff;
  font-size: 1.1rem;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: capitalize;
  margin: 0px;
}

.video-card_text {
  color: #ffffff;
  font-size: 0.875rem;
  line-height: 1.5;
  margin-bottom: 1.25rem;
  font-weight: 400;
}
.made_by {
  font-weight: 400;
  font-size: 13px;
  margin-top: 35px;
  text-align: center;
}
</style>