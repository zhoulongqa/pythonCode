#encoding=utf-8
import requests
import json
def register():
    url=r"http://103.36.173.17:8080/register"
    headers={"Content-type":"application/json"}
    for i in xrange(1,200):
        name="wang"+str(i+10000)
        params={"username":name,"password":name,"email":name+"@qq.com"}
        req=requests.post(url,data=json.dumps(params),headers=headers)
        print req.text
        res_data=json.loads(req.text)
        username=res_data.get('user')
        assert name==username,"not match."
register()