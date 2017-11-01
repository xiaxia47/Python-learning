#-*- coding:utf-8
'''
	冒泡排序（英语：Bubble Sort，台湾另外一种译名为：泡沫排序）是一种简单的排序算法。
	算法核心：重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
	          走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
	          这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
	时间复杂度：O(n**2)

'''
def bubble(items):
	if len(items) <= 1:
		return items
	for index in range(len(items)-1,0,-1):
		for sub_index in range(index):
			if items[sub_index] > items[sub_index + 1]:
				items[sub_index],items[sub_index + 1] = items[sub_index + 1], items[sub_index] 
	return items

items = [27, 31, 28, 4, 2, 2, 0, 35, 8, 14,12,33,0]
print('final:', bubble(items))
