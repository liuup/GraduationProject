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
                <el-button class="btn" @click="register()">注册</el-button>  
            </div>
        </div>

        <el-drawer v-model="drawer" >
            <el-form
                label-position="top"
                label-width="100px"
                :model="reg_form"
            >
                <el-form-item label="姓名">
                    <el-input v-model="reg_form.name" />
                </el-form-item>
                <el-form-item label="账号">
                    <el-input v-model="reg_form.num" />
                </el-form-item>
                <el-form-item label="密码">
                    <el-input v-model="reg_form.pwd" type="password" />
                </el-form-item>
                <el-form-item label="手机号">
                    <el-input v-model="reg_form.phone" />
                </el-form-item>
            </el-form>
            <el-button type="primary" @click="submit()">提交</el-button>
        </el-drawer>
    </div>
</template>



<script>
import { ElMessage } from 'element-plus'
import axios from "axios"
import md5 from "md5"
import Cookies from "js-cookie"

export default {
    data() {
        return {
            drawer: false,

            reg_form: {
                name: "",   // 姓名
                num: "",    // 账号
                pwd: "",    // 密码
                phone: "",   // 手机号
                date: "2022-04-15"  // 登录日期
            },

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
                ElMessage({
                    type: "warning",
                    message: "输入框禁止为空"
                })

                this.cancel();

                return;
            }

            this.user_form.pwd = md5(this.user_form.pwd);

            axios
                .post("http://127.0.0.1:8000/login", this.user_form)
                .then(res => {
                    let data = JSON.parse(res.data);
                    // console.log(data.status);

                    if(data.status == "failure") {
                        ElMessage({
                            type: "warning",
                            message: "账号或密码错误"
                        })

                        this.cancel();
                    } else if(data.status == "success") {
                        ElMessage({
                            type: "success",
                            message: "登录成功"
                        })

                         // 设置跳转本地存储
                        localStorage.setItem("menuid", JSON.stringify("1"));
                        // 设置本地存储token
                        Cookies.set("token", this.user_form.num);
                        // 跳转路由
                        this.$router.replace({path: "/home"});
                    }
                })
                .catch(err => {

                    console.log(err);
                })
        },

        register() {
            this.drawer = true;
        },

        submit() {
            // FIXME: 注册判空验证
            // TODO: 注册接口测试

            this.reg_form.pwd = md5(this.reg_form.pwd);

            axios
                .post("http://127.0.0.1:8000/register", this.reg_form)
                .then(res => {
                    console.log(res);
                    this.drawer = false;

                    let data = JSON.parse(res.data);

                    if(data.status == "failure") {
                        ElMessage({
                            message: '注册失败',
                            type: 'error',
                        })

                        this.cancel();
                    } else if(data.status == "success") {
                        ElMessage({
                            message: '注册成功',
                            type: 'success',
                        })

                         // 设置本地存储
                        // localStorage.setItem("menuid", JSON.stringify("1"));
                        // 跳转路由
                        // this.$router.replace({path: "/home"});
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
