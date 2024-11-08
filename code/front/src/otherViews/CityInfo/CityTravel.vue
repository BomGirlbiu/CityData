<template>
  <div class="city-travel">
    <Header />
    <header id="travel-header">
      <CityNav />
      <Slider />
    </header>

    <header id="travel-views">
      <h1>当热门景点</h1>
      <views-card />
    </header>
    <div id="travel-body">
      <nav>
        <h1>景点推文</h1>
        <InfoCards :dataList="dataList" />
      </nav>
      <aside>
        <header id="travel-rank">
          <h1>近期热门景点</h1>
          <RankTable />
        </header>
      </aside>

      <article>
        <Videos />

        <p>
          灿若星河的文化之旅，三湘四水的芙蓉国度，惟楚有才，于斯为盛，
          湖南人民在湖湘大地上谱写了一曲深邃而悠远的传奇。
        </p>
      </article>
    </div>
    <Footer />
  </div>
</template>

<script>
import CityNav from "../../components/CityInfo/CityNav.vue";
import InfoCards from "../../components/CityInfo/InfoCards.vue";
import ViewsCard from "../../components/CityInfo/ViewsCard.vue";
// import NavItem from "../../components/Layout/NavItem.vue";
import Slider from "../../components/CityInfo/Slider.vue";
import ArticleCards from "../../components/CityInfo/ArticleCards.vue";
import Footer from "../../components/Layout/Footer.vue";
import Header from "@/components/Layout/Header.vue";

import RankTable from "../../components/CityInfo/RankTable.vue";
import Videos from "../../components/CityInfo/Videos.vue";
export default {
  name: "CityFood",
  components: {
    Slider,
    InfoCards,
    ArticleCards,
    Footer,
    ViewsCard,
    Header,
    InfoCards,
    RankTable,
    Videos,
    CityNav,
  },
  data() {
    return {
      currentOffset: 0,
      windowSize: 3,
      paginationFactor: 220,
      currentCity: "", //
      buttonData: [],
      items: [], // 瀑布流数据
      videos: [],
      dataList: [
        {
          URL: "https://travel.qunar.com/p-cs300064-zhangjiajie",
          title: "烟雨张家界，有“自然的迷宫”武陵源，有“天门吐雾”的罕见奇观。 这里的每一座山峰都是大自然的鬼斧神工。",
          img: "https://img1.qunarzz.com/travel/poi/1806/95/cc9542a3d8722d37.png_r_720x400x95_53eabde3.png",
        },
        {
          URL: "https://travel.qunar.com/p-cs300022-changsha",
          title: "长沙，一座充火辣直爽的城市。它是芙蓉国里的一抹灿烂的朝晖，是湘水之畔的灵韵所在。",
          img: "https://img1.qunarzz.com/travel/poi/1806/46/a1bc3ab1228d6437.png_r_720x400x95_8c0fa956.png",
        },
        {
          URL: "https://travel.qunar.com/p-cs300061-yueyang",
          title: "昔闻洞庭之水，今登岳阳楼上，漫步汨罗江畔，追忆屈子离骚，感叹世事无常，走进文人墨客笔下的岳阳。",
          img: "https://img1.qunarzz.com/travel/poi/201405/26/997b59e2ed4f0d11ddb12cfb.jpg_r_720x400x95_fd74827f.jpg",
        },
        {
          URL: "https://travel.qunar.com/p-cs300068-xiangxi",
          title: "剪一段旧时光，容我岁月静好，透过凤凰烟雨，寻找100多年前的地图上的古镇风貌。",
          img: "https://img1.qunarzz.com/travel/poi/1412/ac/acba8be6f59496c1cdb.jpg_r_720x400x95_3d475a85.jpg",
        },
        {
          URL: "https://travel.qunar.com/p-cs300063-huaihua",
          title: "怀化市区（鹤城区）位于湖南省西南部，雪峰山脉和武陵山脉之间。面积773平方公里，人口30.69万。人口密度为每平方公里…",
          img: "https://img1.qunarzz.com/travel/poi/201403/26/6a0ebcaf6f73fb27ddb12cfb.jpg_r_720x400x95_fd277633.jpg",
        },
      ],
      currentPage: 1, //当前页数
      pageSize: 10, // 每页显示条数
      total: 0, // 总条数
      videoTotal: 0, // 总条数
    };
  },
  computed: {
    atHeadOfList() {
      return this.currentOffset === 0;
    },
    atEndOfList() {
      return this.currentOffset === (this.items.length - 1) * this.slideWidth;
    },
  },
  created() {
    // this.loadButton();
  },
  methods: {
    moveCarousel(direction) {
      // Find a more elegant way to express the :style. consider using props to make it truly generic
      if (direction === 1 && !this.atEndOfList) {
        this.currentOffset -= this.paginationFactor;
      } else if (direction === -1 && !this.atHeadOfList) {
        this.currentOffset += this.paginationFactor;
      }
    },
    handleClick(url) {
      window.open(url, "_blank");
    },
  },
};
</script>

<style lang="scss" scope>
* {
  box-sizing: border-box;
}

.city-travel {
  margin: 1em;
  // font: 1.2em/1.3em "HelveticaNeue-Light", "Helvetica Neue Light",
  //   "Helvetica Neue", "Roboto-Light", "Roboto Light", "Roboto",
  //   "Segoe UI Web Light", "Segoe UI Light", "Segoe UI Web Regular", "Segoe UI",
  //   Helvetica, Arial, sans-serif;
  color: #fff;
}
#travel-rank {
  background-color: gray;
  height: auto;
}
h1 {
  font-weight: normal;
  text-align: center;
}
p {
  margin: 0 0 1em 0;
}

#travel-body {
  margin: 0;
  padding: 0;
  display: -webkit-flex;
  display: flex;
  -webkit-flex-flow: row;
  flex-flow: row;
}

#travel-header,
#travel-footer,
#travel-body > article,
#travel-body > nav,
#travel-body > aside {
  margin: 4px;
  padding: 1em;
}
#travel-header {
  margin-top: 2px;
  margin-left: 4px;
  margin-right: 4px;
}
#travel-body > article {
  background: #996;
  -webkit-flex: 4 1 0;
  flex: 4 1 0;
  -webkit-order: 2;
  order: 2;
}

#travel-body > nav,
#travel-body > aside {
  background: #663;
  -webkit-flex: 1 6 0;
  flex: 4 6 0;
}
#travel-body > nav {
  -webkit-order: 1;
  order: 1;
}

#travel-body > aside {
  -webkit-order: 3;
  order: 3;
}

#travel-header,
#travel-footer {
  display: block;
  min-height: 80px;
}

#travel-header {
  background: #633;
  margin-top: 80px;
  height: 100%;
}
#travel-views {
  height: 100%;
}
#travel-footer {
  background: #c66;
}

/* Too narrow to support three columns */
@media all and (max-width: 640px) {
  #travel-body,
  #page {
    -webkit-flex-flow: column;
    flex-flow: column;
  }

  #travel-body > article,
  #travel-body > nav,
  #travel-body > aside {
    /* Return them to document order */
    -webkit-order: 0;
    order: 0;
  }

  #travel-body > nav,
  #travel-body > aside,
  #travel-header,
  #travel-footer {
    min-height: 50px;
  }
}
</style>