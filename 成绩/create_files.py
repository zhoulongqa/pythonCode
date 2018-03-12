#encoding=utf-8
fp=open("d:\\xx.py",'w+')
fp.write('0')
fp.seek(2,0)
fp.write('2')
fp.seek(4,0)
fp.write('4')
fp.seek(0,0)