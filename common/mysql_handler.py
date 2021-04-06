import pymysql
from common.config import my_config

class MysqlHandler():
    def __init__(self):
        self.con = pymysql.connect(host=my_config.get('sql','host'),
                                   user=my_config.get('sql','user'),
                                   password=my_config.get('sql','password'),
                                   database=my_config.get('sql','database'),
                                   port=my_config.getint('sql','port'),
                                   charset='utf8')
        self.cur = self.con.cursor()
    #查找全部内容
    def fetchall(self,sql):
        self.cur.execute(sql)
        self.con.commit()
        return self.cur.fetchall()
    #查找第一条内容
    def fetchone(self,sql):
        self.cur.execute(sql)
        self.con.commit()
        return self.cur.fetchone()
    #查找指定条内容
    def fetchmany(self,sql,size):
        self.cur.execute(sql)
        self.con.commit()
        return self.cur.fetchmany(size)
    #查找条数
    def count(self,sql):
        count = self.cur.execute(sql)
        self.con.commit()
        return count
    #断开连接
    def close(self):
        self.cur.close()
        self.con.close()


# if __name__ == '__main__':
    # mysql_handler = MysqlHandler()
    # a = mysql_handler.fetchall("select reg_name from member where mobile_phone='15690403234'")
    # b = mysql_handler.count('SELECT MAX(id) FROM loan ')
    # print(type(b))