<template>
  <div class="viws-card">
    <div class="views-container" v-for="item in viewsList" :key="item.url">
      <img
        class="views-img"
        :src="item.img"
        alt=""
      />
      <p class="views-title">card title</p>
      <div class="views-overlay"></div>
      <div class="views-button"><a href="item.url"> BUTTON </a></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ViewsCard",
  data() {
    return {
      viewsList:[
        {
            img:"http://tr-osdcp.qunarzz.com/tr-osd-tr-manager/img/09da45332823f014429b94e55fa96c5d.jpg?width=2048&height=1365&top=0&color=#928f52",
            title:"北京小长假周末必玩榜",
            url:"https://travel.qunar.com/smartlist/7589216"
        },
        {
            img:"http://tr-osdcp.qunarzz.com/tr-osd-tr-manager/img/09da45332823f014429b94e55fa96c5d.jpg?width=2048&height=1365&top=0&color=#928f52",
            title:"北京小长假周末必玩榜",
            url:"https://travel.qunar.com/smartlist/7589216"
        },
        {
            img:"http://tr-osdcp.qunarzz.com/tr-osd-tr-manager/img/09da45332823f014429b94e55fa96c5d.jpg?width=2048&height=1365&top=0&color=#928f52",
            title:"北京小长假周末必玩榜",
            url:"https://travel.qunar.com/smartlist/7589216"
        },
        {
            img:"http://tr-osdcp.qunarzz.com/tr-osd-tr-manager/img/09da45332823f014429b94e55fa96c5d.jpg?width=2048&height=1365&top=0&color=#928f52",
            title:"北京小长假周末必玩榜",
            url:"https://travel.qunar.com/smartlist/7589216"
        },
      ]
    };
  },
};
</script>

<style lang="scss" scope>
.viws-card{
    display: flex;
    justify-content: space-around;
}
.views-container {
  position: relative;
  margin-top: 50px;
  width: 500px;
  height: 300px;
}

.views-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0);
  transition: background 0.5s ease;
}

.views-container:hover .views-overlay {
  display: block;
  background: rgba(0, 0, 0, 0.3);
}

.views-img {
  position: absolute;
  width: 500px;
  height: 300px;
  left: 0;
}

.views-title {
  position: absolute;
  width: 500px;
  left: 0;
  top: 120px;
  font-weight: 700;
  font-size: 30px;
  text-align: center;
  text-transform: uppercase;
  color: white;
  z-index: 1;
  transition: top 0.5s ease;
}

.views-container:hover .views-title {
  top: 90px;
}

.views-button {
  position: absolute;
  width: 500px;
  left: 0;
  top: 180px;
  text-align: center;
  opacity: 0;
  transition: opacity 0.35s ease;
}

.views-button a {
  width: 200px;
  padding: 12px 48px;
  text-align: center;
  color: white;
  border: solid 2px white;
  z-index: 1;
}

.views-container:hover .views-button {
  opacity: 1;
}
</style>