<template>
  <!-- <h1>Class 2</h1> -->
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

        <div>张淳皓 96.40分</div>
        <br />
        <div>王承磊 95.60分</div>
        <br />
        <div>刘宇 90.60分</div>
        <br />
        <div>吴东泽 90.40分</div>
        <br />
        <div>李安民 90.00分</div>
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

        <div>曹逸飞 34.70分</div>
        <br />
        <div>李凯 30.80分</div>
        <br />
        <div>黄铮 29.20分</div>
        <br />
        <div>原永治 28.40分</div>
        <br />
        <div>梁宝军 26.50分</div>
        <br />
      </el-card>
    </el-col>
  </el-row>

  <h3>2. 纵向数据分析</h3>
  <div>
    纵向数据统计的为全班学生的学习情况，可以观察出整个课堂的宏观数据，比如签到统计，答题正确率，答题错误选项分布等。
  </div>

  <br />
  <!-- <div>第一次作业统计</div> -->
  <br />
  <el-row>
    <el-col :span="12">
      <Bar :option="line_data_1" />
      <!-- <hr /> -->
      <!-- <Bar :option="line_data_3" /> -->
      <!-- <hr /> -->
      <!-- <Bar :option="line_data_5" /> -->
      <!-- <hr /> -->
    </el-col>
    <el-col :span="12">
      <Bar :option="line_data_2" />
      <!-- <hr /> -->
      <!-- <Bar :optsion="line_data_4" /> -->
      <!-- <hr /> -->
      <!-- <Bar :option="line_data_6" /> -->
      <!-- <hr /> -->
    </el-col> </el-row
  ><br /><br />
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
              [1, 96.4],
              [2, 95.6],
              [3, 90.6],
              [4, 90.4],
              [5, 90.0],
              [6, 85.3],
              [7, 84.8],
              [8, 84.4],
              [9, 83.1],
              [10, 82.4],
              [11, 80.6],
              [12, 80.4],
              [13, 80.0],
              [14, 79.1],
              [15, 79.0],
              [16, 77.1],
              [17, 76.4],
              [18, 75.8],
              [19, 75.5],
              [20, 75.1],
              [21, 73.9],
              [22, 73.7],
              [23, 72.8],
              [24, 71.9],
              [25, 71.6],
              [26, 71.3],
              [27, 70.5],
              [28, 70.4],
              [29, 69.7],
              [30, 69.5],
              [31, 69.2],
              [32, 67.9],
              [33, 67.2],
              [34, 65.6],
              [35, 65.4],
              [36, 64.8],
              [37, 64.4],
              [38, 64.2],
              [39, 64.1],
              [40, 63.0],
              [41, 62.6],
              [42, 62.6],
              [43, 61.2],
              [44, 59.3],
              [45, 58.9],
              [46, 58.0],
              [47, 56.2],
              [48, 56.2],
              [49, 55.5],
              [50, 55.5],
              [51, 54.7],
              [52, 53.4],
              [53, 52.9],
              [54, 52.1],
              [55, 51.8],
              [56, 51.0],
              [57, 50.8],
              [58, 48.9],
              [59, 48.3],
              [60, 48.1],
              [61, 48.1],
              [62, 47.0],
              [63, 45.0],
              [64, 45.0],
              [65, 38.4],
              [66, 38.4],
              [67, 37.6],
              [68, 36.2],
              [69, 34.7],
              [70, 30.8],
              [71, 29.2],
              [72, 28.4],
              [73, 26.5],
            ],
            type: "scatter",
          },
        ],
      },

      line_data_1: {
        title: {
          text: "第一次计分作业 得分情况",
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
            data: ["40分", "38分","36分","35分","34分","30分","26分","0分"],
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
            data: [58, 5,1,1,2,4,1,4],
          },
        ],
      },

      line_data_2: {
        title: {
            text: '第二次计分作业 得分情况'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['成绩']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            feature: {
            saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false
            // data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
            name: '成绩',
            type: 'line',
            stack: 'Total',
            data: [
                50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
                50, 50, 50, 48, 48, 48, 48, 48, 46, 46, 46, 46, 46, 46, 44, 44, 44, 44,
                44, 44, 44, 44, 42, 42, 42, 42, 42, 42, 42, 40, 40, 40, 40, 40, 40, 40,
                40, 40, 39.6, 38, 38, 38, 38, 38, 38, 38, 38, 38, 37.6, 36, 36, 36, 36,
                36, 36, 36, 36, 36, 36, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34,
                33.6, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
                32, 32, 32, 32, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 28, 28,
                28, 28, 28, 28, 28, 28, 28, 28, 26, 26, 26, 26, 26, 26, 24, 24, 24, 24,
                24, 24, 24, 24, 23.6, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 20,
                20, 20, 20, 20, 20, 18.8, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18,
                18, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 15.6, 14, 14, 14, 14, 14,
                14, 14, 14, 14, 14, 14, 12, 12, 12, 12, 10, 10, 10, 10, 10, 10, 8, 7.2,
                6, 5.6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            ]
            }
        ]
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