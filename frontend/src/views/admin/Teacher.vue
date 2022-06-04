<template>
    <div class="teacher-main">
        <h1>教师管理</h1>
        <el-table :data="teacherData" stripe style="width: 100%">
          <el-table-column prop="id" label="ID" width="180" />
          <el-table-column prop="name" label="教师姓名" width="180" />
          <el-table-column prop="account" label="登录账号" width="180" />
          <el-table-column prop="last_logintime" label="最后登录时间" width="220" />
          <!-- <el-table-column prop="password" label="学生人数" width="180" /> -->
          <el-table-column prop="phone" label="手机号" width="180" />

          <el-table-column label="操作">
            <template #default="scope">
              <el-button type="primary" @click="handleEdit(scope.$index)">编辑</el-button>
            </template>
          </el-table-column>
        </el-table>
            <el-button type="primary" style="width: 100%" @click="dialogFormVisible = true">添加教师</el-button>
    </div>

    <el-dialog v-model="dialogFormVisible" title="个人信息">
      <el-form :model="input_teacher">
        <el-form-item label="ID">
          <el-input v-model="input_teacher.id" autocomplete="off" />
        </el-form-item>
        <el-form-item label="姓名">
          <el-input v-model="input_teacher.name" autocomplete="off" />
        </el-form-item>
        <el-form-item label="账号">
          <el-input v-model="input_teacher.account" autocomplete="off" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="input_teacher.password" autocomplete="off" />
        </el-form-item>
        <el-form-item label="手机">
          <el-input v-model="input_teacher.phone" autocomplete="off" />
        </el-form-item>
      </el-form>

      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取消</el-button>
          <el-button type="primary" @click="submit()">确定</el-button>
        </span>
      </template>
    </el-dialog>
</template>

<script>
import axios from 'axios'
// import { ElMessageBox, ElMessage } from "element-plus";
// import axios from "axios";

export default {
  data() {
    return {
      // 添加公告的对话框是否可见，默认为false不可见
      dialogFormVisible: false,

      input_teacher: {
        id: "",
        name: '',
        account: '',
        password: '',
        phone: '',
      },

      teacherData: [
        // {
        //   name: "TeacherName",
        //   classname: "",
        //   class: "",
        //   platform: "",
        // },
      ],
    }
  },

  mounted() {
    axios.get("http://127.0.0.1:8000/teacher/list").then((res) => {
      this.teacherData = JSON.parse(res.data);
    });
  },

  methods: {
    handleEdit(index) {
      console.log(index);
    },

    submit() {
      this.teacherData.push(this.input_teacher);
      this.dialogFormVisible = false;
    }
  }
}
</script>

<style scoped>
.teacher-main {
  height: 650px;
}
</style>