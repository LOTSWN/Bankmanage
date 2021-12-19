from Dao.connectionPool import connectionPool
from Service.Hash import hash_passwd
class ClientDao(object):

    def __init__(self):
        self.ac=connectionPool()
        (self.cur, self.con) = self.ac.getconn() #con：连接；cur：连接的对象

    def findclientByID(self,theId):     #根据ID查找单个客户
        sql="SELECT * FROM `client` WHERE `clientID` LIKE "+"'"+theId+"'"
        try:
            self.cur.execute(sql)
            list=self.cur.fetchall()
            nowClient=self.__lisTodic(list[0])
            return nowClient
        except:
            return None

    def delclientByID(self,theId):     #根据ID删除单个客户
        sql="DELETE FROM `client` WHERE `client`.`clientID` ="+"'"+ theId+"'"
        try:
            self.cur.execute(sql)
            return "success"
        except:
            return "failed"

    def newclient(self,data):#创建客户
        passwd = hash_passwd(data['password'])
        # print(passwd)
        sql='INSERT INTO `client` (`clientID`, `password`, `gender`, `name`, `openTime`, `openBank`, `telephone`, `age`) VALUES (\'{t1}\', \'{t2}\', \'{t3}\', \'{t4}\', \'{t5}\', \'{t6}\', \'{t7}\', \'{t7}\');'.format(t1=data['clientID'],t2=passwd,t3=data['gender'],t4=data['name'],t5=data['openTime'],t6=data['openBank'],t7=data['telephone'],t8=data['age'])
        try:
            self.cur.execute(sql)
            return "success"
        except:
            return "failed"

    def userchange(self,data):
        sql="UPDATE `client` SET `name` = '"+data['name']+"', `telephone` = '"+data['telephone']+"' WHERE `client`.`clientID` = '"+data['clientID']+"';"
        try:
            self.cur.execute(sql)
            return "success"
        except:
            return "failed"


    def findclientByBK(self,openBank):     #根据银行ID查找客户
        sql="SELECT * FROM `client` WHERE `openBank` LIKE "+"'"+openBank+"'"
        try:
            self.cur.execute(sql)
            list=self.cur.fetchall()
            # aditc={}
            aditc=[]
            for i in range(len(list)):
                # aditc[i]=self.__lisTodic(list[i])
                aditc.append(self.__lisTodic(list[i]))
            return aditc
        except:
            return None


    def __lisTodic(self,list): #列表转字典
        title=[]
        title=["clientID","password","gender","name","openTime","openBank","telephone","age"]
        nowClient={}
        for i in range(len(list)):
            if str(list[i].__class__) == '<class \'bytes\'>':
                nowClient[title[i]]=str(list[i], encoding = "utf-8")
            else :
                nowClient[title[i]] = list[i] #bytes外类型暂不处理
        return nowClient


            

if __name__=="__main__":
    new=ClientDao()
    cs=new.findclientByBK(openBank="bk001")
    print(cs)
