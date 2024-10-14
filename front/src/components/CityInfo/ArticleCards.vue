<template>
  <section class="cards">
    <article class="card card--1"  v-for="item in ArticleList" :key="item.URL">
      <div class="card__info-hover">
        <img class="card__like" :src="item.img" alt=""/>
        <div class="card__clock-info">
          <img class="card__clock" :src="item.img" alt=""/>
            <span class="card__time">15 min</span>
        </div>
      </div>
      <div class="card__img"></div>
      <a href="#" class="card_link">
        <div class="card__img--hover"></div>
      </a>
      <div class="card__info">
        <span class="card__category"> Recipe</span>
        <h3 class="card__title">{{item.title}}</h3>
        <span class="card__by"
          >by
          <a href="#" class="card__author" title="author"
            >{{item.author}}</a
          ></span
        >
      </div>
    </article>
  </section>
</template>

<script>
export default {
  name: "ArticleCards",
  data(){
    return{
        ArticleList:[
            {
                img:"https://p1.img.cctvpic.com/photoAlbum/page/performance/img/2018/2/14/1518615286960_176.jpg",
                title:"独家访谈——著名纪录片专家： “舌尖3”突破了固有的美食讲述范围，带来更宽广的视野",
                author:"作者"
            },
            {
                img:"https://p1.img.cctvpic.com/photoAlbum/page/performance/img/2018/2/14/1518615286960_176.jpg",
                title:"独家访谈——著名纪录片专家： “舌尖3”突破了固有的美食讲述范围，带来更宽广的视野",
                author:"作者"
            },
            {
                img:"https://p1.img.cctvpic.com/photoAlbum/page/performance/img/2018/2/14/1518615286960_176.jpg",
                title:"独家访谈——著名纪录片专家： “舌尖3”突破了固有的美食讲述范围，带来更宽广的视野",
                author:"作者"
            },
            {
                img:"https://p1.img.cctvpic.com/photoAlbum/page/performance/img/2018/2/14/1518615286960_176.jpg",
                title:"独家访谈——著名纪录片专家： “舌尖3”突破了固有的美食讲述范围，带来更宽广的视野",
                author:"作者"
            },
            {
                img:"https://p1.img.cctvpic.com/photoAlbum/page/performance/img/2018/2/14/1518615286960_176.jpg",
                title:"独家访谈——著名纪录片专家： “舌尖3”突破了固有的美食讲述范围，带来更宽广的视野",
                author:"作者"
            },
        ]
    }
  }
};
</script>

<style lang="scss" scope>
@import url("https://fonts.googleapis.com/css?family=Roboto+Slab:100,300,400,700");
@import url("https://fonts.googleapis.com/css?family=Raleway:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i");

// * {
//   box-sizing: border-box;
// }

// body,
// html {
//   font-family: "Roboto Slab", serif;
//   margin: 0;
//   width: 100%;
//   height: 100%;
//   padding: 0;
// }

// body {
//   background-color: #d2dbdd;
//   display: flex;
//   display: -webkit-flex;
//   -webkit-justify-content: center;
//   -webkit-align-items: center;
//   justify-content: center;
//   align-items: center;
// }

.cards {
  width: 100%;
//   display: flex;
//   display: -webkit-flex;
  justify-content: center;
  -webkit-justify-content: center;
  max-width: 820px;
}

.card--1 .card__img,
.card--1 .card__img--hover {
  background-image: url("https://images.pexels.com/photos/45202/brownie-dessert-cake-sweet-45202.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260");
}
.card__like {
  width: 18px;
}

.card__clock {
  width: 15px;
  vertical-align: middle;
  fill: #ad7d52;
}
.card__time {
  font-size: 12px;
  color: #ad7d52;
  vertical-align: middle;
  margin-left: 5px;
}

.card__clock-info {
  float: right;
}

.card__img {
  visibility: hidden;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  width: 100%;
  height: 235px;
  border-top-left-radius: 12px;
  border-top-right-radius: 12px;
}

.card__info-hover {
  position: absolute;
  padding: 16px;
  width: 100%;
  opacity: 0;
  top: 0;
}

.card__img--hover {
  transition: 0.2s all ease-out;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  width: 100%;
  position: absolute;
  height: 235px;
  border-top-left-radius: 12px;
  border-top-right-radius: 12px;
  top: 0;
}
.card {
  margin-right: 25px;
  margin-bottom: 20px;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0, 1);
  background-color: #fff;
  width: 100%;
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0px 13px 10px -7px rgba(0, 0, 0, 0.1);
}
.card:hover {
  box-shadow: 0px 30px 18px -8px rgba(0, 0, 0, 0.1);
  transform: scale(1.1, 1.1);
}

.card__info {
  z-index: 2;
  background-color: #fff;
  border-bottom-left-radius: 12px;
  border-bottom-right-radius: 12px;
  padding: 16px 24px 24px 24px;
}

.card__category {
  font-family: "Raleway", sans-serif;
  text-transform: uppercase;
  font-size: 13px;
  letter-spacing: 2px;
  font-weight: 500;
  color: #868686;
}

.card__title {
  margin-top: 5px;
  margin-bottom: 10px;
  font-family: "Roboto Slab", serif;
}

.card__by {
  font-size: 12px;
  font-family: "Raleway", sans-serif;
  font-weight: 500;
}

.card__author {
  font-weight: 600;
  text-decoration: none;
  color: #ad7d52;
}

.card:hover .card__img--hover {
  height: 100%;
  opacity: 0.3;
}

.card:hover .card__info {
  background-color: transparent;
  position: relative;
}

.card:hover .card__info-hover {
  opacity: 1;
}
</style>