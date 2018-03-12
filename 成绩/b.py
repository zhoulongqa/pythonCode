#encoding=utf-8
import sys
command_string=''.join(sys.argv[1:])
if "--" not in command_string:
    print u"命令行参数没有包含--xx类型参数，请重新输入"
    sys.exit(1)
for s in sys.argv[1:]:
    if s[2:]=='help':
        print u"此程序为光荣之路出品"
    if s[2:]=="version":
        print "version:1.0"
