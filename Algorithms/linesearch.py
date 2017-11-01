#/usr/bin/env python
#-*- coding=utf-8

#也就是数据不排序的线性查找，遍历数据元素。
#算法分析：最好情况是在第一个位置就找到了，此为O(1)；最坏情况在最后一个位置才找到，此为O(n)；所以平均查找次数为(n+1)/2。
#时间复杂度为:O(n)


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

