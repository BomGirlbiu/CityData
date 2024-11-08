<template>
  <div class="app-container">
    <el-form :model="queryParams" ref="queryForm" size="small" :inline="true" v-show="showSearch" label-width="68px">
      <el-form-item label="城市编号" prop="cityID">
        <el-input
          v-model="queryParams.cityID"
          placeholder="请输入城市编号"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="城市名" prop="cityName">
        <el-input
          v-model="queryParams.cityName"
          placeholder="请输入城市名"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <!-- <el-form-item label="搜索引擎影响力" prop="searchin">
        <el-input
          v-model="queryParams.searchin"
          placeholder="请输入搜索引擎影响力"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="网络传播影响力" prop="network">
        <el-input
          v-model="queryParams.network"
          placeholder="请输入网络传播影响力"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="媒体报道影响力" prop="mediatr">
        <el-input
          v-model="queryParams.mediatr"
          placeholder="请输入媒体报道影响力"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="国际访客影响力" prop="tourism">
        <el-input
          v-model="queryParams.tourism"
          placeholder="请输入国际访客影响力"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="社交媒体影响力" prop="social">
        <el-input
          v-model="queryParams.social"
          placeholder="请输入社交媒体影响力"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="综合城市传播指数" prop="totalrate">
        <el-input
          v-model="queryParams.totalrate"
          placeholder="请输入综合城市传播指数"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item> -->
      <el-form-item>
        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">更新</el-button>
      </el-form-item>
    </el-form>

    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button
          type="primary"
          plain
          icon="el-icon-plus"
          size="mini"
          @click="handleAdd"
          v-hasPermi="['system:cityattributes:add']"
        >新增</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="success"
          plain
          icon="el-icon-edit"
          size="mini"
          :disabled="single"
          @click="handleUpdate"
          v-hasPermi="['system:cityattributes:edit']"
        >修改</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="danger"
          plain
          icon="el-icon-delete"
          size="mini"
          :disabled="multiple"
          @click="handleDelete"
          v-hasPermi="['system:cityattributes:remove']"
        >删除</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="warning"
          plain
          icon="el-icon-download"
          size="mini"
          @click="handleExport"
          v-hasPermi="['system:cityattributes:export']"
        >导出</el-button>
      </el-col>
      <right-toolbar :showSearch.sync="showSearch" @queryTable="getList"></right-toolbar>
    </el-row>

    <el-table v-loading="loading" :data="cityattributesList" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55" align="center" />
      <el-table-column label="城市编号" align="center" prop="cityID" />
      <el-table-column label="城市名" align="center" prop="cityName" />
      <el-table-column label="搜索引擎影响力" align="center" prop="searchin" />
      <el-table-column label="网络传播影响力" align="center" prop="network" />
      <el-table-column label="媒体报道影响力" align="center" prop="mediatr" />
      <el-table-column label="国际访客影响力" align="center" prop="tourism" />
      <el-table-column label="社交媒体影响力" align="center" prop="social" />
      <el-table-column label="综合城市传播指数" align="center" prop="totalrate" />
      <el-table-column label="操作" align="center" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleUpdate(scope.row)"
            v-hasPermi="['system:cityattributes:edit']"
          >修改</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-delete"
            @click="handleDelete(scope.row)"
            v-hasPermi="['system:cityattributes:remove']"
          >删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    
    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="queryParams.pageNum"
      :limit.sync="queryParams.pageSize"
      @pagination="getList"
    />

    <!-- 添加或修改城市传播指数对话框 -->
    <el-dialog :title="title" :visible.sync="open" width="500px" append-to-body>
      <el-form ref="form" :model="form" :rules="rules" label-width="80px">
        <el-form-item label="城市名" prop="cityName">
          <el-input v-model="form.cityName" placeholder="请输入城市名" />
        </el-form-item>
        <el-form-item label="搜索引擎影响力" prop="searchin">
          <el-input v-model="form.searchin" placeholder="请输入搜索引擎影响力" />
        </el-form-item>
        <el-form-item label="网络传播影响力" prop="network">
          <el-input v-model="form.network" placeholder="请输入网络传播影响力" />
        </el-form-item>
        <el-form-item label="媒体报道影响力" prop="mediatr">
          <el-input v-model="form.mediatr" placeholder="请输入媒体报道影响力" />
        </el-form-item>
        <el-form-item label="国际访客影响力" prop="tourism">
          <el-input v-model="form.tourism" placeholder="请输入国际访客影响力" />
        </el-form-item>
        <el-form-item label="社交媒体影响力" prop="social">
          <el-input v-model="form.social" placeholder="请输入社交媒体影响力" />
        </el-form-item>
        <el-form-item label="综合城市传播指数" prop="totalrate">
          <el-input v-model="form.totalrate" placeholder="请输入综合城市传播指数" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submitForm">确 定</el-button>
        <el-button @click="cancel">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { listCityattributes, getCityattributes, delCityattributes, addCityattributes, updateCityattributes } from "@/api/system/cityattributes";

