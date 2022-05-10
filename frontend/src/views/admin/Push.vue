<template>
  <div class="push-main">
    <h1>公告发布</h1>

    <el-row :gutter="20" type="flex" style="flex-wrap: wrap">
      <el-col :span="6" v-for="item in card_list" :key="item.id">
        <el-card class="box-card" shadow="hover">
          <template #header>
            <div class="card-header">
              <span>{{ item.title }}</span>
              <el-button-group class="ml-4">
                <el-button type="default" @click="CardEdit(item.id)"
                  >编辑</el-button
                >
                <el-button type="danger" @click="CardDelete(item.id)"
                  >删除</el-button
                >
              </el-button-group>
            </div>
          </template>

          <div class="card-text">
            {{ item.message }}
          </div>
          <div class="card-time">{{ item.msg_date }}</div>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card class="box-card" shadow="hover">
          <template #header>
            <div class="card-header">
              <span>添加公告</span>
            </div>
          </template>
          <div class="card-text">
            <el-button @click="CardAdd()">点击添加</el-button>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { ElMessageBox, ElMessage } from "element-plus";
import axios from "axios"


export default {
  data() {
    return {
      // 公告列表，从后端请求
      card_list: [],

    };
  },

  methods: {
    // 编辑卡片信息
    CardEdit(cardid) {
      console.log(cardid);
    },

    // 删除卡片
    CardDelete(cardid) {
      console.log("delete" + cardid);

      ElMessageBox.confirm(
        "这将会永远删除此公告，是否继续？",
        "Warning",
        {
          confirmButtonText: "确认删除",
          cancelButtonText: "取消",
          type: "warning",
        }
      )
        .then(() => {
          ElMessage({
            type: "success",
            message: "已删除公告",
          });
          // TODO: 添加删除接口
        })
        .catch(() => {
          ElMessage({
            type: "info",
            message: "取消",
          });
        });
    },

    // 增加卡片
    CardAdd() {
      
    },
  },

  mounted() {
    // 获取全部公告信息
    axios
        .get("http://127.0.0.1:8000/notices")
        .then(res => {
            this.card_list = JSON.parse(res.data);
            // console.log(this.card_list);
        })
        .catch(err => {
            console.log(err);
        });
  }
};
</script>

<style scoped>
.push-main {
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
</style>