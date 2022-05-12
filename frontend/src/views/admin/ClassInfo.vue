<template>
    <div class="classinfo-main">
        <!-- <h1>Class Info index:{{ classindex }}</h1> -->
        <Class1 v-if="classindex == 0"/>
        <Class2 v-if="classindex == 1"/>
        <Class3 v-if="classindex == 2"/>
        <Class4 v-if="classindex == 3"/>
        <Class5 v-if="classindex == 4"/>
    </div>
</template>

<script>
import Class1 from "../../components/Class1.vue"
import Class2 from "../../components/Class2.vue"
import Class3 from "../../components/Class3.vue"
import Class4 from "../../components/Class4.vue"
import Class5 from "../../components/Class5.vue"

export default {
    components: {
        // Echarts组件
        // Bar,
        // Round,
        Class1,
        Class2,
        Class3,
        Class4,
        Class5,
    },
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