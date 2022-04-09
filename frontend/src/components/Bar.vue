<template>
    <div :id="elid" class="bar_container"></div>
    <!-- <slot></slot> -->

</template>

<script>
import * as echarts from "echarts"
import {v4 as uuidv4} from "uuid";

export default {
    props: ["bar_data"],

    data() {
        return {
            elid: "",

            option: {
                title: {
                    text: "ECharts示例"
                },
                tooltip: {},
                legend: {
                    data: ["销量"]
                },
                xAxis: {
                    data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
                },
                yAxis: {},
                series: [{
                    name: "销量",
                    type: "bar",
                    // data: [5, 20, 36, 10, 10, 20],
                    data: this.bar_data,
                    showBackground: true,
                    backgroundStyle: {
                        color: "rgba(180, 180, 180, 0.2)"
                    }
                }]
            }
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
    /* background-color: aqua; */
    /* border: 1px solid blue; */
    width: 300px;
    height: 300px;
}
</style>