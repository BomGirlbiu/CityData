<template>
  <div class="container">
    <!-- <button style="color: black" @click="callApi">发送请求</button> -->
    <div v-if="over" class="response-container">
      <!-- <pre>{{ response.choices[0].message.content }}</pre> -->
      <MarkdownRenderer :markdown="response.choices[0].message.content" />
    </div>
    <MyLottie v-else :animationData="lottieJson" />
  </div>
</template>

<script>
import axios from "axios";
import MarkdownRenderer from "./MarkdownRenderer.vue";
import MyLottie from "./MyLottie.vue";

export default {
  components: {
    MarkdownRenderer,
    MyLottie,
  },
  data() {
    return {
      response: null,
      apiKey: "be1802e7a021dd6a2bbaef64aceef73e.pJ71zWr33pxKumx7", // 替换为你的 {id}.{secret} 格式的 API Key
      //true表示确认response已经回复，不用再显示加载图标
      over: false,
      lottieJson: require("../../assets/json/loading.json"),
    };
  },
  props: {
    analyzedata: Array,
    Question: String,
  },
  computed: {
    analyzed() {
      if (this.analyzedata) {
        return this.analyzedata.map((item) => JSON.stringify(item)).join(",\n");
      } else {
        return "";
      }
    },
  },
  methods: {
    async callApi() {
      try {
        const url = "https://open.bigmodel.cn/api/paas/v4/chat/completions";
        const headers = {
          Authorization: `Bearer ${this.apiKey}`,
          "Content-Type": "application/json",
        };
        const data = {
          model: "glm-4-flash",
          messages: [
            {
              role: "user",
              content: this.Question + this.analyzed,
            },
          ],
        };
        if (this.analyzed == "") {
          this.respons = "";
          return;
        }
        const response = await axios.post(url, data, { headers });
        this.over = true;
        this.response = response.data;
      } catch (error) {
        if (error.message && error.message.status === 429) {
          // console.error("Too many requests. Retrying in 1 second...");
          setTimeout(callApi, 1000); // 1秒后重试
        }
        console.error("API 请求失败:", error);
        this.response = `Error: ${error.message}`;
      }
    },
  },
  created() {
    this.callApi(); // 页面加载时调用 callApi
  },
  watch: {
    analyzed: {
      handler: function (newValue) {
        if (newValue && newValue.length > 0) {
          this.over = false;
          this.callApi(); // 当 analyzedata 发生变化时调用 callApi
        } else {
          this.over = true;
          this.response = "";
        }
      },
      deep: true, // 深度监听数组的变化
    },
    response: {
      handler: function (newValue) {
        if (newValue == "") {
          this.over = false;
        }
      },
    },
  },
};
</script>

<style scoped>
.container {
  position: relative;
  width: 100%; /* 根据需要调整宽度 */
  height: 100%; /* 根据需要调整高度，或者设置为具体值 */
  overflow: hidden; /* 防止内容溢出 */
  display: flex; /* 启用 Flexbox */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}

.response-container {
  /* background-color: #7dabcb; /* 可选：添加背景色以增强可读性 */
  /* color: #ffffff; /* 可选：设置文本颜色 */
}
</style>
