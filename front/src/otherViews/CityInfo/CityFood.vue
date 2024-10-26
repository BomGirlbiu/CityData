<template>
  <div class="city-food">
    <Header />
    <header id="food-header">
      <CityNav />
      <h1>Responsive Layout using Flexbox</h1>
      <div class="food-slider">
        <p>美食菜谱</p>
        <div class="card-carousel-wrapper">
          <div
            class="card-carousel--nav__left"
            @click="moveCarousel(-1)"
            :disabled="atHeadOfList"
          ></div>
          <div class="card-carousel">
            <div class="card-carousel--overflow-container">
              <div
                class="card-carousel-cards"
                :style="{
                  transform: 'translateX' + '(' + currentOffset + 'px' + ')',
                  height: '100%',
                  width: '2000px',
                }"
              >
                <div
                  class="card-carousel--card"
                  v-for="item in cookbook"
                  :key="item.URL"
                >
                  <img :src="item.cover" width="600px" height="400px" />
                  <div class="card-carousel--card--footer">
                    <p>{{ item.title }}</p>
                    <p>11111</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div
            class="card-carousel--nav__right"
            @click="moveCarousel(1)"
            :disabled="atEndOfList"
          ></div>
        </div>
      </div>
    </header>

    <div id="food-body">
      <aside>
        <h1>特色专题</h1>
        <span id="activity-list" v-for="item in dataList" :key="item.URL">
          <div class="flip">
            <div class="front" :style="{ backgroundImage: `url(${item.img})` }">
              <h1 class="text-shadow">{{ item.title }}</h1>
            </div>
            <div class="back">
              <h2>Angular</h2>
              <p>
                Good tools make application development quicker and easier to
                maintain than if you did everything by hand..
              </p>
            </div>
          </div>
        </span>
      </aside>

      <article>
        <h1>美食资讯</h1>
        <InfoCards :dataList="dataList" />
      </article>
      <article>
        <h1>美食文章</h1>
        <ArticleCards />
      </article>
    </div>
    <Footer />
  </div>
</template>

<script>
// import NavItem from "../../components/Layout/NavItem.vue";
import Header from '../../components/Layout/Header.vue'

import CityNav from "../../components/CityInfo/CityNav.vue";
import InfoCards from "../../components/CityInfo/InfoCards.vue";
import ArticleCards from "../../components/CityInfo/ArticleCards.vue";
import Footer from "../../components/Layout/Footer.vue";
export default {
  name: "CityFood",
  components: {
    Header,
    InfoCards,
    ArticleCards,
    Footer,
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
      cookbook: [
        {
          cover:
            "https://cp1.douguo.com/upload/caiku/9/1/6/500x300_916681faf14299041584069fffa44996.jpg",
          title: "四川担担面",
          URL: "https://www.douguo.com/cookbook/1594159.html",
        },
        {
          cover:
            "https://cp1.douguo.com/upload/caiku/9/1/6/500x300_916681faf14299041584069fffa44996.jpg",
          title: "四川担担面",
          URL: "https://www.douguo.com/cookbook/1594159.html",
        },
        {
          cover:
            "https://cp1.douguo.com/upload/caiku/9/1/6/500x300_916681faf14299041584069fffa44996.jpg",
          title: "四川担担面",
          URL: "https://www.douguo.com/cookbook/1594159.html",
        },
        {
          cover:
            "https://cp1.douguo.com/upload/caiku/9/1/6/500x300_916681faf14299041584069fffa44996.jpg",
          title: "四川担担面",
          URL: "https://www.douguo.com/cookbook/1594159.html",
        },
        {
          cover:
            "https://cp1.douguo.com/upload/caiku/9/1/6/500x300_916681faf14299041584069fffa44996.jpg",
          title: "四川担担面",
          URL: "https://www.douguo.com/cookbook/1594159.html",
        },
        {
          cover:
            "https://cp1.douguo.com/upload/caiku/9/1/6/500x300_916681faf14299041584069fffa44996.jpg",
          title: "四川担担面",
          URL: "https://www.douguo.com/cookbook/1594159.html",
        },
        {
          cover:
            "https://cp1.douguo.com/upload/caiku/9/1/6/500x300_916681faf14299041584069fffa44996.jpg",
          title: "四川担担面",
          URL: "https://www.douguo.com/cookbook/1594159.html",
        },
      ], //轮播图数据
      dataList: [
        {
          URL: "https://culture-food.cctv.com/2024/09/19/ARTIwTB6ZFevuMbzGrjdIi0U240919.shtml?spm=C30123.PdSpIAXhl6Iy.EqQGKgG2jQOS.1",
          title: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
          img: "https://p5.img.cctvpic.com/photoworkspace/2024/09/19/2024091910130313801.jpg",
          content: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
        },
        {
          URL: "https://culture-food.cctv.com/2024/09/19/ARTIwTB6ZFevuMbzGrjdIi0U240919.shtml?spm=C30123.PdSpIAXhl6Iy.EqQGKgG2jQOS.1",
          title: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
          img: "https://p5.img.cctvpic.com/photoworkspace/2024/09/19/2024091910130313801.jpg",
        },
        {
          URL: "https://culture-food.cctv.com/2024/09/19/ARTIwTB6ZFevuMbzGrjdIi0U240919.shtml?spm=C30123.PdSpIAXhl6Iy.EqQGKgG2jQOS.1",
          title: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
          img: "https://p5.img.cctvpic.com/photoworkspace/2024/09/19/2024091910130313801.jpg",
          content: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
        },
        {
          URL: "https://culture-food.cctv.com/2024/09/19/ARTIwTB6ZFevuMbzGrjdIi0U240919.shtml?spm=C30123.PdSpIAXhl6Iy.EqQGKgG2jQOS.1",
          title: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
          img: "https://p5.img.cctvpic.com/photoworkspace/2024/09/19/2024091910130313801.jpg",
          content: "新文旅“广东范儿”：让你给“味蕾游”留出最多预算",
        },
        {
          URL: "https://culture-food.cctv.com/2024/09/19/ARTIwTB6ZFevuMbzGrjdIi0U240919.shtml?spm=C30123.PdSpIAXhl6Iy.EqQGKgG2jQOS.1",
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
// * {
//     box-sizing: border-box;
// }
.city-food {
  margin: 1em;
  color: #fff;
}
h1 {
  font-weight: normal;
  text-align: center;
}
p {
  margin: 0 0 1em 0;
}

#food-body {
  margin: 0;
  padding: 0;
  display: -webkit-flex;
  display: flex;
  -webkit-flex-flow: row;
  flex-flow: row;
}

#food-header,
#food-footer,
#food-body > article,
#food-body > nav,
#food-body > aside {
  margin: 4px;
  padding: 1em;
}

#food-body > article {
  background: #996;
  -webkit-flex: 4 1 0;
  flex: 4 1 0;
  -webkit-order: 2;
  order: 2;
}

#food-body > nav,
#food-body > aside {
  background: #663;
  -webkit-flex: 1 6 0;
  flex: 4 6 0;
}
#food-body > nav {
  -webkit-order: 1;
  order: 1;
}

