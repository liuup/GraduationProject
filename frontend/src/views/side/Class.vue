<template>
  <div class="class-main">
    <h1>课程分析</h1>
    <el-table :data="tableData" stripe height="600px" style="width: 100%">
      <el-table-column prop="date" label="日期" width="180" />
      <el-table-column prop="name" label="课程名称" width="180" />
      <el-table-column prop="class" label="行政班级" width="220" />
      <el-table-column prop="count" label="学生人数" width="180" />
      <el-table-column prop="platform" label="学习平台" width="180" />
      
      <el-table-column label="Operations">
        <template #default="scope">
          <el-button type="primary" @click="handleShowClass(scope.$index)">查看</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        {
          date: "2018-05-03",
          name: "软件工程基础",
          class: "计科1801 计科1802 计科1803",
          count: "72",
          platform: "雨课堂"
        },
        {
          date: "1918-05-03",
          name: "测试",
          class: "Test",
          count: "0",
          platform: "超星"
        },
        {
          date: "1918-05-03",
          name: "测试",
          class: "Test",
          count: "0",
          platform: "超星"
        },
      ],
    };
  },

  methods: {
    handleShowClass(index) {
      console.log(index);
      localStorage.setItem("classindex", JSON.stringify(index));
      this.$router.push({ path: "/classinfo" });
    },
    
  }
};
</script>

<style scoped>
.class-main {
  height: 650px;
}
</style>