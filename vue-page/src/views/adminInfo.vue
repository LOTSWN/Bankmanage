<template>
<el-container>
  <el-main class="mybox boxleft"> 
<div class="box-card" style="width:200px">
  <div name="header" class="clearfix">
    <span>管理员：{{staffname}}</span>
    <br><br><hr><br><br>
  </div> 
  <div class="text item"> 账号ID：{{staffID}} </div>
  <div class="text item"> 性别：{{gender}} </div>
  <div class="text item"> 年龄：{{age}} </div>
  <div class="text item"> 职务：{{level}} </div>
  <div class="text item"> 所在支行：{{workBank}} </div>
</div>      

  </el-main>
  <el-container>
    <el-header class="mybox boxtop" style="padding: 20px,5px,5px,5px;">
      <br>
      当前时间：{{vdate}}
      </el-header>
    <el-main class="mybox boxright">Main</el-main>
  </el-container>
</el-container>

</template>

<script>
import $ from 'jquery'
export default {
    name:"admininfo",
    data() {
      var data = {
        data: JSON.stringify({
        'staffID': localStorage.getItem("user_id"),
        })
      }
      var res
      $.ajax({
          url: 'http://127.0.0.1:9529/fastaff',
          type: 'POST',
          data: data,
          async: false, //设置ajax为同步请求
          dataType: 'text',
           success: function(responses) {  
             res = JSON.parse(responses);
             console.log(res.workBank)        
           }
      })
      return {      
        staffID: res.staffID,
      staffname: res.staffname,
         gender: res.gender,
            age: res.age,
          level: res.level,
       workBank: res.workBank,
          vdate:this.getNowFormatDate()
      }
    },
    methods:{
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
     }
    }
    
}
</script>
<style scoped>

.myheader{
     font-family:"Hiragino Sans GB";
     text-align:center;
     font-size:30px;
}

.mybox{
   background-color: #FFFFFF;
   box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
   border-radius: 4px;
}
.boxtop{
   margin:5px 5px 10px 20px;
}
.boxleft{
   width:"600px";
   margin:5px 40px 0px 10px;
}
.boxright{
   margin:5px 5px 0px 20px;
}
 .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
</style>