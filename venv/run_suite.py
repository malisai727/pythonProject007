import os
import time
import unittest
from common.contents import CASE_DIR
from common.contents import REPORT_DIR
from librarys.HTMLTestRunnerNew import HTMLTestRunner


report_name = time.strftime('%Y%m%d%H%M%S',time.localtime())+'report.html'

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASE_DIR))
report_filepath = os.path.join(REPORT_DIR,report_name)
with open(report_filepath,'wb') as f:
    runner = HTMLTestRunner(stream=f,
                            verbosity=2,
                            title='接口测试报告',
                            description='接口的测试报告',
                            tester='malisai')
    runner.run(suite)