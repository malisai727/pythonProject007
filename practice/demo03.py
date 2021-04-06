import json
from demo02 import httprequest


# url = 'http://api.lemonban.com/futureloan/member/register'
# data = {"mobile_phone":"13331135579","pwd":"123456789","type":"","reg_name":""}
# data2 = {"mobile_phone":"*register_phone*","pwd":"123456789","type":"","reg_name":""}
# header = {"X-Lemonban-Media-Type":"lemonban.v3","Content-Type":"application/json"}
# response = httprequest.request(method='post',url=url,json=data,headers=header)
# print(response.json())


url = 'http://api.lemonban.com/futureloan/member/login'
data = {"mobile_phone":"13331135579","pwd":"123456789"}
header = {"X-Lemonban-Media-Type":"lemonban.v3","Content-Type":"application/json"}
response = httprequest.request(method='post',url=url,json=data,headers=header)
print(response.json())


{'code': 0,
 'msg': 'OK',
 'data': {'id': 1000080689,
          'leave_amount': 0.0,
          'mobile_phone': '13331135579',
          'reg_name': 'malisai',
          'reg_time': '2021-02-24 11:20:06.0',
          'type': 0,
          'token_info': {'token_type': 'Bearer',
                         'expires_in': '2021-03-02 16:39:17',
                         'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwMDAwODA2ODksImV4cCI6MTYxNDY3NDM1N30.GnGgZpseJY8jr7basZDlIN8w7XQ2Tch8tapwMekHrYwAdcSuMPfLlJAgLunlOr9PRXz2azx4iOBLMnNdXXtaZQ'}},
 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}