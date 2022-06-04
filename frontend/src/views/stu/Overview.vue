<template>
  <div class="overview-main">
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
    <el-row :gutter="10">
      <el-col :span="12">
        <Bar :option="line_data" />
      </el-col>
      <el-col :span="4">
        <el-card class="safe-box-card" shadow="hover">
          <template #header>
            <div class="card-header">
              <span>当前课程预警</span>
            </div>
          </template>

          <div>暂无</div>
          <br />
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from "axios";
import Bar from "../../components/Bar.vue";

export default {
  components: {
    // Echarts组件
    // Class1,
    Bar,
  },

  data() {
    return {
      // 公告列表，从后端请求
      card_list: [],

      line_data: {
        title: {
          text: "签到统计",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
            label: {
              backgroundColor: "#6a7985",
            },
          },
        },
        toolbox: {
          // feature: {
          //   saveAsImage: {},
          // },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: [
          {
            type: "category",
            boundaryGap: false,
            data: [
              "3-15 8:20",
              "3-17 8:20",
              "3-22 10:20",
              "3-25 8:20",

              "3-30 8:20",
              "4-02 8:20",
              "4-06 10:20",
              "4-10 8:20",
              "4-15 8:20",
            ],
          },
        ],
        yAxis: [
          {
            type: "value",
          },
        ],
        series: [
          {
            name: "迟到时间",
            type: "line",
            stack: "Total",
            areaStyle: {},
            emphasis: {
              focus: "series",
            },
            data: [-13, 7, 9, 2, -5, 9, 13, 6, -3],
          },
        ],
      },
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