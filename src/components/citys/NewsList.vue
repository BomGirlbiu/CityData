<template>
  <div class="newsList">
    <el-form :inline="true" class="demo-form-inline" size="small">
      <el-form-item>
        <el-button type="primary" @click="addNews">新增</el-button>
      </el-form-item>
    </el-form>
    <el-table :data="compData" border style="width: 100%">
      <el-table-column prop="newsID" label="新闻ID" align="center">
      </el-table-column>
      <el-table-column prop="province" label="省份" align="center">
      </el-table-column>
      <el-table-column prop="city" label="城市名" align="center">
      </el-table-column>
      <el-table-column prop="title" label="新闻标题" align="center">
      </el-table-column>
      <el-table-column
        prop="newsURL"
        label="新闻URL"
        align="center"
        style="overflow: hidden"
      >
      </el-table-column>
      <el-table-column label="操作" align="center">
        <template slot-scope="scope">
          <el-button
            type="primary"
            size="mini"
            icon="el-icon-edit"
            @click="edit(scope.row)"
          ></el-button>
          <el-button
            type="danger"
            size="mini"
            icon="el-icon-delete"
            @click="del(scope.row)"
          ></el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 分页功能的实现 -->
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-sizes="[10, 20, 50]"
      :page-size="pageSize"
      layout="total, sizes, prev, pager, next, jumper"
      :total="total"
    >
    </el-pagination>

    <el-dialog
      :title="state == true ? '添加新闻信息' : '修改新闻信息'"
      :visible.sync="dialogFormVisible"
      width="500px"
    >
      <el-form :model="form" :rules="rules" ref="form">
        <el-form-item label="城市" :label-width="formLabelWidth" prop="city">
          <el-input v-model="form.city" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item
          label="省份"
          :label-width="formLabelWidth"
          prop="province"
        >
          <el-input v-model="form.province" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="标题" :label-width="formLabelWidth" prop="title">
          <el-input v-model="form.title" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item
          label="新闻URL"
          :label-width="formLabelWidth"
          prop="newsURL"
        >
          <el-input v-model="form.newsURL" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="closeInfo('form')">取 消</el-button>
        <el-button type="primary" @click="sure('form')">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      tableData: [],
      dialogFormVisible: false,
      currentPage: 1, //当前页数
      pageSize: 10, // 每页显示条数
      row: "",

      form: {
        city: "",
        title: "",
        newsURL: "",
      },
      formLabelWidth: "80px",
      formLabelHeight: "40px",
      rules: {
        city: [{ required: true, message: "请输入城市名" }],
        title: [{ required: true, message: "请输入新闻标题" }],
        province: [{ required: true, message: "请输入省份" }],
        newsURL: [{ required: true, message: "请输入新闻URL" }],
      },
      state: true,
      total: 0,
    };
  },
  created() {
    this.getData();
  },
  computed: {
    compData() {
      return this.tableData.slice(
        (this.currentPage - 1) * this.pageSize,
        this.currentPage * this.pageSize
      );
    },
  },
  methods: {
    edit(row) {
      console.log(row);
      this.form = { ...row };
      this.state = false;
      this.dialogFormVisible = true;
    },
    closeInfo(form) {
      console.log(form);
      this.$refs[form].resetFields();
      this.dialogFormVisible = false;
    },
    reset() {
      console.log(this.form);
      this.form = {};
      this.getData(this.form);
    },
    handleSizeChange(val) {
      this.pageSize = val;
      this.currentPage = 1;
    },
    handleCurrentChange(val) {
      this.currentPage = val;
    },
    del(row) {
      console.log(row, "row222..");
      this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          axios({
            method: "DELETE",
            url: "http://localhost:8081/home/news/" + row.newsID,
          })
            .then((response) => {
              if (response.status === 200) {
                this.$message({ message: "删除数据成功", type: "success" });
                this.getData(); // 假设这是重新获取数据的函数
              }
            })
            .catch((error) => {
              this.$message({
                message: "删除数据失败：" + error.message,
                type: "error",
              });
              // done(); // 即使出错也关闭对话框
            });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
    addNews() {
      this.form = {
        city: "",
        title: "",
        newsURL: "",
      };
      this.state = true;
      this.dialogFormVisible = true;
      axios
        .post("http://localhost:8081/home/news", {
          newsID: 999999,
          title: this.form.title,
          city: this.form.city,
          province: this.form.province,
          newsURL: this.form.newsURL,
        })
        .then((response) => {
          // 处理成功情况
          this.getData(this.formInline);
          this.dialogFormVisible = false;

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
    async getData() {
      console.log("getData被调用了");
      if (this.isLoading) return;
      try {
        this.isLoading = true;
        const response = await axios.get("http://localhost:8081/home/news");
        console.log(response);
        this.tableData = response.data.cityNewsList; // 假设后端返回的对象中有一个items数组
        this.total = response.data.total;
      } catch (error) {
        console.error("Error loading data:", error);
      } finally {
        this.isLoading = false;
      }
    },
    // 提交修改信息
    sure(form) {
      console.log(this.form);
      axios
        .post("http://localhost:8081/home/news", {
          newsID: this.form.newsID,
          title: this.form.title,
          province: this.form.province,
          city: this.form.city,
          newsURL: this.form.newsURL,
        })
        .then((response) => {
          // 处理成功情况
          this.getData(this.formInline);
          this.dialogFormVisible = false;

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
<style lang="scss">
.newsList {
  .demo-form-inline,
  .el-form-item {
    text-align: left;
  }
}
</style>