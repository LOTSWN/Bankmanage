<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-cascades"></i> 用户信息
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="handle-box">
                <el-select v-model="query.type" placeholder="关键字" class="handle-select mr10">
                    <el-option key="1" label="客户ID" value="客户ID"></el-option>
                    <el-option key="2" label="支行编号" value="支行编号"></el-option>
                </el-select>
                <el-input v-model="query.name" placeholder="请输入查询内容" class="handle-input mr10"></el-input>
                <el-button type="primary" icon="el-icon-search" @click="getData">搜索</el-button>
            </div>
                 
            <table class="pure-table">
                <thead>
                    <tr>
                        <th style="width:120px">客户ID</th>
                        <th style="width:120px">姓名</th>
                        <th style="width:80px">性别</th>
                        <th style="width:80px">年龄</th>
                        <th style="width:120px">联系电话</th>
                        <th style="width:120px">开户行</th>
                        <th style="width:180px">操作</th>
                    </tr>
                </thead>
                <tbody>

                    <template v-for="(row) in vrows "  >
                        <!-- eslint-disable-next-line--> 
                         <tr>
                        <td>{{row.clientID}}</td>
                        <td>{{row.name}}</td>
                        <td>{{row.gender}}</td>
                        <td>{{row.age}}</td>
                        <td>{{row.telephone}}</td>
                        <td>{{row.openBank}}</td>
                        <td><el-button href="#" type="primary" plain @click="Edit(row)">编辑</el-button> <el-button type="primary" plain href="#" @click="Delete(row.clientID)">删除</el-button></td>
                        </tr>
                    </template>
                </tbody>
            </table>

            <div class="pagination">
                <el-pagination
                    background
                    layout="total, prev, pager, next"
                    :current-page="query.pageIndex"
                    :page-size="query.pageSize"
                    :total="pageTotal"
                    @current-change="handlePageChange"
                ></el-pagination>
            </div>
        </div>

        <!-- 编辑弹出框 -->
        <el-dialog title="编辑" v-model="editVisible" width="30%">
            <el-form ref="form" :model="form" label-width="70px">
                <el-form-item label="姓名">
                    <el-input v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="联系方式">
                    <el-input v-model="form.telephone"></el-input>
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="editVisible = false">取 消</el-button>
                    <el-button type="primary" @click="saveEdit">确 定</el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>

