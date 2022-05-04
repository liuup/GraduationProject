<template>
    <div class="backimage">
        <div class="meituan-content">
            <div class="title">高校学情分析可视化平台</div>

            <div class="login-content">
                <el-row>
                    <el-col :span="6" class="left-col">
                        <div class="left-buttons">
                            <el-button class="left-button" :type="stu_btn_type" @click="StudentBtn()">学生</el-button><br/>
                            <el-button class="left-button" :type="teach_btn_type" @click="TeachBtn()">教师</el-button><br/>
                            <el-button class="left-button" :type="admin_btn_type" @click="AdminBtn()">管理员</el-button><br/>
                        </div>
                    </el-col>
                    <el-col :span="12">
                        <span class="login-text">{{ login_text }}</span>

                        <div>
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
                            <!-- <el-button class="btn" @click="cancel()">清空</el-button> -->
                        </div>
                        
                    </el-col>
                </el-row>
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

            login_text: "学生",

            // 三个按钮的显示类型
            stu_btn_type: "primary",
            teach_btn_type: "default",
            admin_btn_type: "default",

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
        // 学生登录切换按键
        StudentBtn() {
            this.stu_btn_type = "primary";
            this.teach_btn_type = "default";
            this.admin_btn_type = "default";

            // TODO:
        },

        // 老师登录切换按键
        TeachBtn() {
            this.stu_btn_type = "default";
            this.teach_btn_type = "primary";
            this.admin_btn_type = "default";

            // TODO:
        },

        // 管理员登录切换按键
        AdminBtn() {
            this.stu_btn_type = "default";
            this.teach_btn_type = "default";
            this.admin_btn_type = "primary";

            // TODO:
        },

        // 登录按钮
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

        // 注册按钮
        register() {
            this.drawer = true;
        },

        // 注册提交按钮
        submit() {
            // FIXME: 注册判空验证

            // TODO: 注册接口测试
            // TODO: 注册日期功能添加

            /*
            reg_form: {
                name: "",   // 姓名
                num: "",    // 账号
                pwd: "",    // 密码
                phone: "",   // 手机号
                date: "2022-04-15"  // 登录日期
            },
            */

            if(this.reg_form.name == "" || this.reg_form.num == "" || 
                this.reg_form.pwd == "" || this.reg_form.phone == "") {
                ElMessage({
                    message: '输入框禁止为空',
                    type: 'warning',
                });
                
                this.cancel();
                return;
            }

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
                        this.cancel();
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

            this.reg_form.name = "";
            this.reg_form.num = "";
            this.reg_form.pwd = "";
            this.reg_form.phone = "";
            // TODO: 注册日期
            // this.reg_form.date = "";
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
    /* box-shadow: 2px 2px 5px #813c85; */
}
.login-content {
    width: 650px;
    height: 400px;
    background: #d1c2d3;
    border-radius: 10px;
    box-shadow: 2px 2px 5px #813c85;
}
.title {
    text-align: center;
    color:  #337ecc;
    font-size: 45px;
    padding-top: 30px;
    padding-bottom: 30px;
}
.user {
    width: 400px;
    /* margin: 0 auto; */
    padding-top: 30px;
    height: 40px;
    display: flex;
    align-items: center;

    margin-top: 20px;
    margin-left: 20px;
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

.login-text {
    font-size: 30px;
    margin-left: 200px;
    margin-top: 80px;
}

.left-col {
    border: 10px;
    border-right-style: solid;
    border-width: 2px;
    border-color: white;
}
.left-buttons {
    margin-top: 40px;
    height: 360px;
    /* border: 10px; */
    /* align-content: center; */
}
.left-button {
    margin-top: 55px;
    margin-left: 40px;
    width: 80px;
    
}


.right-login {
    margin-right: 20px;
}
</style>
