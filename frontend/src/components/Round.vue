<template>
    <div id="test"></div>
</template>

<script>
import * as echarts from "echarts"

export default {
    props: ["round_data"],

    data() {
        return {
            option: {
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    top: '5%',
                    left: 'center'
                },
                series: [
                    {
                        name: 'Access From',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: '#fff',
                            borderWidth: 2
                        },
                        label: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: '40',
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: this.round_data
                    }
                ]
            }
        }
    },
    methods: {
        initChart() {
            let chart = echarts.init(document.getElementById("test"));

            chart.setOption(this.option);
        }
    },
    mounted() {
        this.initChart();
    },

}

</script>

<style scoped>
#test {
    /* background-color: aqua; */
    border: 1px solid blue;
    width: 300px;
    height: 300px;
}
</style>