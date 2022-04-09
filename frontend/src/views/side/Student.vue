<template>
  <div class="student-main">
    <h1>学生分析</h1>

    <el-row>
      <el-col :span="12">
        <Bar :bar_data="bar_data_1"></Bar>
      </el-col>
      <el-col :span="12">
        <Bar :bar_data="bar_data_1"></Bar>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Bar from "../../components/Bar.vue";

export default {
  name: "Studenet",

  components: {
    // Echarts组件
    Bar,
    // Round,
  },

  data() {
    return {
      bar_data_1: [5, 20, 36, 10, 10, 20],
    };
  },
};
</script>

<style scoped>
.student-main {
  height: 650px;
}
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
