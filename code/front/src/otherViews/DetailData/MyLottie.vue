<!-- components/MyLottie -->
<template>
  <!-- 渲染容器 -->
  <div class="lottie"></div>
</template>

<script>
import lottie from "lottie-web";

export default {
  props: {
    animationData: {
      type: Object,
      required: true,
    },
    autoplay: {
      type: Boolean,
      default: true,
    },
    loop: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      lottie: null,
    };
  },
  mounted() {
    this.intLottie();
  },
  methods: {
    intLottie() {
      const { animationData, autoplay, loop } = this;
      this.lottie = lottie.loadAnimation({
        container: this.$el, // 渲染容器
        renderer: "svg", // 渲染方式 svg|canvas|html
        loop, // 是否循环 true|false|number
        autoplay, // 自动播放 true|false
        animationData, // lottie json文件
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.lottie {
  width: 100%;
  height: 100%;
}
</style>
