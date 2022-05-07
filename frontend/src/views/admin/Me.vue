<template>
    <div class="myself-main">
        <h1>个人中心</h1>
          <el-table :data="info" style="width: 100%">
          <el-table-column prop="name" label="姓名" width="120" />
          <el-table-column prop="num" label="账号" />
          <el-table-column prop="last_logintime" label="上次登录时间" />
          <el-table-column prop="phone" label="手机号" />
          <el-table-column label="操作">
            <template #default="scope">
              <el-button type="primary" @click="handleShowClass(scope.$index)">修改</el-button>
            </template>
          </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
  
  data() {
    return {
      info: [
        {
          name: "UP",
          num: "123456",
          last_logintime: "2022-04-15",
          phone: "10086",
        }
      ]
    }
  }
}
</script>

<style scoped>
.myself-main {
  height: 650px;
}
</style>