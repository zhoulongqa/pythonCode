#encoding=utf-8
import multiprocessing
def m1(x):
    return x*x
if __name__=="__main__":
    pool=multiprocessing.Pool(multiprocessing.cpu_count())
    i_list=range(8)
    print pool.map(m1,i_list)