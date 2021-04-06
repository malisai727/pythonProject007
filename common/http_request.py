import requests

class HttpRequest1():
    def request(self,method, url,
                params=None, data=None,
                headers=None, cookies=None, json=None):
        method = method.lower()
        if method == 'post':
            if json:
                return requests.post(url=url,json=json,cookies=cookies,headers=headers)
            else:
                return requests.post(url=url,data=data,cookies=cookies,headers=headers)
        elif method =='get':
            return requests.get(url=url,params=params,cookies=cookies,headers=headers)

class HttpRequest2():
    def __init__(self):
        self.session = requests.sessions.Session()
    def request(self,method, url,
                params=None, data=None,
                headers=None, cookies=None, json=None):
        method = method.lower()
        if method == 'post':
            if json:
                return self.session.post(url=url,json=json,cookies=cookies,headers=headers)
            else:
                return self.session.post(url=url,data=data,cookies=cookies,headers=headers)
        elif method == 'get':
            return self.session.get(url=url,params=params,cookies=cookies,headers=headers)
    def close(self):
        self.session.close()