# -*- coding:gbk
from io import StringIO

HOME_PATH = 'C:/Desktop/WorkStation/程序相关/SRC/'
TEMP_PATH = 'C:/Desktop/WorkStation/python learning/'
"""
with open(TEMP_PATH + 'test.jpg','rb') as f:
    print(f.read())
"""
def get_Input_Data(outfile):
    with open(HOME_PATH + 'M0XXXBAT.CBL','r',
              encoding='gbk',errors='ignore') as f:
         for line in f.readlines():
             outfile.write(line)

    
with open(TEMP_PATH + 'hello.txt','w') as f:
    f.write('head text')
#    get_Input_Data(f)
print('File writting end')
fio = StringIO()
fio.write('hello')
fio.write(' ')
fio.write('world!')

print(fio.getvalue())

"""
f = open(HOME_PATH + 'M0181BAT.CBL','r',encoding='gbk')
for line in f.readlines():
    print(line.strip())
f.close()

try:
    f = open(HOME_PATH + 'M0XXXBAT.cbl','r',encoding='gbk',
             errors='ignore')
    print(f.read())
finally:
    if f:
        f.close()


    print(f.read())


"""
    
