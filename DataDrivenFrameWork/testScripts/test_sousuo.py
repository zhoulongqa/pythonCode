#encoding=utf-8
from util.log import *
from util.ParseExcel import *
from selenium import webdriver
from config.VarConfig import *
import time

test_data_file_path=parentDirPath+u"\\testData\\测试数据.xlsx"
pe=ParseExcel()
pe.loadWorkBook(test_data_file_path)
sheet=pe.getSheetByIndex(0)
def get_test_data():
    global test_data_file_path
    global sheet

    visit_urls=[]
    assert_keys=[]
    max_row=pe.getRowsNumber(sheet)
    print max_row
    for i in range(2,max_row+1):
        row=pe.getRow(sheet,i)
        print row[0].value
        visit_urls.append(row[0].value)
    for i in range(2,max_row+1):
        row=pe.getRow(sheet,i)
        print row[1].value
        assert_keys.append(row[1].value)
    return visit_urls.assert_keys
print get_test_data()


info(u"开始测试")
driver=webdriver.Firefox(executable_path="c:\\geckodriver")
urls=get_test_data()[0]
assert_words=get_test_data()[1]
try:
    for i in range(len(urls)):
        info(u"访问网站")
        driver.get(urls[i])
        time.sleep(2)
        info(u"断言是否有关键词")
        assert assert_words[1] in driver.page_source
        pe.writeCellCurrentTime(sheet,None,i+2,3)
        pe.writeCell(sheet,u"成功",None,i+2,4)
except Exception,e:
    print e.message
    pe.writeCellCurrentTime(sheet,None,i+2,4)
    pe.writeCell(sheet,u"失败",None,i+2,4)