export default {
  name: "Cityattributes",
  data() {
    return {
      // 遮罩层
      loading: true,
      // 选中数组
      ids: [],
      // 非单个禁用
      single: true,
      // 非多个禁用
      multiple: true,
      // 显示搜索条件
      showSearch: true,
      // 总条数
      total: 0,
      // 城市传播指数表格数据
      cityattributesList: [],
      // 弹出层标题
      title: "",
      // 是否显示弹出层
      open: false,
      // 查询参数
      queryParams: {
        pageNum: 1,
        pageSize: 10,
        cityID: null,
        cityName: null,
        searchin: null,
        network: null,
        mediatr: null,
        tourism: null,
        social: null,
        totalrate: null
      },
      // 表单参数
      form: {},
      // 表单校验
      rules: {
        cityID: [
          { required: true, message: "城市编号不能为空", trigger: "blur" }
        ],
        cityName: [
          { required: true, message: "城市名不能为空", trigger: "blur" }
        ],
      }
    };
  },
  created() {
    this.getList();
  },
  methods: {
    /** 查询城市传播指数列表 */
    getList() {
      this.loading = true;
      listCityattributes(this.queryParams).then(response => {
        this.cityattributesList = response.rows;
        this.total = response.total;
        this.loading = false;
      });
    },
    // 取消按钮
    cancel() {
      this.open = false;
      this.reset();
    },
    // 表单重置
    reset() {
      this.form = {
        cityID: null,
        cityName: null,
        searchin: null,
        network: null,
        mediatr: null,
        tourism: null,
        social: null,
        totalrate: null
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
      this.ids = selection.map(item => item.cityID)
      this.single = selection.length!==1
      this.multiple = !selection.length
    },
    /** 新增按钮操作 */
    handleAdd() {
      this.reset();
      this.open = true;
      this.title = "添加城市传播指数";
    },
    /** 修改按钮操作 */
    handleUpdate(row) {
      this.reset();
      const cityID = row.cityID || this.ids
      getCityattributes(cityID).then(response => {
        this.form = response.data;
        this.open = true;
        this.title = "修改城市传播指数";
      });
    },
    /** 提交按钮 */
    submitForm() {
      this.$refs["form"].validate(valid => {
        if (valid) {
          if (this.form.cityID != null) {
            updateCityattributes(this.form).then(response => {
              this.$modal.msgSuccess("修改成功");
              this.open = false;
              this.getList();
            });
          } else {
            addCityattributes(this.form).then(response => {
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
      const cityIDs = row.cityID || this.ids;
      this.$modal.confirm('是否确认删除城市传播指数编号为"' + cityIDs + '"的数据项？').then(function() {
        return delCityattributes(cityIDs);
      }).then(() => {
        this.getList();
        this.$modal.msgSuccess("删除成功");
      }).catch(() => {});
    },
    /** 导出按钮操作 */
    handleExport() {
      this.download('system/cityattributes/export', {
        ...this.queryParams
      }, `cityattributes_${new Date().getTime()}.xlsx`)
    }
  }
};
</script>
