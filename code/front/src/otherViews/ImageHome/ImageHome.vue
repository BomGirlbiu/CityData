<template>
  <div
    style="
      background-color: #f5f5f5;
      color: #333;
      font-family: Arial, sans-serif;
    "
  >
    <div style="max-width: 800px; margin: 0 auto; padding: 20px">
      <h1 style="color: #555">视频生成</h1>
      <textarea
        v-model="prompt"
        placeholder="请输入视频的文本描述"
        rows="10"
        cols="50"
        style="
          width: 100%;
          max-width: 100%;
          background-color: #eee;
          border: 1px solid #ccc;
          color: #666;
        "
      ></textarea>
      <br /><br />
      <label
        for="fileInput"
        style="display: block; color: #555; margin-bottom: 10px"
        >选择封面图片:</label
      >
      <input
        id="fileInput"
        type="file"
        @change="onFileChange"
        accept="image/png, image/jpeg, image/jpg"
        style="background-color: #eee; border: 1px solid #ccc; color: #666"
      />
      <br /><br />
      <button
        @click="generateVideo"
        style="
          background-color: #ddd;
          border: none;
          color: #333;
          padding: 10px 20px;
          cursor: pointer;
        "
      >
        生成视频
      </button>
      <br /><br />
      <div v-if="videoUrl" style="margin-top: 20px">
        <h2 style="color: #555">生成的视频</h2>
        <video controls style="width: 100%; max-width: 100%">
          <source :src="videoUrl" type="video/mp4" />
          您的浏览器不支持 video 标签。
        </video>
        <br /><br />
        <img
          :src="coverImageUrl"
          alt="视频封面"
          style="width: 100%; max-width: 100%; margin-top: 10px"
        />
      </div>
      <div v-if="taskStatus === 'PROCESSING'" style="margin-top: 20px">
        <p style="color: #555">视频正在生成中...</p>
      </div>
      <div v-if="taskStatus === 'FAIL'" style="margin-top: 20px">
        <p style="color: #555">视频生成失败。</p>
      </div>
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
