#encoding=utf-8
import os
#获取当前文件所在目录的父目录的绝对路径
parentDirPath=os.path.driname(os.path.dirname(os.path.abspath(__file__)))
print "parentDirPath",parentDirPath

#获取存放页面元素定位表达式文件的绝对路径
pageElementLocatorPath=parentDirPath+u"\\config\\PageElementLocator.ini"
print "pageElementLocatorPath:",pageElementLocatorPath

#获取数据文件存放绝对路径
dataFilePath=parentDirPath+u"\\testData\\126邮箱联系人.xlsx"

#126账号工作表中，每列对应的数字序号
account_username=2
account_password=3
account_dataBook=4
account_isExecute=5
account_testResult=6

#联系人工作表中，每列对应的数字序号
contacts_contactPersonName=2
contacts_contactPersonEmail=3
contacts_isStar=4
contacts_contactPersonMobile=5
contacts_contactPersonComment=6
