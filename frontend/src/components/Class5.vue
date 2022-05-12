<template>
  <div class="class5-main">
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

          <div>王佳 570分</div>
          <br />
          <div>刘云龙 536分</div>
          <br />
          <div>刘一鸣 531分</div>
          <br />
          <div>何星宇 530分</div>
          <br />
          <div>刘力源 529分</div>
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

          <div>翟洛友 416分</div>
          <br />
          <div>施正涵 416分</div>
          <br />
          <div>张鑫宇 411分</div>
          <br />
          <div>綦翔 407分</div>
          <br />
          <div>刘天旭 338分</div>
          <br />
        </el-card>
      </el-col>
    </el-row>

    <h3>2. 纵向数据分析</h3>
    <div>
      纵向数据统计的为全班学生的学习情况，可以观察出整个课堂的宏观数据，比如签到统计，答题正确率，答题错误选项分布等。
    </div>

    <br><div>2.1 签到统计</div><br>

    <Bar :option="cross_data" style="width: 1000px"/>

    <br><div>2.2 答题统计</div><br>
    <el-row>
        <el-col :span="12">
            <Bar :option="line_data_1" />
        </el-col>
        <el-col :span="12">
            <Bar :option="line_data_2" />
        </el-col>
    </el-row><br><br>
    <el-row>
        <el-col :span="12">
            <Bar :option="line_data_3" />
        </el-col>
        <el-col :span="12">
            <Bar :option="line_data_4" />
        </el-col>
    </el-row>
    
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
                            [1, 570],
                            [2, 536],
                            [3, 531],
                            [4, 530],
                            [5, 529],
                            [6, 525],
                            [7, 525],
                            [8, 524],
                            [9, 523],
                            [10, 522],
                            [11, 516],
                            [12, 516],
                            [13, 516],
                            [14, 515],
                            [15, 508],
                            [16, 507],
                            [17, 507],
                            [18, 506],
                            [19, 506],
                            [20, 505],
                            [21, 503],
                            [22, 502],
                            [23, 502],
                            [24, 501],
                            [25, 501],
                            [26, 501],
                            [27, 496],
                            [28, 496],
                            [29, 495],
                            [30, 494],
                            [31, 494],
                            [32, 493],
                            [33, 491],
                            [34, 487],
                            [35, 486],
                            [36, 478],
                            [37, 478],
                            [38, 478],
                            [39, 473],
                            [40, 469],
                            [41, 469],
                            [42, 467],
                            [43, 466],
                            [44, 465],
                            [45, 461],
                            [46, 460],
                            [47, 460],
                            [48, 459],
                            [49, 459],
                            [50, 458],
                            [51, 458],
                            [52, 456],
                            [53, 455],
                            [54, 453],
                            [55, 449],
                            [56, 446],
                            [57, 438],
                            [58, 435],
                            [59, 435],
                            [60, 431],
                            [61, 425],
                            [62, 416],
                            [63, 416],
                            [64, 411],
                            [65, 407],
                            [66, 338]
                        ],
                        type: 'scatter'
                        }
                    ]
            },

            cross_data: {
                title: {
                    text: '签到统计'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#6a7985'
                    }
                    }
                },
                legend: {
                    data: ['准时上课', '迟到', '未上课']
                },
                toolbox: {
                    // feature: {
                    // saveAsImage: {}
                    // }
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: [
                    {
                    type: 'category',
                    boundaryGap: false,
                    data: ["3-15 8:20",
                            "3-17 10:20",
                            "3-22 8:20",
                            "3-29 8:20",
                            "3-31 10:20",
                            "4-05 8:20",
                            "4-07 10:20",
                            "4-12 8:20",
                            "4-14 10:20"]
                    }
                ],
                yAxis: [
                    {
                    type: 'value'
                    }
                ],
                series: [
                    {
                    name: '准时上课',
                    type: 'line',
                    stack: 'Total',
                    areaStyle: {},
                    emphasis: {
                        focus: 'series'
                    },
                    data: [57,53,57,58,60,52,60, 52, 61]
                    },
                    {
                    name: '迟到',
                    type: 'line',
                    stack: 'Total',
                    areaStyle: {},
                    emphasis: {
                        focus: 'series'
                    },
                    data: [8,13 ,9 ,8 ,6 ,14 ,6 ,13 ,5]
                    },
                    {
                    name: '未上课',
                    type: 'line',
                    stack: 'Total',
                    areaStyle: {},
                    emphasis: {
                        focus: 'series'
                    },
                    data: [1, 0,0,0,0,0,0,1,0]
                    },

                    
                ]
            },

            line_data_1: {
                title: {
                    text: '3-22 答题统计'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                grid: {
                    top: 80,
                    bottom: 30
                },
                xAxis: {
                    type: 'value',
                    position: 'bottom',
                    splitLine: {
                    lineStyle: {
                        type: 'dashed'
                    }
                    }
                },//A 0, B 4, C 48, D 3, NULL 11
                yAxis: {
                    type: 'category',
                    axisLine: { show: false },
                    axisLabel: { show: false },
                    axisTick: { show: false },
                    splitLine: { show: false },
                    data: [
                    '未选',
                    'D',
                    'C',
                    'B',
                    'A',
                    ]
                },
                series: [
                    {
                    name: 'Cost',
                    type: 'bar',
                    stack: 'Total',
                    label: {
                        show: true,
                        formatter: '{b}'
                    },
                    data: [11, 3, 48, 4, 0]
                    }
                ]
            },

            line_data_2: {
                title: {
                    text: '3-31 答题统计'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                grid: {
                    top: 80,
                    bottom: 30
                },
                xAxis: {
                    type: 'value',
                    position: 'bottom',
                    splitLine: {
                    lineStyle: {
                        type: 'dashed'
                    }
                    }
                },//A 0, B 4, C 48, D 3, NULL 11
                yAxis: {
                    type: 'category',
                    axisLine: { show: false },
                    axisLabel: { show: false },
                    axisTick: { show: false },
                    splitLine: { show: false },
                    data: [
                    '未选',
                    'D',
                    'C',
                    'B',
                    'A',
                    ]
                },
                series: [
                    {
                    name: 'Cost',
                    type: 'bar',
                    stack: 'Total',
                    label: {
                        show: true,
                        formatter: '{b}'
                    },
                    data: [3, 31, 52, 24, 31]
                    }
                ]
            },

            line_data_3: {
                title: {
                    text: '4-05 答题统计'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                grid: {
                    top: 80,
                    bottom: 30
                },
                xAxis: {
                    type: 'value',
                    position: 'bottom',
                    splitLine: {
                    lineStyle: {
                        type: 'dashed'
                    }
                    }
                },//A 0, B 4, C 48, D 3, NULL 11
                yAxis: {
                    type: 'category',
                    axisLine: { show: false },
                    axisLabel: { show: false },
                    axisTick: { show: false },
                    splitLine: { show: false },
                    data: [
                    '未选',
                    'E',
                    'D',
                    'C',
                    'B',
                    'A',
                    ]
                },
                series: [
                    {
                    name: 'Cost',
                    type: 'bar',
                    stack: 'Total',
                    label: {
                        show: true,
                        formatter: '{b}'
                    },
                    data: [5, 30, 46, 57, 58, 59]
                    }
                ]
            },

            line_data_4: {
                title: {
                    text: '4-14 答题统计'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                grid: {
                    top: 80,
                    bottom: 30
                },
                xAxis: {
                    type: 'value',
                    position: 'bottom',
                    splitLine: {
                    lineStyle: {
                        type: 'dashed'
                    }
                    }
                },//A 0, B 4, C 48, D 3, NULL 11
                yAxis: {
                    type: 'category',
                    axisLine: { show: false },
                    axisLabel: { show: false },
                    axisTick: { show: false },
                    splitLine: { show: false },
                    data: [
                    '未选',
                    'D',
                    'C',
                    'B',
                    'A',
                    ]
                },
                series: [
                    {
                    name: 'Cost',
                    type: 'bar',
                    stack: 'Total',
                    label: {
                        show: true,
                        formatter: '{b}'
                    },
                    data: [10, 4, 5, 5, 42]
                    }
                ]
            }

        }
    }


}
</script>

<style scoped>
.danger-box-card {
  background-color: #f3d19e;
}
</style>