from Dao.connectionPool import connectionPool


class LoanDao(object):
    def __init__(self):
        self.ac = connectionPool()
        (self.cur, self.con) = self.ac.getconn()  # con：连接；cur：连接的对象
    

    def newloan(self,data):     #提交贷款申请
        sql="INSERT INTO `loannote` (`loanID`, `loannum`, `clientID`, `rate`, `startdate`, `openbank`) VALUES ({t0},\'{t1}\', \'{t2}\', \'{t3}\', \'{t4}\', \'{t5}\');".format(t0="NULL",t1=data['loannum'],t2=data['clientID'],t3=data['rate'],t4=data['startdate'],t5=data['openbank'])
        print(sql)
        try:
            self.cur.execute(sql)
            return "success"
        except:
            return "failed"

    def findloanByCK(self,clientID):     #根据客户ID查找储蓄账户
        sql="SELECT * FROM `loannote` WHERE `clientID` LIKE "+"'"+clientID+"'"
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


    def __lisTodic(self, list):  # 列表转字典
        title = []
        title = ["loanID","loannum", "clientID", "rate", "startdate", "openbank"]
        nowls = {}
        for i in range(len(list)):
            if str(list[i].__class__) == '<class \'bytes\'>':
                nowls[title[i]] = str(list[i], encoding="utf-8")
            else:
                nowls[title[i]] = list[i]  # bytes外类型暂不处理
        # print(nowClient)
        return nowls




