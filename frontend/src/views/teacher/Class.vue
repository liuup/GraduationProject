<template>
    <!-- 课程管理 -->
    <div class="class-main">
        <h1>课程管理</h1>
        <Class1></Class1>
    </div>
</template>

<script>
import Class1 from "../../components/Class1.vue"
import Bar from "../../components/Bar.vue"

export default {
  components: {
    // Echarts组件
    Class1,
    Bar,
  },
}
</script>

<style scoped>
.class-main {
  height: 650px;
}
</style>
