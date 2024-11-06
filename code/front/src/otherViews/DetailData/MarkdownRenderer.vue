<template>
  <div v-html="compiledMarkdown"></div>
</template>

<script>
import MarkdownIt from "markdown-it";

export default {
  name: "MarkdownRenderer",
  props: {
    markdown: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      md: new MarkdownIt(), // 实例化markdown-it
    };
  },
  computed: {
    compiledMarkdown() {
      return this.md.render(this.markdown); // 将markdown转换为html
    },
  },
};
</script>

<style scoped>
/* 您可以根据需要添加样式来优化Markdown的渲染效果 */
</style>
