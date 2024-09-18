<template>
    <div class="header">
        <el-header>
            <div class="title">中国城市大数据后台管理系统</div>
            <span><i class="el-icon-user-solid"></i>{{name}}</span>
        </el-header>
    </div>
</template>
<script>
import { getToken } from '@/utils/setToken.js'
export default {
    data() {
        return {
            name: '',
        }
    },
    created() {
        //生命周期中获取名字，登录时存储的
        this.name = getToken('username')
    }
}
</script>
<style lang="scss" scoped>
.header {
    .el-header {
        background: #263238;
        color: #fff;
        line-height: 60px;
        display: flex;
        justify-content: space-between;
        .title {
            width: 450px;
            margin-left: 40%;
            font-size: 24px;
        }
    }
}
</style>