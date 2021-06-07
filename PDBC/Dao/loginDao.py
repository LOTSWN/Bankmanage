import connectionPool

class loginDao:
    def __init__(self):
        self.ac=connectionPool.get_my_connection()
        (self.cur, self.con) = self.ac.getconn()

    def findclientByID(self,theId):
        # theId="osn"
        sql="SELECT * FROM `client` WHERE `cardID` LIKE "+"'"+theId+"'"
        print(sql)
        self.cur.execute(sql)
        list=self.cur.fetchall()
        return list
        # for i in list:
        #     print(i)

if __name__=="__main__":
    new=loginDao()
    ls=new.findclientByID(theId="cx001")
    for i in ls:
        print(i)
