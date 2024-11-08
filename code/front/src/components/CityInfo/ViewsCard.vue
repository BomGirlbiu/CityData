<template>
  <div class="viws-card">
    <div class="views-container" v-for="item in viewsList" :key="item.url">
      <img
        class="views-img"
        :src="item.img"
        alt=""
      />
      <p class="views-title">scene</p>
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