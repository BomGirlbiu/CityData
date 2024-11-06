<template>
  <div id="common-video" class="h-100">
    <div :class="{ isShow: control }" class="h-100">
      <video
        ref="myVideo"
        :poster="poster"
        :src="src"
        :controls="controls"
        oncontextmenu="return false"
        @timeupdate="timeupdate"
        controlslist="nodownload"
        class="video-box"
      ></video>
      <img
        src="https://p5.img.cctvpic.com/photoworkspace/2024/09/19/2024091910130313801.jpg"
        alt=""
        @click="operateVideo"
        class="pointer operate-btn"
        :class="{ 'fade-out': videoState }"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "CommonVideo",
  data() {
    return {
      videoState: false, // 视频播放状态
      // 学时
      studyTime: {
        currentTime: 0, // 当前已学时长
        duration: 0 // 总时长
      },
      timer: {}, // 定时器
      pauseTimer: {} // 暂停定时器
    };
  },
  /**
   * @param poster 展示图
   * @param src 视频资源
   * @param controls 是否显示控件
   * @param control 控件控制
   * @param videoData 视频基础数据
   */
  props: {
    poster: {
      type: String,
      required: false,
      default: ""
    },
    src: {
      type: String,
      required: true
    },
    controls: {
      type: Boolean,
      required: false,
      default: true
    },
    control: {
      type: Boolean,
      required: false,
      default: false
    },
    videoData: {
      type: Object,
      required: true
    }
  },
  mounted() {
    // 监听视频播放
    this.$refs.myVideo.addEventListener("play", () => {
      console.log("video is playing");
      this.openTimer();
    });
    // 监听视频暂停
    this.$refs.myVideo.addEventListener("pause", () => {
      console.log("video is stop");
      this.closeTimer();
    });
  },
  methods: {
    // 开启定时器
    openTimer() {
      this.timer = setInterval(() => {
        this.$emit("videoStudyTime", this.studyTime);
      }, 5000);
    },
    // 关闭定时器
    closeTimer() {
      clearInterval(this.timer);
      this.$emit("videoStudyTime", this.studyTime);
    },
    // 开启暂停定时器
    openPauseTimer() {
      this.pauseTimer = setInterval(() => {
        this.hintOperate();
      }, 600000);
    },
    // 关闭暂停定时器
    closePauseTimer() {
      clearInterval(this.pauseTimer);
    },
    // 提示操作
    hintOperate() {
      this.operateVideo();
      this.$alert("请点击确认继续学习", "提示", {
        confirmButtonText: "确定",
        confirmButtonClass: "hint-btn",
        showClose: false,
        callback: action => {
          this.$refs.myVideo.currentTime = this.videoData.currentTime;
          this.operateVideo();
          this.openPauseTimer();
        }
      });
    },
    // 获取当前播放位置
    timeupdate(e) {
      this.studyTime.currentTime = e.target.currentTime;
      this.studyTime.duration = e.target.duration ? e.target.duration : 0;
    },
    // 操作视频播放、暂停
    operateVideo() {
      if (!this.src) {
        this.$message({ message: "暂无视频资源，请查看其他视频！" });
        return false;
      }
      if (this.$refs.myVideo.paused) {
        this.$refs.myVideo.play();
        this.videoState = true;
      } else {
        this.$refs.myVideo.pause();
        this.videoState = false;
      }
    }
  },
  watch: {
    // 监听操作
    videoData(val, oldVal) {
      const { currentTime, duration } = val;
      if (currentTime && duration && currentTime < duration) {
        this.hintOperate();
      }
    }
  }
};
</script>

<style lang="scss" scope>
#common-video {
  position: relative;
  .video-box {
    box-sizing: border-box;
    border: 0;
    display: block;
    width: 100%;
    height: 100%;
    outline: none !important;
  }
  .isShow {
    //进度条
    video::-webkit-media-controls-timeline {
      display: none;
    }
  }
  video::-webkit-media-controls-play-button {
    visibility: hidden;
  }
  .operate-btn {
    display: block;
    width: 60px;
    height: 60px;
    position: absolute;
    top: calc(50% - 30px);
    left: calc(50% - 30px);
  }
  .operate-btn:hover {
    opacity: 0.8;
  }
  .fade-out {
    opacity: 0;
  }
}
</style>