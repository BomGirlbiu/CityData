<template>
  <div class="index-ty">
    <div class="main-container">
      <div class="img img-1"></div>
      <div class="img img-2"></div>
      <div class="img img-3"></div>
      <div class="img img-4"></div>
      <div class="img img-5"></div>
      <div class="title title-1">San Francisco</div>
      <div class="title title-2">Hong Kong</div>
      <div class="title title-3">London</div>
      <div class="title title-4">New York</div>
      <div class="title title-5">Tokyo</div>
      <div class="info-container">
        <h3>
          CSS gallery powered by
          <a href="http://animista.net" target="_blank">Animista.net</a>
        </h3>
        <h4>Appearing animations</h4>
        <p>
          <a
            href="http://animista.net/play/background/ken-burns/kenburns-top"
            target="_blank"
            >kenburns-top</a
          >,
          <a
            href="http://animista.net/play/background/ken-burns/kenburns-bottom"
            target="_blank"
            >kenburns-bottom</a
          >,
          <a
            href="http://animista.net/play/background/ken-burns/kenburns-left"
            target="_blank"
            >kenburns-left</a
          >,
          <a
            href="http://animista.net/play/background/ken-burns/kenburns-right"
            target="_blank"
            >kenburns-right</a
          >
        </p>
        <p>
          <a
            href="http://animista.net/play/text/focus-in/focus-in-contract"
            target="_blank"
            >focus-in-contract</a
          >
        </p>
        <p>
          <a
            href="http://animista.net/play/entrances/slide-in/slide-in-bottom"
            target="_blank"
            >slide-in-bottom</a
          >
        </p>
        <h4>Disappearing animations</h4>
        <p>
          <a
            href="http://animista.net/play/exits/fade-out/fade-out"
            target="_blank"
            >fade-out</a
          >
        </p>
        <p>
          <a
            href="http://animista.net/play/text/blur-out/text-blur-out"
            target="_blank"
            >text-blur-out</a
          >
        </p>
      </div>
      <div class="loader-container">
        <div class="loader"></div>
        <p>Loading images...</p>
      </div>
    </div>
    <div class="preloaded"></div>
  </div>
</template>

<script>
import * as createjs from "createjs-module";
import { LoadQueue, Types } from "createjs-module";
export default {
  mounted() {
    var preloaded = document.querySelector(".preloaded");
    //     var queue = new LoadQueue(true, null, true);

    //     queue.on("fileload", handleLoad, this);

    //     queue.on("progress", handleProgress, this);

    //     queue.on("complete", handleComplete, this);
    // console.log(Types);
    //     queue.loadManifest([
    //       {
    //         id: "sf",
    //         crossOrigin: true,
    //         type: Types.IMAGE,
    //         src: "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?ixlib=rb-0.3.5&q=85&fm=jpg&crop=entropy&cs=srgb&s=35233ecf7c2f6b1b99123374610926fe",
    //       },
    //       {
    //         id: "hk",
    //         crossOrigin: true,
    //         type: Types.IMAGE,
    //         src: "https://images.unsplash.com/photo-1507941097613-9f2157b69235?ixlib=rb-0.3.5&q=85&fm=jpg&crop=entropy&cs=srgb&s=f8f33afdfc69b16d51c996cf3a8cc1c7",
    //       },
    //       {
    //         id: "lon",
    //         crossOrigin: true,
    //         type: Types.IMAGE,
    //         src: "https://images.unsplash.com/photo-1506501139174-099022df5260?ixlib=rb-0.3.5&q=85&fm=jpg&crop=entropy&cs=srgb&s=4868d202b74b7a313bb34a3d8526428c",
    //       },
    //       {
    //         id: "nyc",
    //         crossOrigin: true,
    //         type: Types.IMAGE,
    //         src: "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?ixlib=rb-0.3.5&q=85&fm=jpg&crop=entropy&cs=srgb&s=d8f8d728cc689063536174ec02129ebc",
    //       },
    //       {
    //         id: "tok",
    //         crossOrigin: true,
    //         type: Types.IMAGE,
    //         src: "https://images.unsplash.com/photo-1505814360303-5bfcf2a8acb6?ixlib=rb-0.3.5&q=85&fm=jpg&crop=entropy&cs=srgb&s=86aaa627e11ca46f2177787d563de340",
    //       },
    //     ]);
    //图片预加载
    var queue = new createjs.LoadQueue();
    queue.on(
      "progress",
      function (e) {
        //加载中的进度
        $(".loding_time").html(parseInt(e.progress * 100) + "%");
      },
      this
    );
    queue.on(
      "complete",
      function (e) {
        //加载完成执行操作
        $(".loading").addClass("hide");
      },
      this
    );
    queue.loadManifest([
      //加载图片，不包括后台的
      "./image1.png",
      "./img1.jpg",
    ]);
    function handleProgress(event) {
      console.log(event.progress);
    }

    function handleLoad(event) {
      console.log(event);
      var img = new Image();
      img.crossOrigin = "Anonymous";
      img.src = event.item.src;
      preloaded.appendChild(img);
      var img = queue.getResult("image", true);
      preloaded.appendChild(event.result);
    }

    function handleComplete() {
      document.querySelector(".main-container").classList.add("loaded");
      console.log("done");
    }
  },
};
</script>

