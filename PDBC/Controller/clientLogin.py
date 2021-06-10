from flask import Flask , request,render_template
import json
from Dao.ClientDao import ClientDao
from Dao.StaffDao import StaffDao
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/login", methods=["GET", "POST"])
def checkLogin():
    cd= ClientDao()
    data = json.loads(request.form.get('data'))
    username = data['username']
    password = data['password']
    diccd=cd.findclientByID(theId=username)

    if diccd == None:
        print("there")
        return "notfind"
    if(diccd['password']==password) :
        print("right")
        return "find"
    else :
        print("wrong")
        return "notfind"


@app.route("/Stafflogin", methods=["GET", "POST"])
def checkStaffLogin():
    cd = StaffDao()
    data = json.loads(request.form.get('data'))
    username = data['username']
    password = data['password']
    diccd=cd.findstaffByID(theId=username)

    if diccd == None:
        print("ID don't exist")
        return "notfind"
    if(diccd['password']==password) :
        print("right")
        return "find"
    else :
        print("wrong")
        return "notfind"

if __name__ == '__main__':
   app.run(host="localhost",port=9529)