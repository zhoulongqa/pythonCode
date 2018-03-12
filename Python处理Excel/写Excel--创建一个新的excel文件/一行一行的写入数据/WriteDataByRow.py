#encoding=utf-8
'''
除了通过cell(coordinate).value来逐个向excel中添加或者修改值外，我们还可以直接一行一行的append数据
sheet.append(iterable)
该方法用于向excel表中添加一整行数据，参数是一个迭代器类型
'''
import openpyxl
out=openpyxl.Workbook()
sheet2=out.create_sheet(u"员工工资表",index=1)
print u"创建表的表名：",sheet2.title
sheet2.append(('a',1,2,3,u"中国"))
for i in sheet2.rows[0]:
    print i.value
out.save("D:\\python\\gloryroadtest.xlsx")

