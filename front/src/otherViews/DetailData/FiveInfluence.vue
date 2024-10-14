<template>
  <div class="influence">
    <div class="bar">
      <el-progress
        :text-inside="true"
        :stroke-width="20"
        :percentage="70"
        text-color="white"
      ></el-progress>
      <br />
      <el-progress
        :text-inside="true"
        :stroke-width="20"
        :percentage="100"
        status="success"
        text-color="white"
      ></el-progress>
      <br />
      <el-progress
        :text-inside="true"
        :stroke-width="20"
        :percentage="80"
        status="warning"
        text-color="white"
      ></el-progress>
      <br />

      <el-progress
        :text-inside="true"
        :stroke-width="20"
        :percentage="50"
        status="exception"
        text-color="white"
      ></el-progress>
      <br />
      <el-progress
        :text-inside="true"
        :stroke-width="20"
        :percentage="70"
        text-color="white"
      ></el-progress>
    </div>
  </div>
</template>
<script>
export default {
  name: "FiveInfluence",
};
</script>
<style scoped>
.influence {
  width: 30%;
  height: 100%;
}
</style>
