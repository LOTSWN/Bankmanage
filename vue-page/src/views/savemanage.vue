<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-calendar"></i> 表单
                </el-breadcrumb-item>
                <el-breadcrumb-item>存款账号信息</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="form-box">
                <el-form :model="form" status-icon :rules="rules" ref="form"  label-width="80px">

                    <el-form-item label="账号ID">
                        <el-input readonly v-model="form.saveID"></el-input>
                    </el-form-item>

                    <el-form-item label="客户ID">
                        <el-input readonly v-model="form.clientID"></el-input>
                    </el-form-item>

                    <el-form-item label="余额">
                        <el-input readonly v-model="form.moneynum"></el-input>
                    </el-form-item>

                    <el-form-item label="账号类型">
                        <el-input readonly v-model="form.savetype"></el-input>
                    </el-form-item>

                    <el-form-item label="月利率">
                        <el-input readonly v-model="form.rate"></el-input>
                    </el-form-item>

                    <el-form-item>
                        <el-button type="primary" @click="editVisible1 = true">存款</el-button>
                        <el-button type="primary" @click="editVisible2 = true">取款</el-button>
                        <el-button type="primary" @click="editVisible3 = true">年限修改</el-button>
                        <el-button type="primary" @click="Delete(form.saveID)">注销</el-button>
                        <el-button @click="editVisible = true">登录</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>

        <el-dialog title="储蓄账号登录" v-model="editVisible" width="30%">
            <el-form ref="loginform" :model="loginform" label-width="70px">
                <el-form-item label="账号ID">
                    <el-input v-model="loginform.saveID"></el-input>
                </el-form-item>
                <el-form-item label="密码">
                    <el-input v-model="loginform.password"></el-input>
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button type="primary" @click="savelogin">确 定</el-button>
                </span>
            </template>
        </el-dialog>

        <el-dialog title="储蓄类型更改" v-model="editVisible3" width="30%">
            <el-form ref="loginform" label-width="70px">
                    <el-form-item label="存款类型">
                        <el-select v-model="changetype" placeholder="请选择">
                            <el-option key="活期" label="活期" value="活期"></el-option>
                            <el-option key="定期一年" label="定期一年" value="定期一年"></el-option>
                            <el-option key="定期三年" label="定期三年" value="定期三年"></el-option>
                            <el-option key="定期五年" label="定期五年" value="定期五年"></el-option>
                        </el-select>
                    </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button type="primary" @click="tochangetype">确 定</el-button>
                </span>
            </template>
        </el-dialog>

        <el-dialog title="取款" v-model="editVisible2" width="30%">
            <el-form ref="loginform" label-width="70px">
                <el-input oninput="value=value.replace(/[^\d]/g,'')" v-model="changemoney"></el-input>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button type="primary" @click="tochangemoney(2)">确 定</el-button>
                </span>
            </template>
        </el-dialog>

        <el-dialog title="存款" v-model="editVisible1" width="30%">
            <el-form ref="loginform" label-width="70px">
                <el-input oninput="value=value.replace(/[^\d]/g,'')" v-model="changemoney"></el-input>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button type="primary" @click="tochangemoney(1)">确 定</el-button>
                </span>
            </template>
        </el-dialog>



    </div>
</template>