<style lang="css" scope>
@font-face {
  font-family: "Rubik";
  font-style: normal;
  font-weight: 300;
  src: url(https://fonts.gstatic.com/s/rubik/v28/iJWZBXyIfDnIV5PNhY1KTN7Z-Yh-WYiFV0Uw.ttf)
    format("truetype");
}
@font-face {
  font-family: "Rubik";
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.gstatic.com/s/rubik/v28/iJWZBXyIfDnIV5PNhY1KTN7Z-Yh-B4iFV0Uw.ttf)
    format("truetype");
}
@font-face {
  font-family: "Rubik";
  font-style: normal;
  font-weight: 700;
  src: url(https://fonts.gstatic.com/s/rubik/v28/iJWZBXyIfDnIV5PNhY1KTN7Z-Yh-4I-FV0Uw.ttf)
    format("truetype");
}
body {
  background: black;
  color: #fff;
  font-family: "Rubik", sans-serif;
}
.main-container {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: black;
  overflow: hidden;
  z-index: 1;
  perspective: 400px;
  transition: opacity 0.3s;
}
.img {
  position: absolute;
  overflow: hidden;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  background-color: transparent;
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  opacity: 0;
}
.title {
  display: block;
  position: absolute;
  width: 200%;
  top: 50%;
  left: -50%;
  transform: translateY(-50%);
  font-size: 6em;
  text-align: center;
  color: #fff;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  opacity: 0;
  z-index: 5;
}
.info-container {
  position: absolute;
  left: 20%;
  top: 0;
  right: 20%;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  text-align: center;
  transform: translateY(100%);
  opacity: 0;
  z-index: 5;
}
.info-container h3 {
  font-size: 2.6em;
  font-weight: 400;
  letter-spacing: 0.05em;
  margin: 0 0 0.5em 0;
  padding: 0;
}
.info-container h4 {
  font-size: 1.7em;
  font-weight: 400;
  margin: 1.4em 0 0.8em 0;
  padding: 0;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}
.info-container h5 {
  font-size: 1.3em;
  font-weight: 300;
  margin: 1.5em 0 0.5em 0;
  padding: 0;
  text-transform: uppercase;
}
.info-container p {
  font-size: 1.2em;
  margin: 0;
  padding: 0;
  line-height: 1.6;
}
.info-container a {
  color: #fff;
  text-decoration: none;
  opacity: 0.6;
  transition: all 0.3s;
}
.info-container a:hover {
  opacity: 1;
}
.main-container.loaded .loader-container {
  display: none;
}
.main-container.loaded .img,
.main-container.loaded .info-container {
  opacity: 1;
}
.main-container.loaded .title {
  opacity: 0;
}
.main-container.loaded .img-1 {
  background-image: url("./img1.jpg");
  animation: kenburns-top 6s linear both reverse 0.5s,
    fade-out 2s ease-in forwards 5.5s;
  z-index: 5;
}
.main-container.loaded .img-2 {
  background-image: url(https://images.unsplash.com/photo-1507941097613-9f2157b69235?ixlib=rb-0.3.5&q=85&fm=jpg&crop=entropy&cs=srgb&s=f8f33afdfc69b16d51c996cf3a8cc1c7);
  animation: kenburns-bottom 6s linear both 5.5s,
    fade-out 2s ease-in forwards 10.5s;
  z-index: 4;
}
.main-container.loaded .img-3 {
  background-image: url(https://images.unsplash.com/photo-1506501139174-099022df5260?ixlib=rb-0.3.5&q=85&fm=jpg&crop=entropy&cs=srgb&s=4868d202b74b7a313bb34a3d8526428c);
  animation: kenburns-right 6s linear both reverse 10.5s,
    fade-out 2s ease-in forwards 15.5s;
  z-index: 3;
}
.main-container.loaded .img-4 {
  background-image: url(https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?ixlib=rb-0.3.5&q=85&fm=jpg&crop=entropy&cs=srgb&s=d8f8d728cc689063536174ec02129ebc);
  animation: kenburns-left 6s linear both 15.5s,
    fade-out 2s ease-in forwards 20.5s;
  z-index: 2;
}
.main-container.loaded .img-5 {
  background-image: url(https://images.unsplash.com/photo-1505814360303-5bfcf2a8acb6?ixlib=rb-0.3.5&q=85&fm=jpg&crop=entropy&cs=srgb&s=86aaa627e11ca46f2177787d563de340);
  animation: kenburns-right 7s linear both reverse 20.5s,
    fade-out 3s ease-in forwards 24.5s;
  z-index: 1;
}
.main-container.loaded .title-1 {
  animation: focus-in-contract 1.3s cubic-bezier(0.25, 0.46, 0.45, 0.94)
      forwards 1.8s,
    text-blur-out 1.2s ease-in forwards 5.5s;
}
.main-container.loaded .title-2 {
  animation: focus-in-contract 1.3s cubic-bezier(0.25, 0.46, 0.45, 0.94)
      forwards 6.8s,
    text-blur-out 1.2s ease-in forwards 10.5s;
}
.main-container.loaded .title-3 {
  animation: focus-in-contract 1.3s cubic-bezier(0.25, 0.46, 0.45, 0.94)
      forwards 11.8s,
    text-blur-out 1.2s ease-in forwards 15.5s;
}
.main-container.loaded .title-4 {
  animation: focus-in-contract 1.3s cubic-bezier(0.25, 0.46, 0.45, 0.94)
      forwards 16.8s,
    text-blur-out 1.2s ease-in forwards 20.5s;
}
.main-container.loaded .title-5 {
  animation: focus-in-contract 1.3s cubic-bezier(0.25, 0.46, 0.45, 0.94)
      forwards 21.8s,
    text-blur-out 1.6s ease-in forwards 25.5s;
}
.main-container.loaded .info-container {
  opacity: 0;
  animation: slide-in-bottom 12s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards
    26.5s;
}
/* ----------------------------------------------
 * Generated by Animista on 2017-12-10 16:42:7
 * w: http://animista.net, t: @cssanimista
 * ---------------------------------------------- */
/**
 * ----------------------------------------
 * animation kenburns-top
 * ----------------------------------------
 */
@keyframes kenburns-top {
  0% {
    transform: scale(1) translateY(0);
    transform-origin: 50% 16%;
  }
  100% {
    transform: scale(1.25) translateY(-15px);
    transform-origin: top;
  }
}
/**
 * ----------------------------------------
 * animation kenburns-bottom
 * ----------------------------------------
 */
@keyframes kenburns-bottom {
  0% {
    transform: scale(1) translateY(0);
    transform-origin: 50% 84%;
  }
  100% {
    transform: scale(1.25) translateY(15px);
    transform-origin: bottom;
  }
}
/**
 * ----------------------------------------
 * animation kenburns-right
 * ----------------------------------------
 */
@keyframes kenburns-right {
  0% {
    transform: scale(1) translate(0, 0);
    transform-origin: 84% 50%;
  }
  100% {
    transform: scale(1.25) translateX(20px);
    transform-origin: right;
  }
}
/**
 * ----------------------------------------
 * animation kenburns-left
 * ----------------------------------------
 */
@keyframes kenburns-left {
  0% {
    transform: scale(1) translate(0, 0);
    transform-origin: 16% 50%;
  }
  100% {
    transform: scale(1.25) translate(-20px, 15px);
    transform-origin: left;
  }
}
/**
 * ----------------------------------------
 * animation focus-in-contract
 * ----------------------------------------
 */
@keyframes focus-in-contract {
  0% {
    letter-spacing: 1em;
    filter: blur(12px);
    opacity: 0;
  }
  100% {
    filter: blur(0px);
    opacity: 1;
  }
}
/**
 * ----------------------------------------
 * animation tracking-in-contract
 * ----------------------------------------
 */
@keyframes tracking-in-contract {
  0% {
    letter-spacing: 1em;
    opacity: 0;
  }
  40% {
    opacity: 0.6;
  }
  100% {
    letter-spacing: normal;
    opacity: 1;
  }
}
/**
 * ----------------------------------------
 * animation fade-out
 * ----------------------------------------
 */
@keyframes fade-out {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
/**
 * ----------------------------------------
 * animation fade-in
 * ----------------------------------------
 */
@keyframes fade-in {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
/**
 * ----------------------------------------
 * animation text-blur-out
 * ----------------------------------------
 */
@keyframes text-blur-out {
  0% {
    filter: blur(0.01);
  }
  100% {
    filter: blur(12px) opacity(0%);
  }
}
/**
 * ----------------------------------------
 * animation slide-in-bottom
 * ----------------------------------------
 */
@keyframes slide-in-bottom {
  0% {
    transform: translateY(100%);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}
/**
 * ----------------------------------------
 * animation rotate-center
 * ----------------------------------------
 */
@keyframes rotate-center {
  0% {
    transform: rotate(0);
  }
  100% {
    transform: rotate(360deg);
  }
}
.preloaded {
  position: absolute;
  bottom: -1px;
  left: -1px;
  width: 1px;
  height: 1px;
  overflow: hidden;
  visibility: hidden;
}
.loader-container {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  text-align: center;
  font-size: 0.9em;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  font-weight: 400;
  color: #fff;
  background: transparent;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  z-index: 5;
}
.loader {
  width: 42px;
  height: 42px;
  margin-bottom: 10px;
  align-self: center;
  border-radius: 50%;
  background: whiteSmoke;
  box-shadow: 0px -10px 25px 0px #ffffff inset;
  background: linear-gradient(to right, #ffffff 50%, transparent 50%);
  opacity: 0.8;
  animation: rotate-center 0.7s infinite linear;
}
.loader:before {
  display: block;
  content: "";
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 39px;
  height: 39px;
  border-radius: 50%;
  background: black;
}
</style>