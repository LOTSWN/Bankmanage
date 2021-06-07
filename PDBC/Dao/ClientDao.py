from Dao import connectionPool

class ClientDao(object):
    def __init__(self):
        self.ac=connectionPool.get_my_connection()
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

    def __lisTodic(self,list): #列表转字典
        title=[]
        title=["clientID","password","gender","name","openTime","openBank","telephone","age"]
        nowClient={}
        for i in range(len(list)):
            if str(list[i].__class__) == '<class \'bytes\'>':
                nowClient[title[i]]=str(list[i], encoding = "utf-8")
            else :
                nowClient[title[i]] = list[i] #bytes外类型暂不处理
        # print(nowClient)
        return nowClient


            

if __name__=="__main__":
    new=ClientDao()
    cs=new.findclientByID(theId="cx001")
    print(cs)
