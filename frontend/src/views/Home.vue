<template>
  <div class="common-layout">
    <el-container>
      <el-header class="header">
        <img src="../assets/saulogo_blue_800x800.png" style="width:20px;">
        <span> 高校学情分析可视化平台</span>
        <el-button type="danger" class="exit-button" @click="Exit()">退出</el-button>
      </el-header>

      <el-container>
        <el-aside class="aside">
          <el-row>
            <el-col>
              <el-menu :default-active="active_index" @select="SelectIndex">
                <el-menu-item index="1" @click="Overview()">
                  <div class="menu-item">
                    <el-icon><View /></el-icon>
                    <span>学情总览</span>
                  </div>
                </el-menu-item>

                <el-menu-item index="2" @click="Student()">
                  <div class="menu-item">
                    <el-icon><User /></el-icon>
                    <span>学生分析</span>
                  </div>
                </el-menu-item>

                <el-menu-item index="3" @click="Class()">
                  <div class="menu-item">
                    <el-icon><DataAnalysis /></el-icon>
                    <span>课程分析</span>
                  </div>
                </el-menu-item>

                <el-menu-item index="4" @click="About()">
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
import { View, DataAnalysis, User, More } from "@element-plus/icons-vue";
// <el-icon><view /></el-icon>
export default {
  name: "Home",

  components: {
    // element-plus icons 组件
    View,
    DataAnalysis,
    User,
    More,
  },

  data() {
    return {
      // 用户停留的页面，做缓存用
      active_index: "1",
    };
  },

  methods: {
    SelectIndex(index, path) {
      localStorage.setItem("menuid", JSON.stringify(index));
    },

    Overview() {
      this.$router.replace({ path: "/overview" });
    },

    Student() {
      this.$router.replace({ path: "/student" });
    },

    Class() {
      this.$router.replace({ path: "/class" });
    },

    About() {
      this.$router.replace({ path: "/about" });
    },

    Exit() {
      this.$router.replace({ path: "/" });
    }
  },

  mounted() {
    this.active_index = JSON.parse(localStorage.getItem("menuid"));
  },
};
</script>


<style scoped>
.header {
  height: 46px;
  font-size: 30px;
}

.exit-button {
  margin-top: 7px;
  margin-right: 1px;
  float: right;
}

.common-layout {
  background-size: cover;
  min-height: 100vh;
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