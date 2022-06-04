<template>
  <div class="me-main">
    <h1>个人中心</h1>
    <el-table :data="info_form" style="width: 100%">
      <el-table-column prop="account" label="账号" />
      <el-table-column prop="name" label="姓名" />
      <el-table-column prop="last_logintime" label="上次登录时间" />
      <el-table-column prop="phone" label="手机号" />
      <el-table-column label="操作">
        <template #default>
          <el-button type="primary" @click="dialogFormVisible = true"
            >修改</el-button
          >
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="dialogFormVisible" title="个人信息">
      <el-form :model="info_form[0]">
        <el-form-item label="登录账号">
          <el-input
            v-model="info_form[0].account"
            autocomplete="off"
            clearable
          />
        </el-form-item>
        <el-form-item label="姓名">
          <el-input v-model="info_form[0].name" autocomplete="off" clearable />
        </el-form-item>
        <el-form-item label="密码">
          <el-input
            v-model="info_form[0].password"
            autocomplete="off"
            clearable
          />
        </el-form-item>
        <el-form-item label="手机号">
          <el-input v-model="info_form[0].phone" autocomplete="off" clearable />
        </el-form-item>
      </el-form>
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

      info_form: [
        {
          account: "teacher",
          name: "TeacherName",
          last_logintime: "2022-05-17",
          phone: "10086",
          password: "c33367701511b4f6020ec61ded352059"
        },
      ],
    };
  },
};
</script>

<style scoped>
.me-main {
  height: 650px;
}
</style>
