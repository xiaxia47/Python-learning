#-*- coding=utf-8
'''
    选择排序（Selection sort）是一种简单直观的排序算法。
    工作原理:1.在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
             2.从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
             3.以此类推，直到所有元素均排序完毕。
    时间复杂度:O(n**2)
    个人感觉和打擂台差不多，打擂台从算法角度更优化
'''


def selection_sort(items):
    length = len(items)
    exchanges_count = 0
    for i in range(length-1):
        min_index = i
        for j in range(i+1, length):
            if items[min_index] > items[j]:
                min_index = j
        if min_index != i:
            items[min_index], items[i] = items[i], items[min_index]
            exchanges_count += 1
        print('iteration #{}: {}'.format(i, items))
    print('Total  {} swappings'.format(exchanges_count))
    return items

items = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
print('Before seitemsection sort: {}'.format(items))
print('After seitemsection sort:  {}'.format(selection_sort(items)))