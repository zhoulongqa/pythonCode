#encoding=utf-8
import sys
import string
letter_num=0
for arg in sys.argv[1:]:
    for s in arg:
        if s in string.letters:
            letter_num+=1
print u"命令行参数包含的字母个数为：",letter_num

