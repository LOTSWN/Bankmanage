from Dao.connectionPool import connectionPool


class StaffDao(object):
    def __init__(self):
        self.ac = connectionPool()
        (self.cur, self.con) = self.ac.getconn()  # con：连接；cur：连接的对象

    def findstaffByID(self, theId):  # 根据ID查找单个客户

        sql = "SELECT * FROM `staff` WHERE `staffID` LIKE " + "'" + theId + "'"
        try:
            self.cur.execute(sql)
            list = self.cur.fetchall()
            nowStaff = self.__lisTodic(list[0])
            return nowStaff
        except:
            return None

    def __lisTodic(self, list):  # 列表转字典
        title = []
        title = ["staffID", "staffname", "workbank", "password", "age", "gender", "level"]
        nowStaff = {}
        for i in range(len(list)):
            if str(list[i].__class__) == '<class \'bytes\'>':
                nowStaff[title[i]] = str(list[i], encoding="utf-8")
            else:
                nowStaff[title[i]] = list[i]  # bytes外类型暂不处理
        # print(nowClient)
        return nowStaff


if __name__ == "__main__":
    new = StaffDao()
    cs = new.findstaffByID(theId="admin001")
    print(cs)
