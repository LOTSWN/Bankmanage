from Dao.connectionPool import connectionPool


class SaveDao(object):
    def __init__(self):
        self.ac = connectionPool()
        (self.cur, self.con) = self.ac.getconn()  # con：连接；cur：连接的对象

    def findsaveByID(self, theId):  # 根据ID查找储蓄账号
        sql = "SELECT * FROM `savenote` WHERE `saveID` LIKE " + "'" + str(theId) + "'"
        try:
            self.cur.execute(sql)
            list = self.cur.fetchall()
            nowStaff = self.__lisTodic(list[0])
            return nowStaff
        except:
            return None
    

    def newsave(self,data):     #创建客户
        sql='INSERT INTO `savenote` (`saveID`, `password`, `clientID`, `moneynum`, `savetype`, `begindate`, `overdate`, `rate`) VALUES ({t0},\'{t1}\', \'{t2}\', \'{t3}\', \'{t4}\', \'{t5}\', \'{t6}\', \'{t7}\');'.format(t0="NULL",t1=data['password'],t2=data['clientID'],t3=data['moneynum'],t4=data['savetype'],t5=data['begindate'],t6=data['overdate'],t7=data['rate'])
        try:
            self.cur.execute(sql)
            return "success"
        except:
            return "failed"

    def findsaveByCK(self,clientID):     #根据客户ID查找储蓄账户
        sql="SELECT * FROM `savenote` WHERE `clientID` LIKE "+"'"+clientID+"'"
        try:
            self.cur.execute(sql)
            list=self.cur.fetchall()
            aditc=[]
            for i in range(len(list)):
                # aditc[i]=self.__lisTodic(list[i])
                aditc.append(self.__lisTodic(list[i]))
            if(len(list)==0):
                return None
            else: 
                return aditc
        except:
            return None

    def delsaveByID(self,saveID):     #根据账号ID删除
        sql="DELETE FROM `savenote` WHERE `savenote`.`saveID` ="+"'"+ str(saveID)+"'"
        try:
            self.cur.execute(sql)
            return "success"
        except:
            return "failed"

    def moneychange(self,moneynum,saveID):
        sql="UPDATE `savenote` SET `moneynum` = "+"'"+str(moneynum)+"'"+" WHERE `savenote`.`saveID` = "+str(saveID)+";"
        try:
            self.cur.execute(sql)
            return "success"
        except:
            return "failed"

    def changeyear(self,saveID,changetype):
       if(changetype=="定期五年"):
            rate=0.01
       elif(changetype=="定期三年"):
            rate=0.008
       elif(changetype=="定期一年"):
            rate=0.005
       elif(changetype=="活期"):
            rate=0.003
       sql="UPDATE `savenote` SET `savetype` = "+"'"+changetype+"', `rate` = "+"'"+str(rate)+"' WHERE `savenote`.`saveID` = "+str(saveID)+";"
       print(sql)
       try:
            self.cur.execute(sql)
            return "success"
       except:
            return "failed"
    
    def __lisTodic(self, list):  # 列表转字典
        title = []
        title = ["saveID","password", "clientID", "moneynum", "savetype", "begindate", "overdate", "rate"]
        nowls = {}
        for i in range(len(list)):
            if str(list[i].__class__) == '<class \'bytes\'>':
                nowls[title[i]] = str(list[i], encoding="utf-8")
            else:
                nowls[title[i]] = list[i]  # bytes外类型暂不处理
        # print(nowClient)
        return nowls




