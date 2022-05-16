<template>
  <h1>Class 3</h1>
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

        <div>刘力源 94分</div>
        <br />
        <div>刘一鸣 94分</div>
        <br />
        <div>王桥锋 79分</div>
        <br />
        <div>马红阳 77分</div>
        <br />
        <div>徐子钧 72分</div>
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

        <div>武俊男 22分</div>
        <br />
        <div>翟洛友 5分</div>
        <br />
        <div>陈海龙 0分</div>
        <br />
        <div>郑明洋 0分</div>
        <br />
        <div>韩佳桐 0分</div>
        <br />
      </el-card>
    </el-col>
  </el-row>

  <h3>2. 纵向数据分析</h3>
  <div>
    纵向数据统计的为全班学生的学习情况，可以观察出整个课堂的宏观数据，比如签到统计，答题正确率，答题错误选项分布等。
  </div>

  <br /><br/>
  <div>2.1 期末选择题统计</div>
  <br />

  <Bar :option="choice_data" style="width: 1000px" />
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
              [1, 94],
              [2, 94],
              [3, 79],
              [4, 77],
              [5, 72],
              [6, 71],
              [7, 71],
              [8, 70],
              [9, 70],
              [10, 69],
              [11, 68],
              [12, 68],
              [13, 68],
              [14, 66],
              [15, 62],
              [16, 62],
              [17, 59],
              [18, 59],
              [19, 59],
              [20, 57],
              [21, 55],
              [22, 53],
              [23, 53],
              [24, 53],
              [25, 53],
              [26, 53],
              [27, 53],
              [28, 52],
              [29, 52],
              [30, 52],
              [31, 51],
              [32, 51],
              [33, 50],
              [34, 49],
              [35, 49],
              [36, 48],
              [37, 48],
              [38, 48],
              [39, 47],
              [40, 43],
              [41, 43],
              [42, 42],
              [43, 42],
              [44, 42],
              [45, 42],
              [46, 41],
              [47, 41],
              [48, 40],
              [49, 39],
              [50, 38],
              [51, 37],
              [52, 36],
              [53, 36],
              [54, 35],
              [55, 34],
              [56, 33],
              [57, 32],
              [58, 32],
              [59, 28],
              [60, 22],
              [61, 5],
              [62, 0],
              [63, 0],
              [64, 0],
            ],
            type: "scatter",
          },
        ],
      },

      choice_data: {
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // Use axis to trigger tooltip
            type: "shadow", // 'shadow' as default; can also be 'line' or 'shadow'
          },
        },
        legend: {},
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: {
          type: "category",
          data: [
            "选择题1",
            "选择题2",
            "选择题3",
            "选择题4",
            "选择题5",
            "选择题6",
            "选择题7",
            "选择题8",
            "选择题9",
            "选择题10",
            "选择题11",
            "选择题12",
            "选择题13",
            "选择题14",
            "选择题15",
          ],
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            name: "2分",
            type: "bar",
            stack: "total",
            label: {
              show: true,
            },
            emphasis: {
              focus: "series",
            },
            data: [54, 26, 33, 49, 49, 33, 35, 40, 35, 53, 42, 54, 27, 50, 40],
          },
          {
            name: "0分",
            type: "bar",
            stack: "total",
            label: {
              show: true,
            },
            emphasis: {
              focus: "series",
            },
            data: [
              10,
              64 - 26,
              64 - 33,
              64 - 49,
              64 - 49,
              64 - 33,
              64 - 35,
              64 - 40,
              64 - 35,
              64 - 53,
              64 - 42,
              64 - 54,
              64 - 27,
              14,
              24,
            ],
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