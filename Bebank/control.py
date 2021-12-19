from flask import Flask , request,render_template,jsonify
import json
from Dao.ClientDao import ClientDao
from Dao.SaveDao import SaveDao
from Dao.StaffDao import StaffDao
from Dao.LoanDao import LoanDao
from flask_cors import CORS
from Service.Hash import hash_passwd
app = Flask(__name__)
CORS(app)
@app.route("/login", methods=["GET", "POST"])         #客户登陆验证
def checkLogin():                  
    cd= ClientDao()
    data = json.loads(request.form.get('data'))
    username = data['username']
    password = data['password']
    diccd=cd.findclientByID(theId=username)

    if diccd == None:
        return "account lose"
    if(diccd['password']==hash_passwd(password)) :
        return "success"
    else :
        return "wrong password"

@app.route("/adminlogin", methods=["GET", "POST"]) #管理员登录验证
def checkStaffLogin():
    cd = StaffDao()
    data = json.loads(request.form.get('data'))
    username = data['username']
    password = data['password']
    diccd=cd.findstaffByID(theId=username)

    if diccd == None:
        return "account lose"
    if(diccd['password']==password) :
        return "success"
    else :
        return "wrong password"


@app.route("/savelogin", methods=["GET", "POST"]) #储蓄账号登录验证
def checkSaveLogin():
    cd = SaveDao()
    data = json.loads(request.form.get('data'))
    saveID = data['saveID']
    password = data['password']
    diccd=cd.findsaveByID(theId=saveID)
    print(saveID)

    if diccd == None:
        return "account lose"
    if(diccd['password']==hash_passwd(password)) :
        return "success"
    else :
        return "wrong password"


@app.route("/findauser", methods=["GET", "POST"])  #根据用户ID查找用户
def findauser():
    cd= ClientDao()
    data = json.loads(request.form.get('data'))
    keyword = data['keyword']
    responce=cd.findclientByID(theId=keyword)
    if responce == None:
        return "failed"
    res=json.dumps(responce)
    return  res

@app.route("/findsuser", methods=["GET", "POST"]) #根据银行ID查找用户
def findsuser():
    cd= ClientDao()
    data = json.loads(request.form.get('data'))
    keyword = data['keyword']
    responce=cd.findclientByBK(openBank=keyword)
    if responce == None:
        return "failed"
    res=json.dumps(responce)
    return  res

@app.route("/findasave", methods=["GET", "POST"]) #根据ID查找储蓄账户
def findasave():
    cd= SaveDao()

    data = json.loads(request.form.get('data'))
    keyword = data['saveID']
    responce=cd.findsaveByID(theId=keyword)
    if responce == None:
        return "failed"
    res=json.dumps(responce)
    return  res


@app.route("/deleteauser", methods=["GET", "POST"]) #根据银行ID删除用户
def delauser():
    cd= ClientDao()
    data = json.loads(request.form.get('data'))
    keyword = data['clientID']
    responce=cd.delclientByID(theId=keyword)
    return  responce

@app.route("/fastaff", methods=["GET", "POST"]) #根据管理员ID查找管理员
def fastaff():
    cd= StaffDao()
    data = json.loads(request.form.get('data'))
    keyword = data['staffID']
    responce=cd.findstaffByID(theId=keyword)
    res=json.dumps(responce)
    return  res

@app.route("/newclient", methods=["GET", "POST"]) #创建
def newclient():
    cd= ClientDao()
    data = json.loads(request.form.get('data'))
    responce=cd.newclient(data=data)
    return  responce

@app.route("/newsave", methods=["GET", "POST"]) #创建
def newsave():
    ce= ClientDao()
    cd= SaveDao()
    data = json.loads(request.form.get('data'))
    resc=ce.findclientByID(data['clientID'])
    if(resc==None):
        return "wrongclient"
    responce=cd.newsave(data=data)
    return  responce

@app.route("/newloan", methods=["GET", "POST"]) #创建
def newloan():
    ce= ClientDao()
    cd= LoanDao()
    data = json.loads(request.form.get('data'))
    resc=ce.findclientByID(data['clientID'])
    if(resc==None):
        return "wrongclient"
    responce=cd.newloan(data=data)
    return  responce


@app.route("/fusave", methods=["GET", "POST"]) #根据用户ID查找储蓄账户
def findssave():
    cd= SaveDao()
    data = json.loads(request.form.get('data'))
    keyword = data['keyword']
    responce=cd.findsaveByCK(clientID=keyword)
    if responce == None:
        return "failed"
    res=json.dumps(responce)
    return  res

@app.route("/fuloan", methods=["GET", "POST"]) #根据用户ID查找储蓄账户
def findsloan():
    cd= LoanDao()
    data = json.loads(request.form.get('data'))
    keyword = data['keyword']
    responce=cd.findloanByCK(clientID=keyword)
    if responce == None:
        return "failed"
    res=json.dumps(responce)
    return  res


@app.route("/deleteasave", methods=["GET", "POST"]) #根据账号ID删除账号
def delasave():
    cd= SaveDao()
    data = json.loads(request.form.get('data'))
    keyword = data['saveID']
    responce=cd.delsaveByID(saveID=keyword)
    return  responce

@app.route("/changesavetype", methods=["GET", "POST"]) #改变储蓄账户类型
def changesavetype():
    cd= SaveDao()
    data = json.loads(request.form.get('data'))
    saveID = data['saveID']
    changetype = data['changetype']
    res=cd.changeyear(saveID=saveID,changetype=changetype)
    return res
    
@app.route("/changemoney", methods=["GET", "POST"]) #改变储蓄账户类型
def changemoney():
    cd= SaveDao()
    data = json.loads(request.form.get('data'))
    moneynum = data['moneynum']
    saveID = data['saveID']
    res=cd.moneychange(moneynum=moneynum,saveID=saveID)
    return res

@app.route("/changeuser", methods=["GET", "POST"]) #改变储蓄账户类型
def changeuser():
    cd= ClientDao()
    data = json.loads(request.form.get('data'))
    res=cd.userchange(data=data)
    return res

if __name__ == '__main__':
    app.run(host="localhost",port=9529)
