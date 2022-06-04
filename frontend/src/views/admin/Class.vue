<template>
  <div class="class-main">
    <h1>课程管理</h1>
    <el-table :data="tableData" stripe style="width: 100%">
      <el-table-column prop="date" label="日期" width="180" />
      <el-table-column prop="name" label="课程名称" width="180" />
      <el-table-column prop="class" label="行政班级" width="220" />
      <el-table-column prop="count" label="学生人数" width="180" />
      <el-table-column prop="platform" label="学习平台" width="180" />

      <el-table-column label="操作">
        <template #default="scope">
          <el-button type="primary" @click="handleShowClass(scope.$index)"
            >查看</el-button
          >
        </template>
      </el-table-column>
    </el-table>


    <el-button type="primary" style="width: 100%" @click="addClass()">添加课程</el-button>

    <el-dialog v-model="dialogFormVisible" title="个人信息">
      <el-upload
      class="upload-demo"
    >
      <el-button type="primary" style="width: 100%" @click="addClass()">选择文件</el-button>
    </el-upload>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取消</el-button>
          <el-button type="primary" @click="submit()">确定</el-button>
        </span>
      </template>
    </el-dialog>

  </div>
</template>

<script>
export default {
  data() {
    return {
      dialogFormVisible: false,


      tableData: [
        {
          date: "2019-05-03",
          name: "软件工程基础",
          class: "计科1801 计科1802",
          count: "57",
          platform: "雨课堂",
        },
        {
          date: "2021-04-27",
          name: "软件工程基础",
          class: "软件1901 软件1902",
          count: "72",
          platform: "超星",
        },
        {
          date: "2020-05-03",
          name: "数据结构与算法",
          class: "计科1801 计科1802",
          count: "76",
          platform: "CG",
        },
        {
          date: "2021-05-03",
          name: "数据结构与算法",
          class: "计科2001 计科2002",
          count: "64",
          platform: "CG",
        },
        // {
        //   date: "2022-04-17",
        //   name: "软件工程基础",
        //   class: "计科2001 计科2002",
        //   count: "66",
        //   platform: "雨课堂",
        // },
      ],
    };
  },

  methods: {
    handleShowClass(index) {
      console.log(index);
      localStorage.setItem("classindex", JSON.stringify(index));
      this.$router.push({ path: "/admin/classinfo" });
    },

    addClass() {
      // this.tableData.push({
      //     date: "2022-04-17",
      //     name: "软件工程基础",
      //     class: "计科2001 计科2002",
      //     count: "66",
      //     platform: "雨课堂",
      //   });

      this.dialogFormVisible = true;
        //       {
        //   date: "2022-04-17",
        //   name: "软件工程基础",
        //   class: "计科2001 计科2002",
        //   count: "66",
        //   platform: "雨课堂",
        // },
    },

    submit() {
      this.dialogFormVisible = false;

      this.tableData.push({
          date: "2022-04-17",
          name: "软件工程基础",
          class: "计科2001 计科2002",
          count: "66",
          platform: "雨课堂",
        });
    },
  },
};
</script>

<style scoped>
.class-main {
  height: 650px;
}
</style>