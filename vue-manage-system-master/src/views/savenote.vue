<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-calendar"></i> 表单
                </el-breadcrumb-item>
                <el-breadcrumb-item>存储账号信息</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="form-box">
                <el-form :model="form" status-icon :rules="rules" ref="form"  label-width="80px">

                    <el-form-item label="客户ID">
                        <el-input v-model="form.clientID"></el-input>
                    </el-form-item>

                    <el-form-item label="密码" prop="pass">
                    <el-input type="password" v-model="form.pass" autocomplete="off">输入六位数银行卡密码</el-input>
                    </el-form-item>
                    <el-form-item label="确认密码" prop="checkPass">
                    <el-input type="password" v-model="form.checkPass" autocomplete="off">请再次输入</el-input>
                    </el-form-item>

                    <el-form-item label="姓名">
                        <el-input v-model="form.name"></el-input>
                    </el-form-item>


                    <el-form-item label="存款类型">
                        <el-select v-model="form.savetype" placeholder="请选择">
                            <el-option key="class1" label="活期" value="class1"></el-option>
                            <el-option key="class2" label="定期一年" value="class2"></el-option>
                            <el-option key="class3" label="定期三年" value="class3"></el-option>
                            <el-option key="class4" label="定期五年" value="class4"></el-option>
                        </el-select>
                    </el-form-item>

                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">表单提交</el-button>
                        <el-button>取消</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
    name: 'savenote',
    data() {
      var validatePass = (rule, value, callback) => {

        if (value === '') {
          callback(new Error('请输入密码'));
        } 
        else if(value.length > 6){
          callback(new Error('密码长度超出'));
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
                moneynum: 0,
                savetype: '',
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
                "moneynum": 0,
                "savetype": this.form.savetype,
                "begindate": this.getNowFormatDate(),
                overdate: '',
                rate: '',
           })
          }

          if (data.savetype == "活期"){
            data.voerdate="none"
            data.rate=1
} 
          else if (data.savetype == "定期一年")
          {
            data.voerdate="none"
            data.rate=1
          }
          else if (data.savetype == "定期三年")
          {
            data.voerdate="none"
            data.rate=1
}
          else if (data.savetype == "定期四年")
          {
            data.voerdate="none"
            data.rate=1
}


          $.ajax({
          url: 'http://127.0.0.1:9529/savenote',
          type: 'POST',
          data: data,
          async: false, //设置ajax为同步请求
          dataType: 'text',
          success: function(res) {   
            console.log(res)
            this.$message.success('提交成功！');
           },
          error: function() {
            this.$message.success('出现错误！');
          }



      })



        }
    }
};
</script>