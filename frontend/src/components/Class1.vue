<template>
    <h1>Class 1</h1>
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


          <div>徐松旭 347分</div>
          <br />
          <div>佟凯 340分</div>
          <br />
          <div>方蕊 339分</div>
          <br />
          <div>侯子童 336分</div>
          <br />
          <div>李梦圆 333分</div>
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

          <div>王昕煜 139分</div>
          <br />
          <div>高尊 123分</div>
          <br />
          <div>李沛霖 55分</div>
          <br />
          <div>崔泽山 37分</div>
          <br />
          <div>刘士君 28分</div>
          <br />
        </el-card>
      </el-col>
    </el-row>

    <h3>2. 纵向数据分析</h3>
    <div>
      纵向数据统计的为全班学生的学习情况，可以观察出整个课堂的宏观数据，比如签到统计，答题正确率，答题错误选项分布等。
    </div>






    
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
                    text: '学生分数统计表',
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
                        [1, 347],
                        [2, 340],
                        [3, 339],
                        [4, 336],
                        [5, 333],
                        [6, 332],
                        [7, 332],
                        [8, 331],
                        [9, 330],
                        [10, 328],
                        [11, 328],
                        [12, 325],
                        [13, 325],
                        [14, 325],
                        [15, 324],
                        [16, 323],
                        [17, 323],
                        [18, 322],
                        [19, 321],
                        [20, 320],
                        [21, 320],
                        [22, 314],
                        [23, 313],
                        [24, 309],
                        [25, 307],
                        [26, 307],
                        [27, 307],
                        [28, 306],
                        [29, 305],
                        [30, 304],
                        [31, 303],
                        [32, 302],
                        [33, 302],
                        [34, 301],
                        [35, 297],
                        [36, 295],
                        [37, 294],
                        [38, 291],
                        [39, 282],
                        [40, 281],
                        [41, 280],
                        [42, 279],
                        [43, 275],
                        [44, 273],
                        [45, 269],
                        [46, 267],
                        [47, 260],
                        [48, 242],
                        [49, 210],
                        [50, 190],
                        [51, 166],
                        [52, 141],
                        [53, 139],
                        [54, 123],
                        [55, 55],
                        [56, 37],
                        [57, 28]
                    ],
                    type: 'scatter'
                    }
                ]
            },
        }
    }
}
</script>

<style scoped>
.danger-box-card {
  background-color: #f3d19e;
}
</style>