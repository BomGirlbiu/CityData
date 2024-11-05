<template>
    <div class="app-container">
      <el-row :gutter="10" class="mb8">
        <el-col :span="1.5">
          <el-button
            type="primary"
            plain
            icon="el-icon-bug"
            size="mini"
            @click="fetch()"
            v-hasPermi="['system:post:add']"
            >爬取</el-button
          >
        </el-col>
        <el-col :span="1.5">
          <el-button
            type="warning"
            plain
            icon="el-icon-download"
            size="mini"
            @click="handleExport"
            v-hasPermi="['system:post:export']"
            >导出</el-button
          >
        </el-col>
        <right-toolbar
          :showSearch.sync="showSearch"
          @queryTable="getList"
        ></right-toolbar>
      </el-row>
  
      <el-table
        v-loading="loading"
        :data="cityTravelList"
        @selection-change="handleSelectionChange"
      >
        <el-table-column label="编号" align="center" prop="id" />
        <el-table-column label="省份" align="center" prop="province" />
        <el-table-column label="城市" align="center" prop="city" />
        <el-table-column label="标题" align="center" prop="title"/>
        <el-table-column label="内容" align="center" prop="content"/>
        <el-table-column label="链接" align="center" prop="src" />
        <el-table-column label="图片" align="center" prop="img" />
      </el-table>
  
      <pagination
        v-show="total > 0"
        :total="total"
        :page.sync="queryParams.pageNum"
        :limit.sync="queryParams.pageSize"
        @pagination="getList"
      />
    </div>
  </template>
  
  <script>
  import {
    listDept,
    getPost,
    delPost,
    addPost,
    updatePost,
    fetchCityTravel,
  } from "@/api/system/dept";
  
  export default {
    name: "Post",
    dicts: ["sys_normal_disable"],
    data() {
      return {
        // 遮罩层
        loading: true,
        // 选中数组
        postIds: [],
        // 非单个禁用
        single: true,
        // 非多个禁用
        multiple: true,
        // 显示搜索条件
        showSearch: true,
        // 总条数
        total: 0,
        // 岗位表格数据
        cityTravelList: [],
        // 弹出层标题
        title: "",
        // 是否显示弹出层
        open: false,
        dialogContent: "", // 要显示的内容
        dialogVisible: false, // 控制弹窗显示
        // 查询参数
        queryParams: {
          pageNum: 1,
          pageSize: 10,
          id: undefined,
          userId: undefined,
          essence: undefined,
        },
      };
    },
    created() {
      this.getList();
    },
    methods: {
      /** 点击显示作品内容 */
      showContent(content) {
        this.dialogContent = content; // 存储要显示的内容
        this.dialogVisible = true; // 控制弹窗显示
      },
      generateRandomString(length) {
        return Math.floor(Math.random() * (max - min + 1) + min);
      },
      /** 查询作品列表 */
      getList() {
        this.loading = true;
        listDept(this.queryParams).then((response) => {
          this.cityTravelList = response.data;
          console.log(this.cityTravelList);
          this.total=2;
          this.loading = false;
        });
      },
      /**爬取 */
      fetch(){
        this.$confirm('是否爬取城市旅游所有信息？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          fetchCityTravel().then(response => {
            if (response.code == 200){
              this.$message({
                message: '爬取成功',
                type: 'success'
              });
              this.getList();
            }
            else {
              this.$message({
                message: '爬取失败',
                type: 'error'
              });
            }
          })
        })
      },
      // 取消按钮
      cancel() {
        this.open = false;
        this.reset();
      },
      // 表单重置
      reset() {
        this.form = {
          // id: undefined,
          title: undefined,
          userId: undefined,
          content: "",
          essence: false,
          // remark: undefined
        };
        this.resetForm("form");
      },
      /** 搜索按钮操作 */
      handleQuery() {
        this.queryParams.pageNum = 1;
        this.getList();
      },
      /** 重置按钮操作 */
      resetQuery() {
        this.resetForm("queryForm");
        this.handleQuery();
      },
      // 多选框选中数据
      handleSelectionChange(selection) {
        this.postIds = selection.map((item) => item.postId);
        this.single = selection.length != 1;
        this.multiple = !selection.length;
      },
      /** 新增按钮操作 */
      handleAdd() {
        this.reset();
        this.open = true;
        this.title = "添加作品";
      },
      /** 修改按钮操作 */
      handleUpdate(row) {
        this.reset();
        const postId = row.postId
        // const id = row.id || this.ids;
        getPost(postId).then((response) => {
          this.form = response.data;
          this.open = true;
          this.title = "修改岗位";
        });
      },
      /** 提交按钮 */
      submitForm: function () {
        this.$refs["form"].validate((valid) => {
          if (valid) {
            if (this.form.postId != undefined) {
              console.log(this.form)
              updatePost(this.form).then((response) => {
                this.$modal.msgSuccess("修改成功");
                this.open = false;
                this.getList();
              });
            } else {
              addPost(this.form).then((response) => {
                this.$modal.msgSuccess("新增成功");
                this.open = false;
                this.getList();
              });
            }
          }
        });
      },
      /** 删除按钮操作 */
      handleDelete(row) {
        const postIds = row.postId || this.postIds;
        this.$modal
          .confirm('是否确认删除岗位编号为"' + postIds + '"的数据项？')
          .then(function () {
            return delPost(postIds);
          })
          .then(() => {
            this.getList();
            this.$modal.msgSuccess("删除成功");
          })
          .catch(() => {});
      },
      /** 导出按钮操作 */
      handleExport() {
        this.download(
          "system/city/food/export",
          {
            ...this.queryParams,
          },
          `post_city_food.xlsx`
        );
      },
    },
  };
  </script>
  