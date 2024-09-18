<template>
<div class="index">
    <header>
        <h2 class="logo">Citis in China</h2>
        <nav class="navbar">
            <router-link to="/index/indexContent" >首页</router-link>
            <!-- <a href="#" class="active">首页</a> -->
            <router-link to="/index/news" >城市信息</router-link>
            <router-link to="/index/visual" >可视化大屏</router-link>
            <router-link to="/index/evaluate" >城市传播指数</router-link>
            <router-link to="/index/login" >后台管理</router-link>
        </nav>
    </header>
    <div class="content">
        <router-view></router-view>
    </div>
</div>
  
</template>

<script>
export default {
    data(){
        return{
            dubaiTextLeft: 0,  
            burjkhalifaTop: 0,  
            starsTop: 0, 
        }
    },
    mounted() {  
    window.addEventListener('scroll', this.handleScroll);  
  },  
  beforeDestroy() {  
    window.removeEventListener('scroll', this.handleScroll);  
  },  
  methods: {  
    handleScroll() {  
      let value = window.scrollY;  
      this.dubaiTextLeft = value * -2;  
      this.burjkhalifaTop = value;  
      this.starsTop = value;  
    },  
    // isActive(linkHref){
    //     console.log(this.currentPath)
    //     console.log(linkHref)
    //     return linkHref === this.currentPath; 
    // }
  },  
}
</script>

<style lang="scss" scope>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}
.index
{
    background: linear-gradient(#040228 0%,#0075c7 40%);
    min-height: 100vh;
    overflow: hidden;
}
header
{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    padding: 30px 100px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 100;
}
.logo{
    color: #fff;
    font-size: 2em;
    cursor: default;
}
.navbar a{
    color: #fff;
    text-decoration: none;
    margin-left: 20px;
    font-weight: 600;
    padding: 6px 15px;
    border-radius: 20px;
}
.navbar a:hover,
.navbar a.active {
    background: #00a3b9;
}
.parallax{
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.parallax img{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    pointer-events: none;
}
.sec{
    position: relative;
    padding: 100px;
    background-color: #040228;
}
.sec h2{
    font-size: 3em;
    color: #fff;
    margin-bottom: 10px;
}
.sec h2:nth-child(2){
    font-size: 2em;
}
.sec p{
    font-size: 1em;
    color: #fff;
    font-weight: 300;
}
.bottom{
    height: 4%;
    width: 100%;
    bottom: 0;
    position: absolute;
    background: linear-gradient(to right, rgb(15, 12, 41), rgb(48, 43, 99), rgb(36, 36, 62));
}
.bottom p{
    font: 10px;
    margin: 6px;
}
</style>