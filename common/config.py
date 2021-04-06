import os
import configparser
from common.contents import CONF_DIR


class MyConfig():
    def __new__(cls, *args, **kwargs):
        conf = configparser.ConfigParser()
        conf.read(os.path.join(CONF_DIR,'env.ini'),encoding='utf-8')
        switch = conf.get('env','switch')
        if switch == '0':
            conf.read(os.path.join(CONF_DIR,'config0.ini'),encoding='utf-8')
            return conf
        elif switch == '1':
            conf.read(os.path.join(CONF_DIR,'config1.ini'),encoding='utf-8')
            return conf

my_config = MyConfig()