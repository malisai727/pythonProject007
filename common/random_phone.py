import random
from common.mysql_handler import MysqlHandler

mysqlhandler = MysqlHandler()

def random_phone():
    while 1:
        phone = '1'+random.choice(['3','5','8'])
        for i in range(9):
            phone += str(random.randint(0,9))
        sql = f"SELECT * FROM member WHERE mobile_phone = {phone}"
        if mysqlhandler.count(sql) == 0:
            return phone

if __name__ == '__main__':
    print(type(random_phone()))

# print(random.randint(0,9))