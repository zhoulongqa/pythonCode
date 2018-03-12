#encoding=utf-8
class Computer(object):
    serialNo=[]     #类变量
    def __init__(self,name,cpu,mem,harddisk):
        self.serialNo.append(name)
        self.cpu=cpu
        self.mem=mem
        self.harddisk=harddisk
    def get_computer_info(self):
        print Computer.serialNo
        return "cpu:"+self.cpu+"\n"+"mem:"+self.mem+"\n"+"harddisk:"+self.harddisk
c=Computer("speed1","i7","8G","1T")
print c.get_computer_info()   #[speed1]  'cpu:i7...'
d=Computer("speed2","i5","16G","2T")
print d.get_computer_info()
