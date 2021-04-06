import os
import unittest
from common.contents import DATA_DIR
from librarys.ddt import ddt,data
from common.excel_handler import ExcelHandler
from common.config import my_config
from common.http_request import HttpRequest2
from common.mysql_handler import MysqlHandler
from common.random_phone import random_phone
from common.logger import my_logger


@ddt
class TestRegister(unittest.TestCase):
    #准备测试数据
    workbook = ExcelHandler(os.path.join(DATA_DIR,my_config.get('excel','filename')),'register')
    cases = workbook.read_row_obj()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()
        cls.mysql_handler = MysqlHandler()

    @data(*cases)
    def test_register(self,case):
        #获取预期结果
        expect = int(case.expect)
        #准备接口地址
        url = my_config.get('env','url') + case.url
        #准备请求参数数据
        if '*register_phone*' in case.data:
            register_phone = random_phone()
            data = case.data.replace('*register_phone*',register_phone)
        elif '*phone*' in case.data:
            sql = "SELECT mobile_phone FROM member LIMIT 1"
            data = case.data.replace('*phone*',self.mysql_handler.fetchone(sql)[0])
        else:
            data = case.data
        #发起请求获取响应结果
        response = self.http_request.request(method=case.method,url=url,headers=eval(case.header),json=eval(data),)
        actual = response.json()
        my_logger.info(f'请求响应结果为{actual}')
        #断言判断结果是否正确
        try:
            self.assertEqual(expect,actual['code'])
            if case.check_sql:
                if '*register_phone*':
                    sql = case.check_sql.replace('*register_phone*',register_phone)
                    count = self.mysql_handler.count(sql)
                    self.assertEqual(1,count)
        except AssertionError as e:
            result = '测试未通过'
            # my_logger.info(f'测试没有通过,预期结果为{}，实际结果为{}')
            raise e
        else:
            result = '测试通过'
            # my_logger.info('测试通过')
        finally:
            self.workbook.write(row=case.case_id+1,column=10,value=str(actual))
            self.workbook.write(row=case.case_id+1,column=11,value=result)
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql_handler.close()