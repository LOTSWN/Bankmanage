<template>
    <div class="login-wrap">
        <div class="ms-login">
            <div class="ms-title">后台管理系统</div>
            <el-form :model="param" :rules="rules" ref="login" label-width="0px" class="ms-content">
                <el-form-item prop="username">
                    <el-input v-model="param.username" placeholder="username">
                        <template #prepend>
                            <el-button icon="el-icon-user"></el-button>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input
                        type="password"
                        placeholder="password"
                        v-model="param.password"
                        @keyup.enter="submitForm()"
                    >
                        <template #prepend>
                            <el-button icon="el-icon-lock"></el-button>
                        </template>
                    </el-input>
                </el-form-item>
                <div class="change-btn">
                    <el-button type="primary" @click="changeForm()">切换到管理员</el-button>
                </div>

                <div class="login-btn">
                    <el-button type="primary" @click="submitForm()">登录</el-button>
                </div>
                <p class="login-tips">网上银行管理系统</p>
            </el-form>
        </div>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
    data() {
        return {
            param: {
                username: "",
                password: ""
            },
            rules: {
                username: [
                    { required: true, message: "请输入用户名", trigger: "blur" }
                ],
                password: [
                    { required: true, message: "请输入密码", trigger: "blur" }
                ]
            }
        };
    },
    created() {
        this.$store.commit("clearTags");
    },
    methods: {
        submitForm() {
            this.$refs.login.validate(valid =>{
                if (valid){
                 valid = true
                }
                var data = {
                  data: JSON.stringify({
                    'username': this.param.username,
                    'password': this.param.password
                  })
                }
                $.ajax({
                  url: 'http://127.0.0.1:9529/login',
                  type: 'POST',
                  data: data,
                  async: false, //设置ajax为同步请求
                  dataType: 'text',
                  success: function(res) {
                    if (res === 'find'){
                        valid = true
                    } 
                    else {
                        valid = false
                    }
                  },
                  error: function() {
                      valid = false
                  }
                })

                if (valid) {
                    this.$message.success("登录成功");
                    localStorage.setItem("user_type", "normal");
                    localStorage.setItem("user_id", this.param.username);
                    this.$router.push("/");
                } else {
                    this.$message.error("登陆错误");
                    return false;
                }


            });
        },
        changeForm(){
            this.$message.success("切换成功");
            this.$router.push("/adminlogin");
        }
    }
};
</script>

<style scoped>
.login-wrap {
    position: relative;
    width: 100%;
    height: 100%;
    background-image: url(../assets/img/login-bg.jpg);
    background-size: 100%;
}
.ms-title {
    width: 100%;
    line-height: 50px;
    text-align: center;
    font-size: 20px;
    color: #fff;
    border-bottom: 1px solid #ddd;
}
.ms-login {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 350px;
    margin: -190px 0 0 -175px;
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.3);
    overflow: hidden;
}
.ms-content {
    padding: 30px 30px;
}
.login-btn {
    text-align: center;
}
.login-btn button {
    width: 100%;
    height: 36px;
    margin-bottom: 10px;
}

.change-btn {
    text-align: left;
}

.change-btn button {
    width: 100%;
    height: 36px;
    margin-bottom: 10px;
}


.login-tips {
    font-size: 12px;
    line-height: 30px;
    color: #fff;
}
</style>