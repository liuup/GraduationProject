<template>
  <div class="student-main">
    <h1>学生管理</h1>

    <el-table :data="students" style="width: 100%">
      <el-table-column prop="name" label="姓名" width="120" />
      <el-table-column prop="num" label="学号" />
      <el-table-column prop="course" label="选课" />
      <!-- <el-table-column prop="phone" label="手机号" /> -->
      <el-table-column label="操作">
        <template #default="scope">
          <el-button type="primary" @click="handleShowClass(scope.$index)">查看</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import Bar from "../../components/Bar.vue";
import Round from "../../components/Round.vue";

export default {
  name: "Studenet",

  components: {
    // Echarts组件
    Bar,
    Round,
  },

  data() {
    return {
      students: [
        {
          name: "刘上",
          num: "183424080320",
          // class: "计科1803",
          course: "软件工程基础",
        },
        {
          name: "徐东",
          num: "153401010116",
          // class: "计科1803",
          course: "软件工程基础",
        },
        {
          name: "小明",
          num: "193411010227",
          // class: "计科1803",
          course: "软件工程基础",
        },
        {
          name: "石大千",
          num: "193401010233",
          // class: "计科1803",
          course: "软件工程基础",
        },
        {
          name: "刘上",
          num: "183424080320",
          // class: "计科1803",
          course: "软件工程基础",
        },
      ],


      bar_data: {
        title: {
          text: "ECharts示例",
        },
        tooltip: {},
        legend: {
          data: ["销量"],
        },
        xAxis: {
          data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        },
        yAxis: {},
        series: [
          {
            name: "销量",
            type: "bar",
            data: [5, 20, 36, 10, 10, 20],
            // data: this.bar_data,
            showBackground: true,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.2)",
            },
          },
        ],
      },

      round_data: {
        title: {
          text: "Referer of a Website",
          subtext: "Fake Data",
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
              { value: 1048, name: "Search Engine" },
              { value: 735, name: "Direct" },
              { value: 580, name: "Email" },
              { value: 484, name: "Union Ads" },
              { value: 300, name: "Video Ads" },
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
.student-main {
  height: 650px;
}
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}
/* .bg-purple-dark {
	background: #99a9bf;
}
.bg-purple {
	background: #d3dce6;
}
.bg-purple-light {
	background: #e5e9f2;
} */
/* .grid-content {
	border-radius: 4px;
	min-height: 36px;
}
.row-bg {
	padding: 10px 0;
	background-color: #f9fafc;
} */
</style>
