<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-calendar"></i> 表单
                </el-breadcrumb-item>
                <el-breadcrumb-item>客户信息</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="form-box">
                <el-form :model="form" status-icon :rules="rules" ref="form"  label-width="80px">

                    <el-form-item label="客户ID">
                        <el-input v-model="form.clientID"></el-input>
                    </el-form-item>

                    <el-form-item label="密码" prop="pass">
                    <el-input type="password" v-model="form.pass" show-password></el-input>
                    </el-form-item>
                    <el-form-item label="确认密码" prop="checkPass">
                    <el-input type="password" v-model="form.checkPass" show-password></el-input>
                    </el-form-item>

                    <el-form-item label="姓名">
                        <el-input v-model="form.name"></el-input>
                    </el-form-item>


                    <el-form-item label="性别">
                        <el-select v-model="form.gender" placeholder="请选择">
                            <el-option key="male" label="男" value="male"></el-option>
                            <el-option key="female" label="女" value="female"></el-option>
                        </el-select>
                    </el-form-item>

                    <el-form-item label="年龄">
                        <el-input v-model="form.age"></el-input>
                    </el-form-item>

                    <el-form-item label="联系电话">
                        <el-input v-model="form.telephone"></el-input>
                    </el-form-item>

                    <el-form-item label="开户行">
                        <el-input v-model="form.openBank"></el-input>
                    </el-form-item>




                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">表单提交</el-button>
                        <el-button  @click="cleanall"> 重置</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script>
import {ElMessage } from 'element-plus'
import $ from 'jquery'
export default {
    name: 'newclient',
    data() {
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.form.checkPass !== '') {
            this.$refs.form.validateField('checkPass');
          }
          callback();
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.form.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
        
        return {
            form: {
                clientID: '',
                pass: '',
                checkPass: '',
                gender: '',
                name: '',
                openTime: this.getNowFormatDate(),
                openBank: '',
                telephone: '',
                age:'',
            },
       rules: {
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { validator: validatePass2, trigger: 'blur' }
          ]
        }

        };
    },
    methods: {
      getNowFormatDate() {
          var date = new Date();
          var seperator1 = "-";
          var year = date.getFullYear();
          var month = date.getMonth() + 1;
          var strDate = date.getDate();
          if (month >= 1 && month <= 9) {
            month = "0" + month;
          }
          if (strDate >= 0 && strDate <= 9) {
             strDate = "0" + strDate;
          }
           var currentdate = year + seperator1 + month + seperator1 + strDate;
           return currentdate;
     },
        onSubmit() {
          var data = {

            data: JSON.stringify({
                "clientID": this.form.clientID,
                "password": this.form.pass,
                "gender": this.form.gender,
                "name": this.form.name,
                "openTime": this.form.openTime,
                "openBank": this.form.openBank,
                "telephone": this.form.telephone,
                "age":this.form.age,
           })
          }

          if(this.form.pass==this.form.checkPass)
          {
          $.ajax({
          url: 'http://127.0.0.1:9529/newclient',
          type: 'POST',
          data: data,
          async: false, //设置ajax为同步请求
          dataType: 'text',
          success: function(res) {   
            // console.log(res)
            if(res=="success")
            {
             ElMessage("注册成功！") 
            }
            else if(res=="failed")
            {
             ElMessage("用户名已注册！")
            }  
           },
          error: function() {
             ElMessage("注册失败！")
          }
      })
          }
          else
          {
             ElMessage("两次输入密码不一致！")
          }          
        },
      cleanall() {
          this.form.clientID=''
          this.form.pass=''
          this.form.checkPass=''
          this.form.gender=''
          this.form.name=''
          this.form.openBank=''
          this.form.telephone=''
          this.form.age=''
     }

    }


};
</script>