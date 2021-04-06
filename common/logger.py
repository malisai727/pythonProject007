import os
import logging
from common.contents import LOG_DIR

class MyLogger():

    def __new__(cls, *args, **kwargs):
        #创建日志收集器
        mylogger = logging.getLogger('mylogger')
        mylogger.setLevel('INFO')
        #创建日志输出渠道（到控制台）
        l_s = logging.StreamHandler()
        l_s.setLevel('INFO')
        #创建日志输出渠道（到文件）
        l_f = logging.FileHandler(os.path.join(LOG_DIR,'logger.txt'),encoding='utf8')
        l_f.setLevel('INFO')
        #给收集器添加输出渠道
        mylogger.addHandler(l_s)
        mylogger.addHandler(l_f)
        #设置日志输出格式
        ft = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        my_format = logging.Formatter(ft)
        #给输出渠道设置格式
        l_s.setFormatter(my_format)
        l_f.setFormatter(my_format)
        return mylogger
my_logger = MyLogger()

if __name__ == '__main__':
    mylogger = MyLogger()
    mylogger.debug('输出debug等级的日志')
    mylogger.info('输出info等级的日志')
    mylogger.warning('输出warning等级的日志')
    mylogger.error('输出error等级的日志')