<script>
// import { fetchData } from "../api/index";
import $ from 'jquery'
import { ElMessage } from 'element-plus'
export default {
    name: "basetable",
    data() {
        return {
            query: {
                type: "",
                name: "",
                pageIndex: 1,
                pageSize: 5,
                minnpage: 0,
                maxxpage: 5
            },
            editVisible: false,
            pageTotal: 0,
            form: {},
            rows: [],
            vrows: [],
            rowtemplate: { clientID: '', name: '', gender: '', age: '', telephone: '',openBank: '' }
        };
        
    },
    methods: {
        getData()   {
            var data = {
                  data: JSON.stringify({
                    'keyword': this.query.name
                  })
            }
            var rowtemplate={ clientID: '', name: '', gender: '', age: '', telephone: '',openBank: '' }
            var flag=false

            if(this.query.type=="客户ID") 
            {
                $.ajax({
                  url: 'http://127.0.0.1:9529/findauser',
                  type: 'POST',
                  data: data,
                  async: false, //设置ajax为同步请求
                  dataType: 'text',
                  success: function(responses) {        
                      if(responses=="failed")
                      {
                      ElMessage("无数据！请确认后再输入");    
                      }
                      else{
                      flag=true    
                      var res = JSON.parse(responses);
                      rowtemplate = {clientID: res.clientID, name: res.name, gender: res.gender, age: res.age, telephone: res.telephone,openBank: res.openBank }
                      }
                  },
                  error: function() {
                      ElMessage("错误！");    
                  }                  
                })
                if(flag == true)
                {
                this.pageTotal=1    
                this.rows.splice(0,this.rows.length)
                this.rows.push(rowtemplate)
                this.refresh()
                }
            }
            else if(this.query.type=="支行编号")
            {
                var ri
                var rowts=Array()                 
                $.ajax({
                  url: 'http://127.0.0.1:9529/findsuser',
                  type: 'POST',
                  data: data,
                  async: false, //设置ajax为同步请求
                  dataType: 'text',
                  success: function(responses) {        
                      if(responses=="failed")
                      {
                      ElMessage("无数据！请确认后再输入");    
                      }
                      else{
                      flag=true    
                      var res = JSON.parse(responses);
                      for(ri in res)
                      {
                      rowtemplate = {clientID: res[ri].clientID, name: res[ri].name, gender: res[ri].gender, age: res[ri].age, telephone: res[ri].telephone,openBank: res[ri].openBank }
                      rowts.push(rowtemplate)
                      }
                      }
                  },
                  error: function() {
                      ElMessage("错误！");    
                  }                  
                })
                if(flag == true)
                {
                this.query.pageIndex=1
                this.query.pageSize=5    
                this.pageTotal=parseInt(ri)+1    
                this.rows.splice(0,this.rows.length)
                this.rows=rowts
                this.refresh()
                }

            }
            else 
            {
                ElMessage("请选择关键字！");    
            }


        },
            Delete: function (clientID) {
                var data = {
                  data: JSON.stringify({
                    'clientID': clientID
                  })
                }
                $.ajax({
                  url: 'http://127.0.0.1:9529/deleteauser',
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
                this.getData();
            },
            Edit: function (row) {
                this.form = row;
                this.editVisible = true;
            },
            saveEdit:function()
            {
            var data={data: JSON.stringify({
                "name": this.form.name,
                "telephone": this.form.telephone,
                "clientID":this.form.clientID
           })}
                $.ajax({
                  url: 'http://127.0.0.1:9529/changeuser',
                  type: 'POST',
                  data: data,
                  async: false, //设置ajax为同步请求
                  dataType: 'text',
                  success: function(res) {                      
                      if(res=="failed")
                      {
                      ElMessage("修改失败");    
                      }
                      else{
                      ElMessage("修改成功");    
                      }
                  },
                  error: function() {
                      ElMessage("错误");    
                  }                  
                })
                this.getData();
            },
            handlePageChange: function (val) {
                console.log("there wrong")
                this.query.pageIndex=val;
                this.refresh()
            },
            refresh: function () {
                this.query.minnpage=(this.query.pageIndex-1)*this.query.pageSize;
                this.query.maxxpage=this.query.minnpage+this.query.pageSize;
                this.vrows.splice(0,this.vrows.length)
                for(var ri in this.rows)
                {
                    if(ri>=this.query.minnpage&&ri<this.query.maxxpage)
                    {
                    console.log(this.rows[ri])
                    this.vrows.push(this.rows[ri])
                    }
                }
            },
    }
};
</script>

<style scoped>
.handle-box {
    margin-bottom: 20px;
}

.handle-select {
    width: 120px;
}

.handle-input {
    width: 300px;
    display: inline-block;
}
.table {
    width: 100%;
    font-size: 14px;
}
.red {
    color: #ff0000;
}
.mr10 {
    margin-right: 10px;
}
.table-td-thumb {
    display: block;
    margin: auto;
    width: 40px;
    height: 40px;
}
table {
    border-collapse: collapse;
    border-spacing: 0;
}
 
td,th {
    padding: 0;
}
 
.pure-table {
    border-collapse: collapse;
    border-spacing: 0;
    empty-cells: show;
    border: 1px solid #cbcbcb;
}
 
.pure-table caption {
    color: #000;
    font: italic 85%/1 arial,sans-serif;
    padding: 1em 0;
    text-align: center;
}
 
.pure-table td,.pure-table th {
    border-left: 1px solid #cbcbcb;
    border-width: 0 0 0 1px;
    font-size: inherit;
    margin: 0;
    overflow: visible;
    padding: .5em 1em;
}
 
.pure-table thead {
    background-color: #e0e0e0;
    color: #000;
    text-align: left;
    vertical-align: bottom;
}
 
.pure-table td {
    background-color: transparent;
}
</style>

