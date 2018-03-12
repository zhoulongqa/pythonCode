#encoding=utf-8
'''
打开一个只有ip地址的文本文件，读取其中的ip地址或域名，然后进行ping操作，并将ping结果
写入ping.txt文件中，ip.txt文件内容如下
www.baidu.com
www.taobao.com
123.45.5.34
127.0.0.1
'''
import subprocess
import os
class Shell(object):
    def runCmd(self,cmd):
        res=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        #获取子进程的标准输出，标准错误信息
        sout,serr=res.communicate()
        #sout:执行命令后的输出内容，serr出错内容，res.pid为进程编号
        return res.returncode,sout,serr,res.pid

shell=Shell()
fp=open("D:\\python\\ip.txt",'r')
ipList=fp.readlines()
fp.close()
fp=open("D:\\python\\ping.txt",'a')
print ipList
for i in ipList:
    i=i.strip()
    result=shell.runCmd("ping"+i)
    if result[0]==0:
        w=i+':0'
        fp.write(w+'\n')
    else:
        w=i+":1"
        fp.write(w+"\n")
fp.close()
'''
在windows上也可以使用os.system()这个函数来执行一些doc命令，但这个命令只能拿到返回码，
拿不到标准输出，标准错误，所以通常使用的subprocess模块中的Popen类来实现
'''