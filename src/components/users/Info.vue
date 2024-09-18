<template>
  <div class="info">
    <el-descriptions
      class="margin-top"
      title="个人信息"
      :column="3"
      :size="size"
      border
    >
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-star-off"></i>
          用户ID
        </template>
        {{ this.userInfo.id }}
      </el-descriptions-item>

      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-user"></i>
          用户名
        </template>
        {{ this.userInfo.name }}
      </el-descriptions-item>

      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-unlock"></i>
          密码
        </template>
        {{ this.userInfo.password }}
      </el-descriptions-item>

      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-mobile-phone"></i>
          手机号
        </template>
        {{ this.userInfo.phone }}
      </el-descriptions-item>

      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-message"></i>
          邮箱
        </template>
        {{ this.userInfo.email }}
      </el-descriptions-item>

      <template slot="extra">
        <el-form :inline="true" class="demo-form-inline" size="small">
          <el-form-item>
            <!-- <el-button type="primary" @click="addStudent">新增</el-button> -->
            <el-button
              type="info"
              icon="el-icon-edit"
              @click="updateUserInfo"
              circle
            ></el-button>
          </el-form-item>
        </el-form>
      </template>
    </el-descriptions>

    <!-- 修改用户信息的模态框 -->
    <el-dialog
      title="修改个人信息"
      :visible.sync="dialogFormVisible"
      width="500px"
    >
      <el-form
        @submit.prevent="updateUserInfo"
        :model="ruleForm"
        ref="ruleForm"
        :rules="rules"
      >
        <el-form-item label="用户名" prop="name">
          <el-input
            type="text"
            v-model="ruleForm.name"
            autocomplete="off"
          ></el-input>
        </el-form-item>

        <el-form-item label="密码" prop="password">
          <el-input
            type="password"
            v-model="ruleForm.password"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="spassword">
          <el-input
            type="password"
            v-model="ruleForm.spassword"
            autocomplete="off"
          ></el-input>
        </el-form-item>

        <el-form-item label="手机号" prop="phone">
          <el-input
            type="phone"
            v-model="ruleForm.phone"
            autocomplete="off"
          ></el-input>
        </el-form-item>

        <el-form-item label="邮箱" prop="email">
          <el-input
            type="email"
            v-model="ruleForm.email"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="postUserInfo">提交</el-button>
          <el-button @click="closeModal">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>
<script>
import axios from "axios";

import { getToken } from "@/utils/setToken.js";
import { setToken } from "@/utils/setToken.js";

import {
  phoneRule,
  // passRule,
  nameRule,
  emailRule,
} from "@/utils/vaildate.js";
export default {
  data() {
    var passRule = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.ruleForm.checkPass !== "") {
          this.$refs.ruleForm.validateField("password");
        }
        callback();
      }
    };
    var spassRule = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.ruleForm.password) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };

    return {
      // vm: this,
      //隐藏修改的弹窗
      dialogFormVisible: false,
      //显示用户个人信息
      userInfo: {
        name:getToken("name"),
        password:"",
        phone:getToken("phone"),
        email:getToken("email"),
        id:getToken("id"),
      },
      // 用于编辑的用户信息，初始时与原始信息相同
      editUserInfo: {
        ...this.userInfo,
      },
      //修改信息页面
      ruleForm: {
        name: "",
        password: "",
        spassword: "",
        email: "",
      },
      rules: {
        phone: [{ validator: phoneRule, trigger: "blur" }],
        password: [{ validator: passRule, trigger: "blur" }],
        spassword: [{ validator: spassRule, trigger: "blur" }],
        email: [{ validator: emailRule, trigger: "blur" }],
        name: [{ validator: nameRule, trigger: "blur" }],
      },
      // dynamicValidateForm: {
      //   domains: [
      //     {
      //       value: "",
      //     },
      //   ],
      //   email: "",
      // },
    };
  },
  created() {
    this.id = getToken("id");
    this.getAdmin();
    // this.userInfo.name = getToken("name");
    // this.password = getToken("password");
    // this.phone = getToken("phone");
    // this.email = getToken("email");

    // this.menus = [...this.$router.options.routes]
    // // console.log(this.$router.options.routes)
    // // 权限管理和动态路由的思路：
    // // 根据不同的用户登录上来,返回对应的路由权限菜单
    // // 一般可以通过树形控件达到权限的精准控制，根据不同角色，勾选不同的菜单权限，将菜单数据提交给后端进行保存
    // // 后端保存之后，在用户进行登录的时候就会查询该用户或该角色所拥有的菜单数据，最终进行动态的渲染展示。
    // // 动态添加路由使用router.addRoutes(vue-router3.x版本方法,已废弃)方法,后续使用router.addRoute进行动态路由添加
  },
  methods: {
    // 获取用户信息
    getAdmin() {
      axios
        .get("http://localhost:8081/users/info/" + this.id)
        .then((response) => {
          // 处理成功情况
          this.userInfo.name=response.data.name
          setToken("username",this.userInfo.name)
          this.userInfo.phone=response.data.phone
          this.userInfo.email=response.data.email
          this.userInfo.password=response.data.password
          // const admin = response.data[0];
          // console.log("111",admin.data)s
          // setToken("name", admin.name);
          // setToken("phone", admin.phone);
          // setToken("email", admin.email);
          // setToken("password", admin.password);
        })
        .catch((error) => {
          // 处理错误情况
          console.error("Error:", error);
          alert("获取用户信息失败");
        });
      // this.userInfo.name = getToken("name");
      // this.userInfo.password = getToken("password");
      // this.userInfo.phone = getToken("phone");
      // this.userInfo.email = getToken("email");
    },
    //修改信息
    updateUserInfo() {
      this.dialogFormVisible = true; //显示修改弹窗
      console.log(this.dialogFormVisible);
      // 这里编写更新用户信息的逻辑
      // 例如，发送一个API请求到后端来更新用户信息
      console.log("Updating user info:", this.editUserInfo);
      //this.closeModal();
    },
    //关闭弹窗
    closeModal() {
      this.dialogFormVisible = false;
      // 如果需要重置editUserInfo，可以在这里设置
      // this.editUserInfo = { name: '', email: '' };
    },
    //提交修改信息
    postUserInfo() {
      axios
        .post("http://localhost:8081/users/info", {
          id: this.id,
          name: this.ruleForm.name,
          password: this.ruleForm.password,
          phone: this.ruleForm.phone,
          email: this.ruleForm.email,
        })
        .then((response) => {
          // 处理成功情况
          this.dialogFormVisible = false;
          this.getAdmin();
          this.$message({
            type: "success",
            message: "修改成功!",
          });
        })
        .catch((error) => {
          // 处理错误情况
          console.error("Error:", error);
          alert("There was an error submitting the form!");
        });
    },
  },
};
</script>
<style lang="scss" scoped>
.modal {
  /* 模态框的样式 */
  position: fixed;
  top: 50%;
  background-color: black;
  left: 50%;
  transform: translate(-50%, -50%);
  /* 其他样式 */
}
</style>