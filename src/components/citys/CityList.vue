<template>
  <div class="cityList">
    <!-- 查询、重置 -->
    <el-form
      :inline="true"
      :model="formInline"
      class="demo-form-inline"
      size="small"
    >
      <el-form-item label="城市" style="display: inline-flex">
        <el-input
          v-model="formInline.cityName"
          placeholder="请输入城市查询"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="find">查询</el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="reset">重置</el-button>
      </el-form-item>
    </el-form>
    <div class="weightListInfo">
      <el-descriptions
        class="margin-top"
        title="权重计算结果"
        :column="5"
        v-if="weightListInfoVisible"
        style="color:red;"
      >
        <el-descriptions-item label="网络传播指数" >{{this.weightList[0]}}</el-descriptions-item>
        <el-descriptions-item label="媒体报道影响力">{{this.weightList[1]}}</el-descriptions-item>
        <el-descriptions-item label="社交媒体影响力">{{this.weightList[2]}}</el-descriptions-item>
        <el-descriptions-item label="国际访客影响力">{{this.weightList[3]}}</el-descriptions-item>
        <el-descriptions-item label="搜索引擎影响力">{{this.weightList[4]}}</el-descriptions-item>
      </el-descriptions>
    </div>
    <el-table :data="compData" border style="width: 100%">
      <el-table-column prop="cityid" label="城市序号" align="center">
      </el-table-column>
      <el-table-column prop="cityName" label="城市" align="center">
      </el-table-column>
      <el-table-column prop="totalrate" label="综合传播指数" align="center">
      </el-table-column>
      <el-table-column prop="network" label="网络传播指数" align="center">
      </el-table-column>
      <el-table-column prop="mediatr" label="媒体报道影响力" align="center">
      </el-table-column>
      <el-table-column prop="social" label="社交媒体影响力" align="center">
      </el-table-column>
      <el-table-column prop="tourism" label="国际访客影响力" align="center">
      </el-table-column>
      <el-table-column prop="searchin" label="搜索引擎影响力" align="center">
      </el-table-column>
      <el-table-column label="操作" align="center">
        <template slot-scope="scope">
          <el-button
            type="primary"
            size="mini"
            icon="el-icon-edit"
            @click="change(scope.row)"
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

    <div class="add">
      <el-button type="info" @click="add()" plain> 添加 </el-button>
    </div>
    <!-- 分页功能的实现 -->
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-sizes="[5, 10, 20, 30, 50]"
      :page-size="pageSize"
      layout="total, sizes, prev, pager, next, jumper"
      :total="total"
    >
    </el-pagination>

    <el-dialog
      :title="state == true ? '添加新闻信息' : this.form.cityName"
      :visible.sync="dialogFormVisible"
      @close="closeInfo('form')"
      width="500px"
    >
      <el-form :model="form" ref="form" >
        <el-form-item label="城市名" prop="cityName" v-show="state">
          <el-input  v-model="form.cityName" autocomplete="off" v-show="state"></el-input>
        </el-form-item>
        <el-form-item label="搜索引擎影响力" prop="searchin">
          <el-input v-model="form.searchin" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="网络传播指数" prop="network">
          <el-input v-model="form.network" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="媒体报道影响力" prop="mediatr">
          <el-input v-model="form.mediatr" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="国际访客影响力" prop="tourism">
          <el-input v-model="form.tourism" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="社交媒体影响力" prop="social">
          <el-input v-model="form.social" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="closeInfo('form')">取 消</el-button>
        <el-button type="primary" @click="sure('form')">确 定</el-button>
      </div>
    </el-dialog>

    <div v-if="isLoading" class="loading-text">加载中...</div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      dialogFormVisible: false,
      weightListInfoVisible:false,
      state:true,
      tableData: [],
      weightList: [],
      currentPage: 1, //当前页数
      pageSize: 10, // 每页显示条数
      total: 0, // 总条数
      row: "",
      formInline: {
        name: "",
      },
      form: {
        cityid: "",
        cityName: "",
        searchin: "",
        network: "",
        mediatr: "",
        tourism: "",
        social: "",
      },
      isLoading: false, // 是否正在加载
    };
  },
  created() {
    this.getData();
    this.find();
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
    async find() {
      console.log("getData被调用了");
      if (this.isLoading) return;
      try {
        this.isLoading = true;
        const response = await axios.get(
          "http://localhost:8081/home/citys/" + this.formInline.cityName
        );
        console.log(response);
        this.tableData = response.data.list; // 假设后端返回的对象中有一个items数组
        this.total = response.data.total;
        this.compData();
      } catch (error) {
        console.error("Error loading data:", error);
      } finally {
        this.isLoading = false;
      }
    },
    reset() {
      console.log(this.formInline);
      this.formInline = {};
      this.getData(this.formInline);
    },
    handleSizeChange(val) {
      this.pageSize = val;
      this.currentPage = 1;
    },
    handleCurrentChange(val) {
      this.currentPage = val;
    },
    //后端需要传递list数据以及total总条数
    async getData() {
      console.log("getData被调用了");
      if (this.isLoading) return;
      try {
        this.isLoading = true;
        const response = await axios.get("http://localhost:8081/home/citys");
        console.log(response);
        this.tableData = response.data.list; // 假设后端返回的对象中有一个items数组
        this.total = response.data.total;
      } catch (error) {
        console.error("Error loading data:", error);
      } finally {
        this.isLoading = false;
      }
    },
    add() {
      this.state = true;
      this.dialogFormVisible = true;
    },

    change(row) {
      this.state=false;
      console.log(row, "row..");
      this.form = { ...row }; //将所选行的属性填入弹出框中
      this.state = false;
      this.dialogFormVisible = true;
    },
    closeInfo(form) {
      console.log(form);
      // this.$refs[form].resetFields();
      this.dialogFormVisible = false;
      this.form = { cityName: '', searchin: '', network: '', mediatr: '', tourism: '', social: '' };
    },

    sure(form) {
      console.log(this.form);
      axios
        .post("http://localhost:8081/home/citys", {
          // cityid: this.form.cityid,
          cityName: this.form.cityName,
          searchin: this.form.searchin,
          network: this.form.network,
          mediatr: this.form.mediatr,
          tourism: this.form.tourism,
          social: this.form.social,
        })
        .then((response) => {
          // 处理成功情况
          this.getData(this.formInline);
          this.closeInfo(form);
          this.weightList = response.data;
          console.log(this.weightList);
          this.weightListInfoVisible=true;
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
            url: "http://localhost:8081/home/citys/" + row.cityid,
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
  },
};
</script>
<style lang="scss" scope>
.cityList {
  .demo-form-inline,
  .el-form-item {
    text-align: left;
  }
  .el-pagination {
    text-align: left;
    margin-top: 20px;
  }
  .el-dialog__header {
    padding: 54px 20px 10px;
  }
  .el-dialog__title {
    font-size: 26px;
  }
  .el-dialog__body {
    padding: 30px 0px 2px 57px;
  }
  .el-dialog {
    border-radius: 30px;
  }
  .el-color-picker__icon,
  .el-input,
  .el-textarea {
    width: 90%;
  }
  .el-input__inner {
    width: 80%;
  }
  .el-form-item__label {
    width: 25%;
    display: flex;
  }
  .dialog-footer {
    display: flex;
    justify-content: center;
  }
  .el-dialog__footer {
    padding: 7px 20px 40px;
  }
  .cityList .el-color-picker__icon,
  .cityList .el-input,
  .cityList .el-textarea {
    width: 110%;
  }
  .el-input--small .el-input__inner {
    width: 100%;
  }
  .add {
    margin-top: 1%;
  }
}
</style>