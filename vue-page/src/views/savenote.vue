<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-calendar"></i> 表单
                </el-breadcrumb-item>
                <el-breadcrumb-item>储蓄账号信息</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="form-box">
                <el-form :model="form" status-icon :rules="rules" ref="form"  label-width="80px">

                    <el-form-item label="客户ID">
                        <el-input v-model="form.clientID"></el-input>
                    </el-form-item>

                    <el-form-item label="密码" prop="pass">
                    <el-input type="password" oninput="value=value.replace(/[^\d]/g,'')" v-model="form.pass" autocomplete="off">输入六位数银行卡密码</el-input>
                    </el-form-item>
                    <el-form-item label="确认密码" prop="checkPass">
                    <el-input type="password" oninput="value=value.replace(/[^\d]/g,'')" v-model="form.checkPass" autocomplete="off">请再次输入</el-input>
                    </el-form-item>

                    <el-form-item label="存款金额">
                    <el-input oninput="value=value.replace(/[^\d]/g,'')" v-model="form.moneynum"></el-input>
                    </el-form-item>


                    <el-form-item label="存款类型">
                        <el-select v-model="form.savetype" placeholder="请选择">
                            <el-option key="活期" label="活期" value="活期"></el-option>
                            <el-option key="定期一年" label="定期一年" value="定期一年"></el-option>
                            <el-option key="定期三年" label="定期三年" value="定期三年"></el-option>
                            <el-option key="定期五年" label="定期五年" value="定期五年"></el-option>
                        </el-select>
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
    name: 'savenote',
    data() {
      var validatePass = (rule, value, callback) => {

        if (value === '') {
          callback(new Error('请输入六位数密码'));
        } 
        else if(value.length != 6){
          callback(new Error('密码格式错误'));
        }
        else {
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
                checkPass:'',
                moneynum: '',
                savetype: '',
                begindate:this.getNowFormatDate(),
                overdate:'',
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

          if (this.form.savetype == "活期"){
            this.form.overdate="none"
            this.form.rate=0.003
          } 
          else if (this.form.savetype == "定期一年")
          {
            this.form.overdate=this.moredate(1)
            this.form.rate=0.005
          }
          else if (this.form.savetype == "定期三年")
          {
            this.form.overdate=this.moredate(3)
            this.form.rate=0.008
          }
          else if (this.form.savetype == "定期五年")
          {
            this.form.overdate=this.moredate(5)
            this.form.rate=0.01
          }
          console.log(this.form.overdate)
          var data = {
            data: JSON.stringify({
                "clientID": this.form.clientID,
                "password": this.form.pass,
                "moneynum": this.form.moneynum,
                "savetype": this.form.savetype,
                "begindate": this.form.begindate,
                "overdate": this.form.overdate,
                "rate": this.form.rate,
           })
          }

          if((this.form.pass==this.form.checkPass)&&(this.form.pass.length == 6))
          {
          console.log(data)
          $.ajax({
          url: 'http://127.0.0.1:9529/newsave',
          type: 'POST',
          data: data,
          async: false, //设置ajax为同步请求
          dataType: 'text',
          success: function(res) {   
            if(res=="success")
            {
             ElMessage("注册成功！") 
            }
            else if(res=="failed")
            {
             ElMessage("创建失败鸭！")
            }
            else if(res=="wrongclient")  
            {
             ElMessage("用户不存在！")
            }
           },
          error: function() {
             ElMessage("创建失败！")
          }

      })
          }
          else
          {
              ElMessage("信息错误！")
          }

        },
      cleanall() {
          this.form.clientID= ''
          this.form.pass=''
          this.form.moneynum=''
          this.form.checkPass=''
          this.form.savetype=''
       },
       moredate: function (type)
       {
         var temp=this.form.begindate
         var mystr=temp.split("-")
         mystr[0]=(parseInt(mystr[0])+parseInt(type)).toString()
         mystr=mystr[0]+'-'+mystr[1]+'-'+mystr[2]
         return mystr
       }
    }
};
</script>