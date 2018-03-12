#encoding=utf-8
from openpyxl import load_workbook
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

workbook=load_workbook(r"D:\\python\\test.xlsx")
print workbook
#获取excel中所有工作表的名字
bookNameList=workbook.get_sheet_names()
#通过表名获取指定的工作表
sheet1=workbook.get_sheet_by_name(u"员工信息表")

area_sheet=sheet1['A1':'C4']    #获取一个区域
for i in area_sheet:
    print i
    print i[0].value