<script>
import {ElMessage } from 'element-plus'
import $ from 'jquery'
export default {
    name: 'savemanage',
    data() {
        return {
            form: {
                readonly: true,
                clientID: '',
                saveID: '',
                moneynum: '',
                savetype: '',
                rate: '',
            },
            loginform:{
                saveID:'',
                password:'',
            },
            changetype:'',
            changemoney:'',
            editVisible:true,
            editVisible1:false,
            editVisible2:false,
            editVisible3:false,
         };
    },
    methods: {
        getData(nowId) {
          var data = {
            data: JSON.stringify({
                "saveID": nowId,
           })
          }
          var temp
          $.ajax({
          url: 'http://127.0.0.1:9529/findasave',
          type: 'POST',
          data: data,
          async: false, //设置ajax为同步请求
          dataType: 'text',
          success: function(responses) {   
            if(res=="failed")
            {             
             ElMessage("获取数据错误")
            }
            else{
                var res = JSON.parse(responses);                
                temp=res;
                console.log(temp)
            }  
           },
          error: function() {
             ElMessage("获取数据错误")
          }
      })
        this.form.clientID=temp.clientID;
        this.form.saveID=temp.saveID;
        this.form.moneynum=temp.moneynum;
        this.form.savetype=temp.savetype;
        this.form.rate=temp.rate;          
        
        },
        Delete: function (saveID) {
                if(this.form.moneynum>0)
                {
                ElMessage("账户余额不为0，注销失败！");
                return ;
                }
                var data = {
                  data: JSON.stringify({
                    'saveID': saveID
                  })
                }
                $.ajax({
                  url: 'http://127.0.0.1:9529/deleteasave',
                  type: 'POST',
                  data: data,
                  async: false, //设置ajax为同步请求
                  dataType: 'text',
                  success: function(res) {                      
                      if(res=="failed")
                      {
                      ElMessage("无数据！请确认后再输入");    
                      }
                      else{
                      ElMessage("删除成功");    
                      }
                  },
                  error: function() {
                      ElMessage("错误");    
                  }                  
                })
                this.clean()
                this.editVisible=true;
        },
        savelogin()
        {
          var data = {
            data: JSON.stringify({
                "saveID": this.loginform.saveID,
                "password": this.loginform.password
           })
          }
          var flag=false;

          $.ajax({
          url: 'http://127.0.0.1:9529/savelogin',
          type: 'POST',
          data: data,
          async: false, //设置ajax为同步请求
          dataType: 'text',
          success: function(res) {   
            // console.log(res)
                if (res === 'success'){
                    flag=true;
                    ElMessage("修改成功！")
                } 
                else if (res === 'account lose' ){
                    ElMessage("账号不存在！")
                }
                else if (res === 'wrong password' ){
                    ElMessage("密码错误！")
                }
           },
          error: function() {
             ElMessage("修改失败！")
          }
         })
         if(flag==true)
         {
            this.getData(this.loginform.saveID)
            this.editVisible=false;
         }
       },
        tochangetype()
        {
          var data = {
            data: JSON.stringify({
                "changetype": this.changetype,
                "saveID":this.form.saveID,
           })
          }
         var flag=false;
         $.ajax({
          url: 'http://127.0.0.1:9529/changesavetype',
          type: 'POST',
          data: data,
          async: false, //设置ajax为同步请求
          dataType: 'text',
          success: function(res) {   
            // console.log(res)
                if (res === 'success'){
                    ElMessage("修改成功！")
                    flag=true
                } 
                else if (res === 'failed' ){
                    ElMessage("修改失败！")
                }
           },
          error: function() {
             ElMessage("登录失败！")
          }
         })
         if(flag==true)
         {
             this.changetype=''
             this.getData(this.form.saveID)
         }
        },
        tochangemoney: function(key)
        {
          var money
          if(key==1) money=parseInt(this.form.moneynum)+parseInt(this.changemoney)
          else if(key==2) money=parseInt(this.form.moneynum)-parseInt(this.changemoney)
          if(money<0)
          {
              this.changemoney=''
              ElMessage("卡内余额不足！");
              return ;
          }
          if(money>999999999999999)
          {
              this.changemoney=''
              ElMessage("您没有这么多钱！");
              return ;
          }
          if(this.form.savetype!='活期')
          {
              this.changemoney=''
              ElMessage("非活期账户不可存取款!");
              return ;
          }
          
          var data = {
            data: JSON.stringify({
                "saveID":this.form.saveID,
                "moneynum":money,
           })
          }
         var flag=false;
         $.ajax({
          url: 'http://127.0.0.1:9529/changemoney',
          type: 'POST',
          data: data,
          async: false, //设置ajax为同步请求
          dataType: 'text',
          success: function(res) {   
            // console.log(res)
                if (res === 'success'){
                    ElMessage("修改成功！")
                    flag=true
                } 
                else if (res === 'failed' ){
                    ElMessage("修改失败！")
                }
           },
          error: function() {
             ElMessage("登录失败！")
          }
         })
         if(flag==true)
         {
             this.changemoney=''
             this.getData(this.form.saveID)
         }
        },
        clean()
        {
            this.form.savetype='',
            this.form.clientID='',
            this.form.moneynum=''
            this.form.saveID='',
            this.form.rate=''
        }


    }


};
</script>