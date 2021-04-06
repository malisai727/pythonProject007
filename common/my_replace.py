import re
from common.config import my_config

class ConText():
    loan_id = None
    token = None


def my_replace(data):
    p = "#(.+?)#"
    while re.search(p,data):
        res = re.search(p,data).group(1)
        try:
            repl = my_config.get('user',res)
        except:
            repl = getattr(ConText,res)
        data = re.sub(p,repl,data,count=1)
    return data

def my_replace2(data):
    p = re.compile(r"#(.+?)#")
    while p.findall(data):
        res = p.findall(data)[0]
        try:
            repl = my_config.get('user',res)
        except:
            repl = getattr(ConText,res)
        data = p.sub(repl,data,count=1)
    return data