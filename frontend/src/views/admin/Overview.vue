<template>
  <div class="overview-main">
    <h1>平台总览</h1>
    <!-- <div style="width: 600px;height:400px;"> -->
    <!-- <Bar :option="bar_data"></Bar> -->
    <!-- </div> -->
    <el-row>
      <el-col :span="12">
        <Bar :option="bar_data"></Bar>
      </el-col>
      <el-col :span="12">
        <Bar :option="bar_data_2"></Bar>
      </el-col>
    </el-row>
    <!-- <el-row>
      <el-col :span="12">
        <Bar :option="bar_data"></Bar>
      </el-col>
      <el-col :span="12">
        <Round :option="round_data"></Round>
      </el-col>
    </el-row> -->
  </div>
</template>

<script>
import Bar from "../../components/Bar.vue";
// import Round from "../../components/Round.vue";

export default {
  components: {
    // Echarts组件
    Bar,
    // Round,
  },

  data() {
    return {
      bar_data: {
        title: {
          text: "平台数据来源",
          //   subtext: "Living Expenses in Shenzhen",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
          formatter: function (params) {
            var tar = params[1];
            return tar.name + "<br/>" + tar.seriesName + " : " + tar.value;
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: {
          type: "category",
          splitLine: { show: false },
          data: ["总数据量", "CG", "雨课堂", "超星"],
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            // name: "Placeholder",
            type: "bar",
            stack: "Total",
            itemStyle: {
              borderColor: "transparent",
              color: "transparent",
            },
            emphasis: {
              itemStyle: {
                borderColor: "transparent",
                color: "transparent",
              },
            },
            data: [0, 1579 + 585, 532, 0],
          },
          {
            name: "数据",
            type: "bar",
            stack: "Total",
            label: {
              show: true,
              position: "inside",
            },
            data: [8517 + 585, 6938, 1047 + 585, 532],
          },
        ],
      },

      bar_data_2: {
        xAxis: {
          name: "数据",
          type: "category",
          data: ["老师", "学生", "管理员", "课程"],
        },
        yAxis: {
          name: "数量",
          type: "value",
        },
        series: [
          {
            data: [1, 1, 1, 5],
            type: "bar",
            showBackground: true,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.2)",
            },
          },
        ],
      },
    };
  },
};
</script>

<style scoped>
.overview-main {
  height: 650px;
}
/*
学生
CG
2020-2021-1 4058
2021-2022-1 2880

超星 532
雨课堂 1047


*/
</style>