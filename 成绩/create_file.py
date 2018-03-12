#encoding=utf-8
import os
def create_file(dir_name):
    for root,dirs,files in os.walk(dir_name):
        file_name=os.path.join(root,"wulaoshi.txt")
        with open(file_name,'w') as fp:
            fp.write("wulaoshi\n")
            print u"创建文件%s成功"%file_name
create_file("d:\\")
