import os

#项目路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#用例数据路径
DATA_DIR = os.path.join(BASE_DIR,'data')

#日志路径
LOG_DIR = os.path.join(BASE_DIR,'logs')

#配置文件路径
CONF_DIR = os.path.join(BASE_DIR,'conf')

#测试报告路径
REPORT_DIR = os.path.join(BASE_DIR,'reports')

#测试用例路径
CASE_DIR = os.path.join(BASE_DIR,'testcases')