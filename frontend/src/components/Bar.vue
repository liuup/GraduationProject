<template>
    <div :id="elid" class="bar_container"></div>
</template>

<script>
import * as echarts from "echarts"
import {v4 as uuidv4} from "uuid";

export default {
    props: ["option"],

    data() {
        return {
            elid: "",
        }
    },

    created() {
        this.elid = uuidv4();
    },

    methods: {
        initChart() {
            let chart = echarts.init(document.getElementById(this.elid));
            
            chart.setOption(this.option);
        }
    },

    mounted() {
        this.initChart();
    },
}

</script>

<style scoped>
.bar_container {

    width: 500px;
    height: 500px;
}
</style>