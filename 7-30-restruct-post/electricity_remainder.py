import time
import os
from electricity_email import e_email
from check_the_electricity import check

while( os.system('ping www.baidu.com')==1):   #当状态为未联网状态时
    print('沉睡60秒')
    time.sleep(30)

#获取电量
value=check('东区', '沁苑9舍', '531')
print(value)
if float(value) < 30:
    e_email('daiyang_liu@163.com','该交电费了' , '剩余电量：'+str(value)+'，大哥您的电费不够了，赶紧交吧')