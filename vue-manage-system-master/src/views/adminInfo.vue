<template>
<el-container>
  <el-main class="mybox boxleft"> 
<div class="box-card" style="width:200px">
  <div name="header" class="clearfix">
    <span>您好！<div class="text item"> {{staffname}} </div></span>
    <br><br><hr><br><br>
  </div> 
  <div class="text item"> 账号ID：{{staffID}} </div>
  <div class="text item"> 姓名：{{staffname}} </div>
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
                            <!-- <el-date-picker
                                v-model="vdate"
                                style="width: 100%;"
                                type="date"
                            ></el-date-picker> -->
      
      </el-header>
    <el-main class="mybox boxright">待添加内容</el-main>
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
      var res_msg
      var isAdmin
      $.ajax({
          url: 'http://127.0.0.1:9529/admininfo',
          type: 'POST',
          data: data,
          async: false, //设置ajax为同步请求
          dataType: 'JSON',
           success: function(res) {
             if(res == 'refuse'){
               isAdmin = false
             }else{
               isAdmin = true
               res_msg = res;//保存在本地
             }
           }
      })
      if (isAdmin == true){
        return {
          staffID: res_msg['staffID'],
          staffname: res_msg['staffname'],
          gender: res_msg['gender'],
          age: res_msg['age'],
          level: res_msg['level'],
          workBank: res_msg['workbank'],
          vdate:this.getNowFormatDate()
        }
      }else {
        this.$message('您没有管理员权限');
        return {
          staffID: '您没有管理员权限',
          staffname: '您没有管理员权限',
          gender: '您没有管理员权限',
          age: '您没有管理员权限',
          level: '您没有管理员权限',
          workBank: '您没有管理员权限',
          vdate:this.getNowFormatDate()
        }
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