#!coding=utf8
import requests




headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:60.0) Gecko/20100101 Firefox/60.0',
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                    'Accept-Encoding':'gzip, deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Content-Length': '13',
                    'Connection': 'close',
                    'Upgrade-Insecure-Requests': '1'
}



class conn():
    rq = requests.session()
    URL = ''
    proxies={}

    def check(self,data):

       if self.rq.post(self.URL,data=data,headers=headers,proxies=self.proxies).headers['Content-Length']=='0':

           return 0
       else:
           return 1


    def send(self,data):
        res=self.rq.post(self.URL,data=data,headers=headers,proxies=self.proxies).text

        return res



