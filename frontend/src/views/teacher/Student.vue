<template>
    <!-- 学生管理 -->
    <div class="student-main">
      <h1>学生管理</h1>
      
      <el-table :data="students" style="width: 100%">
        <el-table-column prop="name" label="姓名" width="120" />
        <el-table-column prop="num" label="学号" />
        <el-table-column prop="course" label="选课" />
        <!-- <el-table-column prop="phone" label="手机号" /> -->
        <el-table-column label="操作">
          <template #default="scope">
            <el-button type="primary" @click="handleShow(scope.$index)"
              >查看</el-button
            >
            <el-button type="warning" @click="handleDelete(scope.$index)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
      <el-button type="primary" style="width: 100%" @click="dialogFormVisible = true"
        >添加学生</el-button
      >
      <el-dialog v-model="dialogFormVisible" title="个人信息">
        <el-form :model="input_stu">
          <el-form-item label="姓名">
            <el-input v-model="input_stu.name" autocomplete="off" />
          </el-form-item>
          <el-form-item label="学号">
            <el-input v-model="input_stu.num" autocomplete="off" />
          </el-form-item>
          <el-form-item label="班级">
            <el-input v-model="input_stu.course" autocomplete="off" />
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
export default{
  data() {
    return {
      // 添加公告的对话框是否可见，默认为false不可见
      dialogFormVisible: false,

      input_stu: {
        name: "",
        num: "",
        course: "",
      },

      students: [
        {
          name: "刘上",
          num: "183424080320",
          // class: "计科1803",
          course: "软件工程基础",
        },
        {
          name: "徐东",
          num: "153401010116",
          // class: "计科1803",
          course: "软件工程基础",
        },
        {
          name: "小明",
          num: "193411010227",
          // class: "计科1803",
          course: "软件工程基础",
        },
        {
          name: "石大千",
          num: "193401010233",
          // class: "计科1803",
          course: "软件工程基础",
        },
        {
          name: "刘上",
          num: "183424080320",
          // class: "计科1803",
          course: "软件工程基础",
        },
      ],
    }
  },


  methods: {
    submit() {
      this.students.push(this.input_stu);
      this.dialogFormVisible = false;
    },

    handleDelete(index) {
      // console.log(index);
      this.students.splice(index, 1);

    }
  }

}
</script>

<style scoped>
.student-main {
  height: 650px;
}
</style>
