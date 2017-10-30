# -*- coding:gbk
import logging
import pdb
logging.basicConfig(level=logging.INFO)

def foo():
    r = some_function()
    if r== (-1):
        return (-1)
    return r

def bar():
    r = foo();
    if r == -1:
        print('error')
    else:
        pass

def some_function():
    pass

s = '0'
n = int(s)
pdb.set_trace()
#logging.info('n = %d' % n)
print(10/n)

"""
try:
    print('try...')
    r = 19/0
    print('result...',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')
"""
