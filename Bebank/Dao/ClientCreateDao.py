from Dao.connectionPool import connectionPool
from Dao.ClientDao import ClientDao


class ClientCreateDao(object):

    def __init__(self):
        self.ac = connectionPool()
        (self.cur, self.con) = self.ac.getconn()  # con：连接；cur：连接的对象

    def insertNewClient(self, clientID, password, gender, name, openTime, openBank, telephone, age ):  # 插入新用户
        cd = ClientDao()
        diccd = cd.findclientByID(theId=clientID)

        if diccd == None:
            sql = "INSERT INTO `client` (`clientID`, `password`, `gender`, `name`, `openTime`, `openBank`, `telephone`, `age`) VALUES (" + "'"+clientID+"'" + "," + "'"+password+"'" + "," + "'"+gender+"'" + "," + "'"+name+"'" + "," + "'"+openTime+"'" + "," + "'"+openBank+"'" + "," + "'"+telephone+"'" + "," + "'"+age+"'" + ")"
            try:
                self.cur.execute(sql)
                return 1
            except:
                return None
        else:
            return "duplicateID"



if __name__ == "__main__":
    new = ClientDao()
    cs = new.findclientByID(theId="cx001")
    print(cs)