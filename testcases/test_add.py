import os
import time
import unittest
from librarys.ddt import ddt,data
from common.excel_handler import ExcelHandler
from common.http_request import HttpRequest2
from common.mysql_handler import MysqlHandler
from common.contents import DATA_DIR
from common.config import my_config
from common.my_replace import my_replace,ConText
from common.encryption import rsaEncrypt
from common.logger import my_logger


@ddt
class test_add(unittest.TestCase):
    #准备测试数据
    workbook = ExcelHandler(os.path.join(DATA_DIR,my_config.get('excel','filename')),'add')
    cases = workbook.read_row_obj()

    #初始化测试环境
    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()
        cls.mysql_handler = MysqlHandler()

    #执行测试用例
    @data(*cases)
    def test_add(self,case):
        #预期结果
        expect = case.expect
        #准备参数数据
        url = my_config.get('env','url')+case.url
        header = my_replace(case.header)
        data = my_replace(case.data)
        if '*member_id*' in data:
            member_id = self.mysql_handler.fetchone("SELECT id FROM member ORDER BY id DESC LIMIT 1")[0] + 1
            data = data.replace('*member_id*',str(member_id))
        if '*timestamp*' in data:
            timestamp = int(time.time())
            data = data.replace('*timestamp*',str(timestamp))
        if '*sign*' in data:
            sign = rsaEncrypt(ConText.token)
            data = data.replace('*sign*',sign)
        #发起请求前查询标的个数
        if case.check_sql:
            sql = my_replace(case.check_sql)
            loan_count_before = self.mysql_handler.count(sql)
        response = self.http_request.request(method=case.method,url=url,headers=eval(header),json=eval(data))
        actual = response.json()
        if case.interface == '登录':
            setattr(ConText,'token',actual['data']['token_info']['token'])
        #断言
        try:
            self.assertEqual(expect,actual['code'])
            if case.check_sql:
                sql = my_replace(case.check_sql)
                loan_count_after = self.mysql_handler.count(sql)
                self.assertEqual(loan_count_before+1,loan_count_after)
        except AssertionError as e:
            result = '测试未通过'
            my_logger.info(f"第{case.case_id}条用例测试未通过，预期结果为{expect}，实际结果为{actual}")
            raise e
        else:
            result = '测试通过'
            my_logger.info(f"第{case.case_id}条用例测试通过，预期结果为{case.expect}实际结果为{actual}")
        finally:
            self.workbook.write(row=case.case_id + 1,column=10,value=str(actual))
            self.workbook.write(row=case.case_id + 1, column=11, value=result)

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql_handler.close()