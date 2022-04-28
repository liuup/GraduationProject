<template>
    <div class="notfound-main">
        <img src="../assets/404.jpg"><br/>
        <el-button type="primary" @click="back()">返回首页</el-button>
    </div>
</template>

<script>
export default{
    data() {
        return {}
    },

    methods: {
        back() {
            // const element = document.getElementsByClassName("notfound-main");
            // console.log(element.clientHeight);
            this.$router.push({ path: "/" });
        }
    }
}
</script>

<style scoped>
.notfound-main {
    text-align: center;
    background-color: black;
    height: 100vh;
}
</style>
