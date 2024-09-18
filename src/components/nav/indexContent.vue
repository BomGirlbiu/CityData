<template>
  <div>
    <section class="parallax">
      <img
        src="../../assets/stars.png"
        id="stars"
        :style="{ top: starsTop + 'px' }"
      />
      <img
        src="../../assets/burjkhalifa.png"
        id="burjkhalifa"
        :style="{ top: burjkhalifaTop + 'px' }"
      />
      <img src="../../assets/building.png" id="building" />
      <img
        src="../../assets/dubaitext.png"
        id="dubaitext"
        :style="{ left: dubaiTextLeft + 'px' }"
      />
    </section>

    <section class="sec">
      <h2>关于我们</h2>
      <h3 class="text">
        在历史与现代的相互交织中，
        每座城市都蕴藏着中华文明的历史遗迹和符号记忆，
        承载着中国式现代化发展的时代使命。讲好中国城市故事，传播好中国城市声音，
        建构好中国城市形象，对于新时代提升中国国际传播能力具有重要战略意义。
        科学评估中国城市国际传播的现状和问题，有助于优化顶层设计和政策布局，
        改进中国城市的全球传播方案，升级中国城市的国际传播策略。在此背景下，
        本系统的用户不仅包含所有对中国城市的传播情况进行调查研究的学者、专家，
        还包括从事企业相关行业的工作人员，还包括对于中国城市传播情况感兴趣的人员。
      </h3>
      <h3 class="text2">
        关于数据来源， 网络传播影响力和社交媒体影响力数据来自google、
        抖音、微博等社交
        媒体平台，媒体报道影响力数据来自纽约时报，搜索引擎影响力数据源于谷歌趋势指数
        （Google Trends），国际访客影响力数据则取自官网出入境公开文件。<br /><br />
      </h3>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dubaiTextLeft: 0,
      burjkhalifaTop: 0,
      starsTop: 0,
    };
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      let value = window.scrollY;
      this.dubaiTextLeft = value * -2;
      this.burjkhalifaTop = value;
      this.starsTop = value;
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap");
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
.parallax {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.parallax img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  pointer-events: none;
}
.sec {
  position: relative;
  padding: 100px;
  background-color: #040228;
}
.sec h2 {
  font-size: 3em;
  color: #fff;
  margin-bottom: 10px;
}
.sec h2:nth-child(2) {
  font-size: 2em;
}
.sec p {
  font-size: 1em;
  color: #e4e4e4;
  font-weight: 300;
}
.text {
  text-indent: 2em;
  text-align: left;
  letter-spacing:4px;
}
.text2 {
  text-indent: 2em;
  text-align: left;
  letter-spacing:4px;
  /* border-bottom: 1px dashed #000;
  text-decoration: underline;
   padding-bottom: 2px; */
}
</style>