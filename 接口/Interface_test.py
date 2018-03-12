#encoding=utf-8
import requests
import json
import random
def register(name):
    url=r'http://103.36.173.17:8080/register/'
    headers={"Content-type":"application/json"}
    params={"username":name,"password":"12345678","email":"Lily@qq.com"}
    req=requests.post(url,data=json.dumps(params),headers=headers)
    print req.status_code
    print req.text
    print type(req.text)
    print type(json.loads(req.text))    #转换为字典
    print json.loads(req.text)['username']
    try:
        assert json.loads(req.text)['username']==name
        assert json.loads(req.text)['code']=='00'
        with open("e:\\successResult.txt",'a+') as sr:
            sr.write("request:%s\n response result:%s\n" % (json.dumps(params),req.text))
            sr.write("-"*50)
    except:
        with open("e:\\failResult.txt",'a+') as fr:
            fr.write("request:%s\n response result:%s\n" % (json.dumps(params),req.text))
            fr.write("-"*50)
if __name__=="__main__":
    name="wangzeliang"+str(random.randint(1000,10000))
    print name
    register(name)