<template>
  <div class="myself-main">
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
import { ElMessage } from 'element-plus';
import axios from "axios";
import md5 from "md5";
import Cookies from "js-cookie";

export default {
  data() {
    return {
      // 添加公告的对话框是否可见，默认为false不可见
      dialogFormVisible: false,

      // 个人信息
      info_form: [],

      // 查询账号
      query_form: {
        account: "",
      },

      // 修改后的提交表单
      edited_form: {
        account: "",
        id: "",
        last_logintime: "",
        name: "",
        password: "",
        phone: "",
      },
    };
  },

  methods: {
    // 修改提交按键
    submit() {
      // 生成提交表单
      this.edited_form.account = this.info_form[0].account;
      this.edited_form.id = this.info_form[0].id;
      this.edited_form.last_logintime = this.info_form[0].last_logintime;
      this.edited_form.name = this.info_form[0].name;
      this.edited_form.password = md5(this.info_form[0].password);
      this.edited_form.phone = this.info_form[0].phone;


      axios
        .post("http://127.0.0.1:8000/admin/me/edit", this.edited_form)
        .then((res) => {
          let data = JSON.parse(res.data);
          // console.log(data.status);

          if (data.status == "failure") {
            ElMessage({
              type: "warning",
              message: "修改失败",
            });
          } else if (data.status == "success") {
            ElMessage({
              type: "success",
              message: "修改成功",
            });
            this.dialogFormVisible = false;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },

  mounted() {
    console.log(Cookies.get("token"));

    // 获取登录的用户
    this.query_form.account = Cookies.get("token");

    axios
      .post("http://127.0.0.1:8000/admin/me", this.query_form)
      .then((res) => {
        this.info_form.push(JSON.parse(res.data));

        // console.log(this.info_form);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
.myself-main {
  height: 650px;
}
</style>