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
          Attack your ankles puking chase the red dot lay down in your way,
          knock over the lamp sunbathe eat the grass sleep on your keyboard jump
          sleep in the sink shed everywhere. Jump on the table sleep on your
          keyboard jump on the table scratched sunbathe judging you, give me
          fish climb the curtains sleep on your face sleep in the sink bat
          sniff. Knock over the lamp jump sleep in the sink tail flick, sleep in
          the sink I don't like that food sleep on your face rip the couch bat
          sleep on your keyboard toss the mousie.
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
          URL: "https://culture-travel.cctv.com/2024/09/19/ARTIwTB6ZFevuMbzGrjdIi0U240919.shtml?spm=C30123.PdSpIAXhl6Iy.EqQGKgG2jQOS.1",
          title: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
          img: "https://p5.img.cctvpic.com/photoworkspace/2024/09/19/2024091910130313801.jpg",
          content: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
        },
        {
          URL: "https://culture-travel.cctv.com/2024/09/19/ARTIwTB6ZFevuMbzGrjdIi0U240919.shtml?spm=C30123.PdSpIAXhl6Iy.EqQGKgG2jQOS.1",
          title: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
          img: "https://p5.img.cctvpic.com/photoworkspace/2024/09/19/2024091910130313801.jpg",
        },
        {
          URL: "https://culture-travel.cctv.com/2024/09/19/ARTIwTB6ZFevuMbzGrjdIi0U240919.shtml?spm=C30123.PdSpIAXhl6Iy.EqQGKgG2jQOS.1",
          title: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
          img: "https://p5.img.cctvpic.com/photoworkspace/2024/09/19/2024091910130313801.jpg",
          content: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
        },
        {
          URL: "https://culture-travel.cctv.com/2024/09/19/ARTIwTB6ZFevuMbzGrjdIi0U240919.shtml?spm=C30123.PdSpIAXhl6Iy.EqQGKgG2jQOS.1",
          title: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
          img: "https://p5.img.cctvpic.com/photoworkspace/2024/09/19/2024091910130313801.jpg",
          content: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
        },
        {
          URL: "https://culture-travel.cctv.com/2024/09/19/ARTIwTB6ZFevuMbzGrjdIi0U240919.shtml?spm=C30123.PdSpIAXhl6Iy.EqQGKgG2jQOS.1",
          title: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
          img: "https://p5.img.cctvpic.com/photoworkspace/2024/09/19/2024091910130313801.jpg",
          content: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
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