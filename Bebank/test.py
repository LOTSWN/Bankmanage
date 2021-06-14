from flask import Flask , request,render_template,jsonify
import json
from Dao.ClientDao import ClientDao
from Dao.StaffDao import StaffDao
from flask_cors import CORS


if __name__ == '__main__':
    new=ClientDao()
    cs=new.findclientByBK(openBank="bk001")
    print(cs)
