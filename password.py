import os
import time
import zipfile
from multiprocessing.dummy import Pool

stars_time = time.time()
f = zipfile.ZipFile('1.zip')
num = 0


def password_pg(c) :
    try :
        f.extractall(pwd=bytes(str(c), 'utf8'))
        print('压缩包密码为：', str(c))
        print('耗时：', time.time() - stars_time)
        pool.close()
        pool.join()
        input()
    except :
        pass
        global num
        num = num + 1
        print('正在尝试第：', str(num), '次')



mm = []
for i in range(1000000) :
    mm.append(i)
pool = Pool(20)
pool.map(password_pg, mm)
pool.close()
pool.join()
