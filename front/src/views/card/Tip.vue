<template>
  <el-card class="box-card" shadow="never">
    <div slot="header">
      <span>🥳 推荐作品</span>
    </div>
    <!-- <div>
      <p v-for="(item, index) in tip" :key="index" class="block">
        <a :href="tip.link" target="_blank">{{ tip.title }}</a>
        <a :href="tip.link" target="_blank">{{ tip.title }}</a>
      </p>
    </div> -->
<el-table
      :data="tip"
      style="width: 100%">
      <el-table-column
        prop="title"
        label="作品"
        width="180">
      </el-table-column>
      <el-table-column
        prop="author"
        label="作者"
        width="180">
      </el-table-column>
    </el-table>
    <!-- <div>
      <div class="has-text-left block">
        {{ tip.title }}
      </div>
      <div class="has-text-right mt-5 block">
        ——{{ tip.author }}
      </div>
    </div> -->
  </el-card>
</template>

<script>
import {getTodayTip} from '@/api/tip'

export default {
  name: 'Tip',
  data() {
    return {
      tip: []
    }
  },
  created() {
    this.fetchTodayTip()
  },
  methods: {
    fetchTodayTip() {
      getTodayTip().then(response => {
        const { data } = response
        this.tip = data

        console.log(typeof(this.tip))
      })
    }
  }
}
</script>

<style scoped>

</style>
