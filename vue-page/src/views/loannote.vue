<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-calendar"></i> 表单
                </el-breadcrumb-item>
                <el-breadcrumb-item>贷款信息填报</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="form-box">
                <el-form :model="form" status-icon :rules="rules" ref="form"  label-width="80px">

                    <el-form-item label="客户ID">
                        <el-input v-model="form.clientID"></el-input>
                    </el-form-item>


                    <el-form-item label="贷款额度">
                        <el-select v-model="form.loannum" placeholder="高额贷款需在附件中说明">
                            <el-option key="壹万" label="壹万" value="壹万"></el-option>
                            <el-option key="拾万" label="拾万" value="拾万"></el-option>
                            <el-option key="伍拾万" label="伍拾万" value="伍拾万"></el-option>
                            <el-option key="高额贷款" label="高额贷款" value="高额贷款"></el-option>
                        </el-select>
                    </el-form-item>

                    <el-form-item label="受理支行">
                        <el-input v-model="form.openbank"></el-input>
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
    name: 'loannote',
    data() {
        
        return {
            form: {
                loannum: '',
                clientID: '',
                openbank: '',
                rate:'',
            },
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
      cleanall() {
          this.form.clientID= ''
          this.form.clientID=''
          this.form.openbank=''
       },
        onSubmit() {
          if(this.form.loannum=="壹万")
          {
                 this.form.rate=0.01
          }  
          else if(this.form.loannum=="拾万")
          {
                 this.form.rate=0.012
          }
          else if(this.form.loannum=="伍拾万")
          {
                 this.form.rate=0.015
          }
          else if(this.form.loannum=="高额贷款")
          {
                 this.form.rate="none"
          }
          var data = {
            data: JSON.stringify({
                "clientID": this.form.clientID,
                "loannum": this.form.loannum,
                "openbank": this.form.openbank,
                "startdate": this.getNowFormatDate(),
                "rate": this.form.rate,
           })
          }

          $.ajax({
          url: 'http://127.0.0.1:9529/newloan',
          type: 'POST',
          data: data,
          async: false, //设置ajax为同步请求
          dataType: 'text',
          success: function(res) {   
            if(res=="success")
            {
             ElMessage("申请提交成功！") 
            }
            else if(res=="failed")
            {
             ElMessage("提交失败鸭！")
            }
            else if(res=="wrongclient")  
            {
             ElMessage("用户不存在！")
            }
           },
          error: function() {
             ElMessage("提交失败！")
          }

      })



        }
    }
};
</script>