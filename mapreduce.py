# -*- coding=gbk -*-
from functools import reduce
INTS= {'1':1,'2':2,
       '3':3,'4':4,
       '5':5,'6':6,
       '7':7,'8':8,
       '9':9,'0':0}
def str2float(s):
          if '.' in s:
                    i = s.index('.')
                    return reduce(lambda x,y: x * 10 + y ,
                                  map(str2int,s[:i] + s[i+1:]))/(10**(len(s)-1 - i))
          else:
                    return reduce(lambda x,y: x * 10 + y ,
                        map(str2int,s))
def str2int(num1):
          return  INTS[num1]

s = input()
print(str2float(s),isdigit(str2float(s)))
