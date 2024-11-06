<template>
  <div>
    <h1>视频生成</h1>
    <textarea
      v-model="prompt"
      placeholder="请输入视频的文本描述"
      rows="10"
      cols="50"
    ></textarea>
    <br />
    <input
      type="file"
      @change="onFileChange"
      accept="image/png, image/jpeg, image/jpg"
    />
    <br />
    <button @click="generateVideo">生成视频</button>
    <br />
    <div v-if="videoUrl">
      <h2>生成的视频</h2>
      <video controls>
        <source :src="videoUrl" type="video/mp4" />
        您的浏览器不支持 video 标签。
      </video>
      <br />
      <img :src="coverImageUrl" alt="视频封面" />
    </div>
    <div v-if="taskStatus === 'PROCESSING'">
      <p>视频正在生成中...</p>
    </div>
    <div v-if="taskStatus === 'FAIL'">
      <p>视频生成失败。</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      prompt: "",
      imageUrl: "",
      videoUrl: "",
      coverImageUrl: "",
      taskId: "",
      taskStatus: "",
    };
  },
  methods: {
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.imageUrl = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
    async generateVideo() {
      const data = {
        model: "cogvideox",
        prompt: this.prompt,
        image_url: this.imageUrl,
      };

      try {
        const response = await axios.post(
          "https://open.bigmodel.cn/api/paas/v4/videos/generations",
          data,
          {
            headers: {
              "Content-Type": "application/json",
              Authorization:
                "be1802e7a021dd6a2bbaef64aceef73e.pJ71zWr33pxKumx7", // 请替换为您的API Key
            },
          }
        );
        this.taskId = response.data.id;
        this.taskStatus = response.data.task_status;

        if (this.taskStatus === "PROCESSING") {
          this.pollForTaskStatus(this.taskId);
        }
      } catch (error) {
        console.error("Error generating video:", error);
      }
    },
    async pollForTaskStatus(taskId) {
      const interval = setInterval(async () => {
        try {
          const response = await axios.get(
            `https://open.bigmodel.cn/api/paas/v4/async-result/${taskId}`,
            {
              headers: {
                Authorization:
                  "be1802e7a021dd6a2bbaef64aceef73e.pJ71zWr33pxKumx7", // 请替换为您的API Key
              },
            }
          );

          this.taskStatus = response.data.task_status;
          if (this.taskStatus !== "PROCESSING") {
            clearInterval(interval);
            if (this.taskStatus === "SUCCESS") {
              this.videoUrl = response.data.video_result[0].url;
              this.coverImageUrl =
                response.data.video_result[0].cover_image_url;
            }
          }
        } catch (error) {
          console.error("Error polling for task status:", error);
          clearInterval(interval);
        }
      }, 5000); // 每5秒轮询一次
    },
  },
};
</script>

<style>
textarea {
  width: 100%;
  max-width: 600px;
  margin-bottom: 10px;
}
</style>
