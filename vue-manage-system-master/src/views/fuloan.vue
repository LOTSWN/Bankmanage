<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-cascades"></i> 贷款信息
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="handle-box">
                <el-input v-model="query.name" placeholder="请输入客户ID" class="handle-input mr10"></el-input>
                <el-button type="primary" icon="el-icon-search" @click="getData">搜索</el-button>
            </div>
                 
            <table class="pure-table">
                <thead>
                    <tr>
                        <th style="width:150px">贷款ID</th>
                        <th style="width:150px">客户ID</th>
                        <th style="width:100px">贷款金额</th>
                        <th style="width:100px">月利率</th>
                        <th style="width:120px">办理支行</th>
                    </tr>
                </thead>
                <tbody>

                    <template v-for="(row) in vrows "  >
                        <!-- eslint-disable-next-line--> 
                         <tr>
                        <td>{{row.loanID}}</td>
                        <td>{{row.clientID}}</td>
                        <td>{{row.loannum}}</td>
                        <td>{{row.rate}}</td>
                        <td>{{row.openbank}}</td>
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

    </div>
</template>

<script>
// import { fetchData } from "../api/index";
import $ from 'jquery'
import { ElMessage } from 'element-plus'
export default {
    name: "fuloan",
    data() {
        return {
            query: {
                name: "",
                pageIndex: 1,
                pageSize: 5,
                minnpage: 0,
                maxxpage: 5
            },
            pageTotal: 0,
            form: {},
            rows: [],
            vrows: [],
            rowtemplate: { loanID: '', loannum: '', clientID: '', rate: '', startdate: '', openbank: ''}
        };
    },
    methods: {
        getData()   {
            var data = {
                  data: JSON.stringify({
                    'keyword': this.query.name
                  })
            }
            var rowtemplate={ loanID: '', loannum: '', clientID: '', rate: '', startdate: '', openbank: ''}
            var flag=false
            var ri=0
            var rowts=Array()                 
                $.ajax({
                  url: 'http://127.0.0.1:9529/fuloan',
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
                      console.log(res)
                      for(ri in res)
                      {
                      rowtemplate= { loanID:res[ri].loanID, loannum:res[ri].loannum, clientID:res[ri].clientID, rate:res[ri].rate, startdate:res[ri].startdate, openbank:res[ri].openbank}
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
        },
            handlePageChange: function (val) {
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

