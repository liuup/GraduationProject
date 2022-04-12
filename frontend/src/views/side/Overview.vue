<template>
  <div class="overview-main">
    <h1>学情总览</h1>
    <!-- <div style="width: 600px;height:400px;"> -->
    <!-- <Bar :option="bar_data"></Bar> -->
    <!-- </div> -->
    <el-row>
      <el-col :span="12">
        <Bar :option="bar_data"></Bar>
      </el-col>
      <el-col :span="12">
        <Round :option="round_data"></Round>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Bar from "../../components/Bar.vue";
import Round from "../../components/Round.vue";

export default {
  components: {
    // Echarts组件
    Bar,
    Round,
  },

  data() {
    return {
      bar_data: {
        title: {
          text: "Where data comes from",
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
            name: "Placeholder",
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
            data: [0, 1579, 532, 0],
          },
          {
            name: "Life Cost",
            type: "bar",
            stack: "Total",
            label: {
              show: true,
              position: "inside",
            },
            data: [8517, 6938, 1047, 532],
          },
        ],
      },

      round_data: {
        title: {
          text: "Where data comes from",
        //   subtext: "Fake Data",
          left: "center",
        },
        tooltip: {
          trigger: "item",
        },
        legend: {
          orient: "vertical",
          left: "left",
        },
        series: [
          {
            name: "Access From",
            type: "pie",
            radius: "50%",
            data: [
              { value: 6938, name: "CG" },
              { value: 1047, name: "雨课堂" },
              { value: 532, name: "超星" },
            //   { value: 484, name: "Union Ads" },
            //   { value: 300, name: "Video Ads" },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
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