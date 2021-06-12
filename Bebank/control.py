from flask import Flask , request,render_template
import json
from Dao.ClientDao import ClientDao
from Dao.StaffDao import StaffDao
from Dao.ClientCreateDao import ClientCreateDao
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# 用户登录
@app.route("/login", methods=["GET", "POST"])
def checkLogin():
    cd = ClientDao()
    data = json.loads(request.form.get('data'))
    username = data['username']
    password = data['password']
    diccd=cd.findclientByID(theId=username)

    if diccd == None:
        return "account lose"
    if(diccd['password']==password) :
        return "success"
    else :
        return "wrong password"
# 管理员登录
@app.route("/adminlogin", methods=["GET", "POST"])
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
# 用户创建
@app.route("/newclient", methods=["GET", "POST"])
def getdata():
    cd = ClientCreateDao()
    data = json.loads(request.form.get('data'))
    clientID = data['clientID']
    password = data['password']
    name = data['name']
    gender = data['gender']
    age = data['age']
    telephone = data['telephone']
    openBank = data['openBank']
    openTime = data['openTime']
    flag = cd.insertNewClient(clientID, password, gender, name, openTime, openBank, telephone, age)

    if flag == None:
        return "insert error"
    if flag =="duplicateID":
        return "ID has been used"
    if flag == 1:
        return "insert success"
#adminifo
@app.route("/admininfo", methods=["GET", "POST"])
def pushdata():
    cd = StaffDao()
    data = json.loads(request.form.get('data'))
    user_id = data['staffID']
    diccd = cd.findstaffByID(theId=user_id)
    # print(user_id)
    if diccd == None :
     return "refuse"
    else:
     return diccd



if __name__ == '__main__':
   app.run(host="localhost",port=9529)