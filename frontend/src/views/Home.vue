<template>
  <div class="common-layout">
    <el-container>
      <el-header class="header">
        <img src="../assets/saulogo_blue_800x800.png" style="width:20px;">
        <span> 高校学情分析可视化平台</span>
      </el-header>

      <el-container>
        <el-aside class="aside">
          <el-row>
            <el-col>
              <el-menu :default-active="active_index" @select="SelectIndex">
                <el-menu-item index="1" @click="Student()">
                  <div class="menu-item">
                    <el-icon><User /></el-icon>
                    <span>学生分析</span>
                  </div>
                </el-menu-item>

                <el-menu-item index="2" @click="Class()">
                  <div class="menu-item">
                    <el-icon><DataAnalysis /></el-icon>
                    <span>课堂分析</span>
                  </div>
                </el-menu-item>

                <el-menu-item index="3" @click="About()">
                  <div class="menu-item">
                    <el-icon><More /></el-icon>
                    <span>关于</span>
                  </div>
                </el-menu-item>
              </el-menu>
            </el-col>
          </el-row>
        </el-aside>
        <el-container>
          <el-main class="main">
            <router-view></router-view>
          </el-main>

          <el-footer class="footer">
            <div>SAU 计科1803-183424080320刘上 Copyright 1.0 beta</div>
          </el-footer>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>


<script>
import { DataAnalysis, User, More } from "@element-plus/icons-vue";

export default {
  name: "Home",

  components: {
    // Echarts组件
    // Bar,
    // Round,

    // element-plus icons 组件
    DataAnalysis,
    User,
    More,
  },

  data() {
    return {
      active_index: "1",

      bar_data_1: [5, 20, 36, 10, 10, 20],
      bar_data_2: [10, 35, 10, 5, 40, 25],

      round_data: [
        { value: 1048, name: "Search Engine" },
        { value: 735, name: "Direct" },
        { value: 580, name: "Email" },
        { value: 484, name: "Union Ads" },
        { value: 300, name: "Video Ads" },
      ],
    };
  },

  methods: {
    SelectIndex(index, path) {
      localStorage.setItem("menuid", JSON.stringify(index));
    },

    Student() {
      this.$router.push({ path: "/student" });
    },

    Class() {
      this.$router.push({ path: "/class" });
    },

    About() {
      this.$router.push({ path: "/about" });
    },
  },

  mounted() {
    this.active_index = JSON.parse(localStorage.getItem("menuid"));
  },
};
</script>


<style scoped>
.common-layout {
  background-size: cover;
  min-height: 100vh;
}

.header {
  /* background-color: bisque; */
  font-size: 30px;
}

.aside {
  width: 200px;
  /* background-color: teal; */
  background-color: white;
}

.main {
  background-color: #fafafa;
}

.footer {
  background-color: white;
  height: 40px;
}

.menu-item {
  margin-left: 10px;
  /* align-items: center; */
}

.sub-menu {
  width: 110px;
  padding-left: 0;
}
</style>