#food-body > aside {
  -webkit-order: 3;
  order: 3;
}

#food-header,
#food-footer {
  display: block;
  min-height: 80px;
}

#food-header {
  background: #633;
  margin-top: 120px;
}

#food-footer {
  background: #c66;
}

/* Too narrow to support three columns */
@media all and (max-width: 640px) {
  #food-body,
  #page {
    -webkit-flex-flow: column;
    flex-flow: column;
  }

  #food-body > article,
  #food-body > nav,
  #food-body > aside {
    /* Return them to document order */
    -webkit-order: 0;
    order: 0;
  }

  #food-body > nav,
  #food-body > aside,
  #food-header,
  #food-footer {
    min-height: 50px;
  }
}

// slider
$vue-navy: #2c3e50;
$vue-navy-light: #3a5169;
$vue-teal: #42b883;
$vue-teal-light: #42b983;
$gray: #666a73;
$light-gray: #f8f8f8;

body {
  background: $light-gray;
  color: $vue-navy;
  font-family: "Source Sans Pro", sans-serif;
}

.card-carousel-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 20px 0 40px;
  color: $gray;
}

.card-carousel {
  display: flex;
  justify-content: center;
  width: 80%;

  &--overflow-container {
    overflow: hidden;
  }

  &--nav__left,
  &--nav__right {
    display: inline-block;
    width: 15px;
    height: 15px;
    padding: 10px;
    box-sizing: border-box;
    border-top: 2px solid $vue-teal;
    border-right: 2px solid $vue-teal;
    cursor: pointer;
    margin: 0 20px;
    transition: transform 150ms linear;
    &[disabled] {
      opacity: 0.2;
      border-color: black;
    }
  }

  &--nav__left {
    transform: rotate(-135deg);
    &:active {
      transform: rotate(-135deg) scale(0.9);
    }
  }

  &--nav__right {
    transform: rotate(45deg);
    &:active {
      transform: rotate(45deg) scale(0.9);
    }
  }
}

