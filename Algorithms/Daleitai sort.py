#-*- coding:utf-8
'''
	打擂台排序
'''

def insertion_sort(items):

	if len(items) == 1:
		return items

	length = len(items)
	for index in range(length):
		for sub_index in range(index,length):
			if items[index]>items[sub_index]:
				items[index],items[sub_index] = items[sub_index],items[index]  
				
	return items

items = [3,4,5,0,1,2,6,7,8,10,9]
print(insertion_sort(items))