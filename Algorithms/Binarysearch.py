#-*- coding=utf-8

#二分查找(Binary Search)
#时间复杂度:O(log(n))
#算法核心：在查找表中不断取中间元素与查找值进行比较，以二分之一的倍率进行表范围的缩小。
def binary_search(item_list,key):
	low = 0
	high = len(item_list) - 1
	time = 0
	while low <= high:
		time += 1
		mid = int((low + high) /2)
		if key < item_list[mid]:
			high = mid - 1
		elif key > item_list[mid]:
			low = mid + 1
		else:
			#打印循环次数
			print("times: {}".format(time))
			#目标值所在位置
			return mid
	print("times: {}".format(time))
	print("{key} not found in list".format(key = key))
	return None

if __name__ == '__main__':
	item_list = [1,4,7,8,22,53,99,123]
	result = binary_search(item_list, 53)
	print("Index in the list is {pos}".format(pos=result))


