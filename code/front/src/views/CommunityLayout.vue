<template>
  <div>
    <div class="mb-5">
      <Header/>
      <CommunityHeader/>
    </div>

    <div class="container context">
        <router-view :key="this.$route.fullPath"></router-view>
    </div>

    <div>
      <Footer></Footer>
    </div>
  </div>
</template>

<script>
import Header from "@/components/Layout/Header";
import Footer from "@/components/Layout/Footer";
import CommunityHeader from "@/components/Layout/CommunityHeader"
export default {
  name: "CommunityLayout",
  components: { Header, Footer,CommunityHeader },
  data(){
    // return{
    //   currentModule:{
    //     value:<a href="#tab-other" class="et-hero-tab">城市频道</a>
    //   },
    //   currentId:"#tab-magic"
    // }
  }
};
</script>

<style scoped>
.container {
  min-height: 500px;
}
</style>
