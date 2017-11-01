#/usr/bin/env python
#-*- coding=utf-8

def sequential_search(lis key):
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return 1
        else:
            return False

if __name__ == '__main__':
   mylist = [1,5,8,123,22,54,7,99,300,222]
   result = sequential_search(mylist, 123)
   print(result)

