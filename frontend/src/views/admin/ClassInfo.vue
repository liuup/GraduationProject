<template>
    <div class="classinfo-main">
        <h1>Class Info index:{{ classindex }}</h1>

    </div>
</template>

<script>
export default {
    data() {
        return {
            classindex: "",
        }
    },
    mounted() {
        this.classindex = localStorage.getItem("classindex");
    }

}
</script>

<style scoped>
.classinfo-main {
    height: 650px;
}
</style>