<template>
    <div class="backimage">
        <div class="meituan-content">
            <div class="login-content">
                <div class="title">高校学情分析可视化平台</div>

                <div class="user">
                    <p>账号</p>
                    <el-input
                        class="inputflex"
                        v-model="user_form.num"
                        placeholder="测试账号123456"
                        clearable
                    ></el-input>
                </div>

                <div class="user">
                    <p>密码</p>
                    <el-input
                        class="inputflex"
                        v-model="user_form.pwd"
                        placeholder="测试密码654321"
                        type="password"
                        clearable
                    ></el-input>
                </div>

                <el-button class="btn" @click="login()" type="primary">登录</el-button>
                <el-button class="btn" @click="cancel()">清除</el-button>
            </div>
        </div>
    </div>
</template>



<script>
import { ElNotification } from 'element-plus'
import axios from "axios"


export default {
    data() {
        return {
            // isloading: false,   // 登录按键是否正在加载，true为加载，false为不在加载
            user_form: {
                num: "",	// 用户账号
                pwd: ""	// 用户密码
            },
        }
    },
    methods: {
        login() {
            // 错误处理
            if(this.user_form.num == "" || this.user_form.pwd == "") {
                ElNotification({
                message: '输入框禁止为空',
                type: 'warning',
                })

                this.cancel();

                return;
            }

            axios
                .post("http://127.0.0.1:8000/login", this.user_form)
                .then(res => {
                    let data = JSON.parse(res.data);
                    // console.log(data.status);

                    if(data.status == "failure") {
                        ElNotification({
                        message: '账号或密码错误',
                        type: 'error',
                        });
                        
                        this.cancel();
                    } else if(data.status == "success") {
                        ElNotification({
                        message: '登录成功',
                        type: 'success',
                        });

                         // 设置本地存储
                        localStorage.setItem("menuid", JSON.stringify("1"));
                        // 跳转路由
                        this.$router.push({path: "/home"});
                    }
                })
                .catch(err => {

                    console.log(err);
                })
        },

        // 清除登录表单
        cancel() {
            this.user_form.num = "";
            this.user_form.pwd = "";
        }
    }
}

</script>



<style scoped>
.backimage {
    background-image: url("../assets/material_you_desktop_8.png");
    /* background-color: #d1c2d3; */
    background-attachment: fixed;
    background-repeat: no-repeat;
    background-size: cover;
    min-height: 100vh;
}
.meituan-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 10px;
    box-shadow: 2px 2px 5px #813c85;
}
.login-content {
    width: 500px;
    height: 300px;
    background: #d1c2d3;
    border-radius: 10px;
}
.title {
    text-align: center;
    color: #000000;
    font-size: 30px;
    padding-top: 30px;
}
.user {
    width: 400px;
    margin: 0 auto;
    padding-top: 30px;
    height: 40px;
    display: flex;
    align-items: center;
}
.user p {
    width: 50px;
    color: #000000;
    font-size: 16px;
}
.inputflex {
    flex: 1;
}
.reg-view {
    width: 400px;
    display: flex;
    justify-content: flex-end;
    margin: 0 auto;
    padding-top: 10px;
}
.reg-view p {
    cursor: pointer;
    display: contents;
}
.btn {
    width: 200px;
    margin-top: 20px;
    /* margin: 10px auto 0 auto; */
    margin-left: 33px;
    align-items: center;
    /* display: flex; */
}
</style>
