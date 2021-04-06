import os
import unittest
from common.contents import DATA_DIR
from librarys.ddt import ddt,data
from common.excel_handler import ExcelHandler
from common.http_request import HttpRequest2
from common.mysql_handler import MysqlHandler
from common.config import my_config
from common.my_replace import my_replace
from common.random_phone import random_phone
from common.logger import my_logger


@ddt
class TestLogin(unittest.TestCase):
    #准备测试数据
    workbook = ExcelHandler(os.path.join(DATA_DIR,my_config.get('excel','filename')),'login')
    cases = workbook.read_row_obj()
    #初始化测试环境
    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()
        cls.mysql_handler = MysqlHandler()
    #执行测试用例
    @data(*cases)
    def test_login(self,case):
        #预期结果
        expect = case.expect
        #实际结果
        url = my_config.get('env','url')+case.url
        if '#login_phone#' in case.data:
            data = my_replace(case.data)
        elif '*phone*' in case.data:
            data = case.data.replace('*phone*',random_phone())
        else:
            data = case.data
        response = self.http_request.request(method=case.method,url=url,headers=eval(case.header),json=eval(data))
        actual = response.json()
        #断言
        try:
            self.assertEqual(expect,actual['code'])
        except AssertionError as e:
            result = '测试未通过'
            my_logger.info(f"测试未通过预期结果为{expect}，实际结果为{actual}")
            raise e
        else:
            result = '测试通过'
            my_logger.info(f'测试通过，预期结果为{expect}，实际结果为{actual}')
        finally:
            self.workbook.write(row=case.case_id+1,column=10,value=str(actual))
            self.workbook.write(row=case.case_id + 1, column=11, value=result)
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql_handler.close()