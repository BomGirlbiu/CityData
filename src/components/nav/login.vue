<template>
  <div class="login">
    <div class="square" style="--i: 0"></div>
    <div class="square" style="--i: 1"></div>
    <div class="square" style="--i: 2"></div>
    <div class="square" style="--i: 3"></div>
    <div class="square" style="--i: 4"></div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span class="title">管理员登录界面</span>
      </div>
      <el-form label-width="40px" :model="form" ref="form" :rules="rules">
        <el-form-item label="" prop="phone">
          <el-input v-model="form.phone" placeholder="手机号"></el-input>
        </el-form-item>
        <el-form-item label="" prop="password">
          <el-input
            type="password"
            v-model="form.password"
            placeholder="密码"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <div style="margin-top: 5%; height: 50px">
            <el-button
              style="font-size: 20px; color: gray"
              type="primary"
              @click="login('form')"
              >登录</el-button
            >
          </div>
          <div class="zhuce">
            <router-link
              style="color: #ffffffa3; font-size: 15px"
              to="/index/register"
              >点击这里,申请成为管理员</router-link
            >
          </div>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>
<script>
import { phoneRule, passRule } from "@/utils/vaildate.js";
import { setToken } from "@/utils/setToken.js";
import { getToken } from "@/utils/setToken.js";
import axios from "axios";

export default {
  data() {
    return {
      form: {
        phone: "",
        password: "",
      },
      rules: {
        phone: [{ validator: phoneRule, trigger: "blur" }],
        password: [{ validator: passRule, trigger: "blur" }],
      },
    };
  },
  methods: {
    login(form) {
      this.$refs[form].validate((valid) => {
        if (valid) {
          console.log(this.form);
          axios
            .post("http://localhost:8081/index/login", {
              phone: this.form.phone,
              password: this.form.password,
            })
            .then((response) => {
              setToken("id", response.data.id);
              setToken("username", response.data.name);
              this.$message({
                type: "success",
                message: "登录成功!",
              });
              this.$router.push("/home");
            })
            .catch((error) => {
              // 处理错误情况
              console.error("Error:", error);
              alert("用户名或密码错误！");
            });
        } else {
          console.error(this.form);
        }
      });
    },
  },
};
</script>
<style lang="scss">
.login {
  width: 100%;
  margin: 0%;
  height: 100%;
  position: absolute;
  .container {
    width: 107%;
    position: absolute;
    margin-left: 13%;
    margin-right: 4%;
    margin-top: 4%;
  }

  .square {
    position: absolute;
    backdrop-filter: blur(5px);
    box-shadow: 0 25px 45px rgb(0, 0, 0, 0.1);
    border: 1px solid rgb(255, 255, 255, 0.5);
    border-right: 1px solid rgb(255, 255, 255, 0.2);
    border-bottom: 1px solid rgb(255, 255, 255, 0.2);
    background: rgb(255, 255, 255, 0.1);
    border-radius: 10px;
    animation: animate 10s linear infinite;
    animation-delay: calc(-1s * var(--i));
  }

  @keyframes animate {
    0%,
    100% {
      transform: translateY(-40px);
    }
    50% {
      transform: translate(40px);
    }
  }
  .square:nth-child(1) {
    top: 17%;
    right: 31%;
    width: 100px;
    height: 100px;
  }
  .square:nth-child(2) {
    top: 44%;
    left: 21%;
    width: 120px;
    height: 120px;
    z-index: 2;
  }
  .square:nth-child(3) {
    bottom: 17%;
    right: 27%;
    width: 80px;
    height: 80px;
    z-index: 2;
  }
  .square:nth-child(4) {
    bottom: 14%;
    left: 36%;
    width: 50px;
    height: 50px;
  }
  .square:nth-child(5) {
    top: 19%;
    left: 39%;
    width: 60px;
    height: 60px;
  }
  .el-card {
    position: absolute;
    width: 400px;
    min-height: 400px;
    background: rgb(255, 255, 255, 0.1);
    border-radius: 10px;
    // display: flex;
    justify-content: center;
    align-items: center;
    backdrop-filter: blur(5px);
    box-shadow: 0 25px 45px rgb(0, 0, 0, 0.1);
    border: 1px solid rgb(255, 255, 255, 0.5);
    border-right: 1px solid rgb(255, 255, 255, 0.2);
    border-bottom: 1px solid rgb(255, 255, 255, 0.2);
  }
  .box-card {
    width: 450px;
    margin: 200px auto;
    // color: #fff;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
    position: relative;
    padding: 40px;

    .title {
      position: relative;
      color: #fff;
      font-size: 27px;
      font-weight: 600;
      letter-spacing: 6px;
      margin-bottom: 40px;
    }

    .el-form .el-form-item__label {
      color: #fff;
      font-size: 18px;
    }
    .el-card__header {
      width: 100%;
      display: inline-block;
      font-size: 34px;
    }
    .el-card__body,
    .el-main {
      padding: 9px;
      display: flex;
      flex-wrap: nowrap;
      justify-content: flex-start;
      margin-top: 6%;
    }
    .el-input {
      width: 100%;
      background: rgb(255, 255, 255, 0.2);
      border: none;
      outline: none;
      padding: 0px 20px;
      border-radius: 35px;
      border: 1px solid rgb(255, 255, 255, 0.5);
      border-right: 0px solid rgb(255, 255, 255, 0.2);
      border-bottom: 1px solid rgb(255, 255, 255, 0.2);
      font-size: 16px;
      letter-spacing: 1px;
      color: #fff;
      box-shadow: 0 5px 15px rgb(0, 0, 0, 0.05);
    }
    .el-input__inner {
      background-color: #ff20;
      border: 0px solid #dcdfe6;
    }
    .el-button {
      width: 100%;
      background: linear-gradient(-200deg, #dcdcdc, #696969);
      background: #fff;
      color: #666;
      max-width: 100px;
      cursor: pointer;
      margin-bottom: 20px;
      font-weight: 600;
      border-radius: 35px;
    }
    .el-button:hover {
      background: linear-gradient(-200deg, #dcdcdc, #696969);
    }
    .zhuce {
      color: #ffffff91;
      text-decoration: none;
      font-size: 8px;
      margin-top: 3%;
    }
  }
}
</style>