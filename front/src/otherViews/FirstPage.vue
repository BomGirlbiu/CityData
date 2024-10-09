<template>
  <div class="index">
    <div class="container">
      <section id="img-one" class="img">
        <h1 class="index-title">中国城市国际传播大数据智能分析平台</h1>
      </section>
      <section class="content-one">
        <div class="text-box">
          <div class="cnt">
            <h2>点击进入您感兴趣的模块</h2>
            <p>Click to enter the module you are interested in.</p>
            <p>
              <!-- <a href="#" class="btn"
                >TAKE <strong>CARE OF</strong><em>YOURSEFL</em></a
              > -->
            </p>

            <!-- 卡片组件 -->
            <!-- <h1 class="title">点击进入您感兴趣的模块</h1> -->
            <div class="card-container">
              <nav-card
                data-image="https://images.unsplash.com/photo-1479660656269-197ebb83b540?dpr=2&auto=compress,format&fit=crop&w=1199&h=798&q=80&cs=tinysrgb&crop="
              >
                <!-- card无法实现跳转 -->
                <h1 slot="header" @click="goToModule(1)">城市信息</h1>
                <p slot="content">浏览讯息，个性化推荐</p>
              </nav-card>
              <nav-card
                data-image="https://images.unsplash.com/photo-1479659929431-4342107adfc1?dpr=2&auto=compress,format&fit=crop&w=1199&h=799&q=80&cs=tinysrgb&crop="
              >
                <h1 slot="header" @click="goToModule(2)">数据跟踪</h1>
                <p slot="content">具体城市详细数据分析</p>
              </nav-card>
              <nav-card
                data-image="https://images.unsplash.com/photo-1479644025832-60dabb8be2a1?dpr=2&auto=compress,format&fit=crop&w=1199&h=799&q=80&cs=tinysrgb&crop="
              >
                <h1 slot="header" @click="goToModule(3)">数据对比</h1>
                <p slot="content">总体城市数据对比</p>
              </nav-card>
              <nav-card
                data-image="https://images.unsplash.com/photo-1479621051492-5a6f9bd9e51a?dpr=2&auto=compress,format&fit=crop&w=1199&h=811&q=80&cs=tinysrgb&crop="
              >
                <h1 slot="header" @click="goToModule(4)">城市频道</h1>
                <p slot="content">信息交互个性化平台</p>
              </nav-card>
              <nav-card
                data-image="https://images.unsplash.com/photo-1479621051492-5a6f9bd9e51a?dpr=2&auto=compress,format&fit=crop&w=1199&h=811&q=80&cs=tinysrgb&crop="
              >
                <h1 slot="header" @click="goToModule(5)">联想空间</h1>
                <p slot="content">定制城市宣传片</p>
              </nav-card>
            </div>
          </div>
        </div>
      </section>
      <section class="content-two">
        <div class="text-box">
          <div class="cnt">
            <h2>关于城市信息</h2>
            <p>
              在这个精心策划的板块中，您将开启一段丰富多彩的城市探索之旅。从迷人的旅游景点，到令人垂涎欲滴的美食佳肴，再到最新的城市新闻动态，每一方面都经过精心挑选，只为满足您的好奇心和探索欲。无论是想要规划下一次的旅行目的地，寻找隐藏在街角的美食天堂，还是了解城市的最新动态，这里都是您的理想起点。
            </p>
            <p>
              <a href="#" class="btn"
                >BEST <strong>WISHS</strong><em>FOR YOU</em></a
              >
            </p>
          </div>
        </div>
      </section>
      <section class="content-three">
        <div class="text-box">
          <div class="cnt">
            <h2>关于数据追踪</h2>
            <p>
              在这个板块，您将获得深入洞察多个城市的传播指数的详尽分析。每一座城市的独特魅力和影响力，都通过细致的数据和图表展现在您眼前。想要了解更多细节？轻触该模块中的帮助文档，一切信息都将为您一一揭晓。
            </p>

            <p>
              <a href="#" class="btn"
                >TAKE <strong>CARE OF</strong><em>YOURSEFL</em></a
              >
            </p>
          </div>
        </div>
      </section>
      <section class="content-forth">
        <div class="text-box">
          <div class="cnt">
            <h2>关于数据对比</h2>
            <p>
              在这个模块，您将见证一场精彩的城市间较量。各项指标的对比，如同一场无声的竞赛，将多个城市的独特优势和潜在挑战一一呈现。通过直观的数据对比，您可以轻松地探索每个城市在不同领域的表现，发现它们之间的微妙差异和显著差异。
            </p>
            <p>
              <a href="#" class="btn"
                >TAKE <strong>CARE OF</strong><em>YOURSEFL</em></a
              >
            </p>
          </div>
        </div>
      </section>
      <section class="content-five">
        <div class="text-box">
          <div class="cnt">
            <h2>关于城市频道</h2>
            <p>
              在城市频道的广阔天地里，挑选您钟情的城市，上传您珍藏的图片或撰写的文章，让城市的每一个角落、每一道风景、每一段故事，都通过您的视角焕发出独特的光彩。让我们一起，用您的作品向世界展现您心中城市的无限魅力。
            </p>
            <p>
              <a href="#" class="btn"
                >TAKE <strong>CARE OF</strong><em>YOURSEFL</em></a
              >
            </p>
          </div>
        </div>
      </section>

      <section class="content-six">
        <div class="text-box">
          <div class="cnt">
            <h2>关于联想空间</h2>
            <p>
              在人工智能技术的浪潮中，我们拥抱变革，将这股智能的力量注入城市宣传的血脉。通过AI的魔法，我们不仅捕捉城市的每一个精彩瞬间，更创造出令人惊叹的图像和视频作品。这些作品不仅仅是视觉的盛宴，它们是城市精神的现代诠释，是创意与科技完美融合的杰作，让城市的每一个故事都以一种新颖、引人入胜的方式呈现给世界。
            </p>
            <p>
              <a href="#" class="btn"
                >TAKE <strong>CARE OF</strong><em>YOURSEFL</em></a
              >
            </p>
          </div>
        </div>
      </section>

      <!-- <section id="img-two" class="img">
        <h2>关于我们</h2>
      </section> -->
      <section id="footer">FOOTER</section>
    </div>
  </div>
</template>

<script>
import NavCard from "./NavCard.vue";
export default {
  name: "FirstPage",
  components: {
    NavCard,
  },
  data() {
    return {};
  },
  methods: {
    goToModule(value) {
      if(value === 1){
        this.$router.push("CityInfo");
      }
      if(value === 2){
        this.$router.push("CityInfo");
      }
      if(value === 3){
        this.$router.push("CityInfo");
      }
      if(value === 4){
        this.$router.push("CommunityLayout");
      }
      if(value === 5){
        this.$router.push("CityInfo");
      }
      
    },
  },
};
</script>

<style lang="scss" scope>
@import url("../assets/css/index.css");
.index-title {
  font-size: 100px;
}
.title {
  font-family: "Raleway";
  font-size: 24px;
  font-weight: 700;
  color: #5d4037;
  text-align: center;
}

p {
  line-height: 1.5em;
}

h1 + p,
p + p {
  margin-top: 10px;
}

.card-container {
  padding: 40px 80px;
  display: flex;
  flex-wrap: nowrap;
  justify-content: center;
}
</style>