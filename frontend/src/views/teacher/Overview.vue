<template>
  <!-- 课程总览 -->
  <div class="overview-main">
    <!-- <h1>课程总览</h1> -->
    <h1>公告栏</h1>
    <el-row :gutter="20" type="flex" style="flex-wrap: wrap">
      <el-col :span="6" v-for="item in card_list" :key="item.id">
        <el-card class="box-card" shadow="hover">
          <template #header>
            <div class="card-header">
              <span>{{ item.title }}</span>
            </div>
          </template>

          <div class="card-text">
            {{ item.message }}
          </div>
          <br />
          <div class="card-time">{{ item.msg_date }}</div>
        </el-card>
      </el-col> </el-row
    ><br />
    <hr />
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      // 公告列表，从后端请求
      card_list: [],
    };
  },

  mounted() {
    // 获取全部公告信息
    axios
      .get("http://127.0.0.1:8000/notices")
      .then((res) => {
        this.card_list = JSON.parse(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
.overview-main {
  height: 650px;
}

.box-card {
  margin-top: 20px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-text {
  word-wrap: break-word;
  word-break: break-all;
  overflow: hidden; /*这个参数根据需要来绝对要不要*/
}

.card-time {
  font-size: 12px;
}
</style>
