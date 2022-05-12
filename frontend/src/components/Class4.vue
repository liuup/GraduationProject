<template>
  <!-- <h1>Class 4</h1> -->
  <h3>1. 横向数据分析</h3>
  <div>
    横向数据可以观察出单个学生的学习情况，按照加权的方式来计算单个学生的情况。
  </div>
  <br />
  <br />
  <el-row :gutter="10">
    <el-col :span="12">
      <Bar :option="scatter_data" />
    </el-col>
    <el-col :span="4">
      <el-card class="box-card" shadow="hover">
        <template #header>
          <div class="card-header">
            <span>成绩前五名</span>
          </div>
        </template>

        <div>潘璐 98.02分</div>
        <br />
        <div>岳维羿 97.66分</div>
        <br />
        <div>南杨 97.19分</div>
        <br />
        <div>解雨洋 97.19分</div>
        <br />
        <div>付俊 96.84分</div>
        <br />
      </el-card>
    </el-col>
    <el-col :span="4">
      <el-card class="danger-box-card" shadow="hover">
        <template #header>
          <div class="card-header">
            <span>成绩后五名</span>
          </div>
        </template>

        <div>卫颖 75.21分</div>
        <br />
        <div>杨洪荣 72.55分</div>
        <br />
        <div>苗YAN菘 72.41分</div>
        <br />
        <div>梁越 71.93分</div>
        <br />
        <div>陈庚 67.08分</div>
        <br />
      </el-card>
    </el-col>
  </el-row>

  <h3>2. 纵向数据分析</h3>
  <div>
    纵向数据统计的为全班学生的学习情况，可以观察出整个课堂的宏观数据，比如签到统计，答题正确率，答题错误选项分布等。
  </div>

  <br />
  <div>2.1 答题统计</div>
  <br />
  <el-row>
    <el-col :span="12">
      <Bar :option="line_data_1" />
    </el-col>
    <el-col :span="12">
      <Bar :option="line_data_2" />
    </el-col> </el-row
  ><br /><br />
  <el-row>
    <el-col :span="12">
      <Bar :option="line_data_3" />
    </el-col>
    <el-col :span="12">
      <Bar :option="line_data_4" />
    </el-col> </el-row
  ><br /><br />
  <el-row>
    <el-col :span="12">
      <Bar :option="line_data_5" />
    </el-col>
    <el-col :span="12">
      <!-- <Bar :option="line_data_4" /> -->
    </el-col>
  </el-row>
</template>

<script>
import Bar from "./Bar.vue";

export default {
  components: {
    // Echarts组件
    Bar,
  },

  data() {
    return {
      scatter_data: {
        title: {
          text: "学生分数统计表",
        },
        xAxis: {
          name: "编号",
        },
        yAxis: {
          name: "得分",
        },
        series: [
          {
            symbolSize: 20,
            data: [
              [1, 98.02],
              [2, 97.66],
              [3, 97.19],
              [4, 97.19],
              [5, 96.84],
              [6, 96.72],
              [7, 96.35],
              [8, 96.25],
              [9, 95.83],
              [10, 95.36],
              [11, 95.24],
              [12, 94.95],
              [13, 94.77],
              [14, 94.74],
              [15, 94.53],
              [16, 94.53],
              [17, 94.36],
              [18, 94.22],
              [19, 94.06],
              [20, 93.73],
              [21, 93.49],
              [22, 93.39],
              [23, 93.32],
              [24, 93.28],
              [25, 93.23],
              [26, 93.23],
              [27, 93.21],
              [28, 93.11],
              [29, 93.07],
              [30, 93.06],
              [31, 92.45],
              [32, 92.1],
              [33, 91.86],
              [34, 91.75],
              [35, 91.72],
              [36, 91.68],
              [37, 91.54],
              [38, 91.54],
              [39, 91.46],
              [40, 91.41],
              [41, 91.3],
              [42, 91.15],
              [43, 91.15],
              [44, 91.13],
              [45, 91.09],
              [46, 90.71],
              [47, 90.43],
              [48, 89.95],
              [49, 89.88],
              [50, 89.67],
              [51, 89.25],
              [52, 88.49],
              [53, 87.69],
              [54, 86.82],
              [55, 84.88],
              [56, 83.8],
              [57, 83.21],
              [58, 81.67],
              [59, 81.56],
              [60, 78.49],
              [61, 77.86],
              [62, 76.93],
              [63, 75.42],
              [64, 75.21],
              [65, 72.55],
              [66, 72.41],
              [67, 71.93],
              [68, 67.08],
            ],
            type: "scatter",
          },
        ],
      },

      line_data_1: {
        title: {
          text: "作业一答题情况",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: [
          {
            name: "得分",
            type: "category",
            data: ["10分", "9分", "8分", "7分", "6分", "5分"],
            axisTick: {
              alignWithLabel: true,
            },
          },
        ],
        yAxis: [
          {
            name: "学生个数",
            type: "value",
          },
        ],
        series: [
          {
            name: "学生个数",
            type: "bar",
            barWidth: "60%",
            data: [45, 7, 3, 4, 5, 4],
          },
        ],
      },

      line_data_2: {
        title: {
          text: "作业二答题情况",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: [
          {
            name: "得分",
            type: "category",
            data: ["10分", "9分", "8分", "7分", "6分"],
            axisTick: {
              alignWithLabel: true,
            },
          },
        ],
        yAxis: [
          {
            name: "学生个数",
            type: "value",
          },
        ],
        series: [
          {
            name: "学生个数",
            type: "bar",
            barWidth: "60%",
            data: [9, 32, 21, 5, 1],
          },
        ],
      },

      line_data_3: {
        title: {
          text: "作业三答题情况",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: [
          {
            name: "得分",
            type: "category",
            data: ["10分", "9分", "8分", "6分"],
            axisTick: {
              alignWithLabel: true,
            },
          },
        ],
        yAxis: [
          {
            name: "学生个数",
            type: "value",
          },
        ],
        series: [
          {
            name: "学生个数",
            type: "bar",
            barWidth: "60%",
            data: [57, 6, 4, 1],
          },
        ],
      },

      line_data_4: {
        title: {
          text: "作业四答题情况",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: [
          {
            name: "得分",
            type: "category",
            data: ["10分", "9分", "8分", "7分", "6分"],
            axisTick: {
              alignWithLabel: true,
            },
          },
        ],
        yAxis: [
          {
            name: "学生个数",
            type: "value",
          },
        ],
        series: [
          {
            name: "学生个数",
            type: "bar",
            barWidth: "60%",
            data: [16, 34, 7, 6, 5],
          },
        ],
      },

      line_data_5: {
        title: {
          text: "作业五答题情况",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: [
          {
            name: "得分",
            type: "category",
            data: ["30分","29分","28分","27分","26分","25分","24分","22分","15分","11分",],
            axisTick: {
              alignWithLabel: true,
            },
          },
        ],
        yAxis: [
          {
            name: "学生个数",
            type: "value",
          },
        ],
        series: [
          {
            name: "学生个数",
            type: "bar",
            barWidth: "60%",
            data: [16,12,8,17,7,4,1,1,1,1],
          },
        ],
      },
    };
  },
};
</script>

<style scoped>
.danger-box-card {
  background-color: #f3d19e;
}
</style>