.card-carousel-cards {
  display: flex;
  transition: transform 150ms ease-out;
  transform: translatex(0px);

  .card-carousel--card {
    height: 200px;
    margin: 0 10px;
    cursor: pointer;
    box-shadow: 0 4px 15px 0 rgba(40, 44, 53, 0.06),
      0 2px 2px 0 rgba(40, 44, 53, 0.08);
    background-color: #fff;
    border-radius: 4px;
    z-index: 3;
    margin-bottom: 2px;

    &:first-child {
      margin-left: 0;
    }

    &:last-child {
      margin-right: 0;
    }

    img {
      vertical-align: bottom;
      border-top-left-radius: 4px;
      border-top-right-radius: 4px;
      transition: opacity 150ms linear;
      user-select: none;

      &:hover {
        opacity: 0.5;
      }
    }

    &--footer {
      border-top: 0;
      padding: 7px 15px;

      p {
        padding: 3px 0;
        margin: 0;
        margin-bottom: 2px;
        font-size: 19px;
        font-weight: 500;
        color: $vue-navy;
        user-select: none;

        &.tag {
          font-size: 11px;
          font-weight: 300;
          padding: 4px;
          background: rgba(40, 44, 53, 0.06);
          display: inline-block;
          position: relative;
          margin-left: 4px;
          color: $gray;

          &:before {
            content: "";
            float: left;
            position: absolute;
            top: 0;
            left: -12px;
            width: 0;
            height: 0;
            border-color: transparent rgba(40, 44, 53, 0.06) transparent
              transparent;
            border-style: solid;
            border-width: 8px 12px 12px 0;
          }
          &.secondary {
            margin-left: 0;
            border-left: 1.45px dashed white;
            &:before {
              display: none !important;
            }
          }

          &:after {
            content: "";
            position: absolute;
            top: 8px;
            left: -3px;
            float: left;
            width: 4px;
            height: 4px;
            border-radius: 2px;
            background: white;
            box-shadow: -0px -0px 0px #004977;
          }
        }
      }
    }
  }
}

h1 {
  font-size: 3.6em;
  font-weight: 100;
  text-align: center;
  margin-bottom: 0;
  color: $vue-teal;
}

// 活动列表
@import url("https://fonts.googleapis.com/css?family=Roboto+Mono");

// * {
//   box-sizing: border-box;
//   font-weight: normal;
// }

// body {
//   color: #555;
//   background: #222;
//   text-align: center;
//   font-family: 'Roboto Mono';
//   padding: 1em;
// }
#activity-list {
  display: flex;
  flex-direction: column;
}

.text-shadow {
  font-size: 2.2em;
}

// base
.flip {
  position: relative;
  > .front,
  > .back {
    display: block;
    transition-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1.275);
    transition-duration: 0.5s;
    transition-property: transform, opacity;
  }
  > .front {
    transform: rotateY(0deg);
  }
  > .back {
    position: absolute;
    opacity: 0;
    top: 0px;
    left: 0px;
    width: 100%;
    height: 100%;
    transform: rotateY(-180deg);
  }
  &:hover {
    > .front {
      transform: rotateY(180deg);
    }
    > .back {
      opacity: 1;
      transform: rotateY(0deg);
    }
  }
  &.flip-vertical {
    > .back {
      transform: rotateX(-180deg);
    }
    &:hover {
      > .front {
        transform: rotateX(180deg);
      }
      > .back {
        transform: rotateX(0deg);
      }
    }
  }
}

// custom
.flip {
  position: relative;
  display: inline-block;
  margin-right: 2px;
  margin-bottom: 1em;
  width: 400px;
  > .front,
  > .back {
    display: block;
    color: white;
    width: inherit;
    background-size: cover !important;
    background-position: center !important;
    height: 220px;
    padding: 1em 2em;
    background: #313131;
    border-radius: 10px;
    p {
      font-size: 0.9125rem;
      line-height: 160%;
      color: #999;
    }
  }
}

.text-shadow {
  text-shadow: 1px 1px rgba(0, 0, 0, 0.04), 2px 2px rgba(0, 0, 0, 0.04),
    3px 3px rgba(0, 0, 0, 0.04), 4px 4px rgba(0, 0, 0, 0.04),
    0.125rem 0.125rem rgba(0, 0, 0, 0.04), 6px 6px rgba(0, 0, 0, 0.04),
    7px 7px rgba(0, 0, 0, 0.04), 8px 8px rgba(0, 0, 0, 0.04),
    9px 9px rgba(0, 0, 0, 0.04), 0.3125rem 0.3125rem rgba(0, 0, 0, 0.04),
    11px 11px rgba(0, 0, 0, 0.04), 12px 12px rgba(0, 0, 0, 0.04),
    13px 13px rgba(0, 0, 0, 0.04), 14px 14px rgba(0, 0, 0, 0.04),
    0.625rem 0.625rem rgba(0, 0, 0, 0.04), 16px 16px rgba(0, 0, 0, 0.04),
    17px 17px rgba(0, 0, 0, 0.04), 18px 18px rgba(0, 0, 0, 0.04),
    19px 19px rgba(0, 0, 0, 0.04), 1.25rem 1.25rem rgba(0, 0, 0, 0.04);
}
</style>