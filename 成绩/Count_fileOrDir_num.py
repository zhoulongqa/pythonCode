#encoding=utf-8
import os
dir_path="d:\\"
file_num=0
dir_num=0
for item in os.listdir(dir_path):
    print os.path.join(dir_path,item)
    item=os.path.join(dir_path,item)
    if os.path.isfile(item):
        file_num+=1
    elif os.path.isdir(item):
        dir_num+=1

print u"目录的个数是：",dir_num
print u"文件的个数是：",file_num
