# -*- coding=gbk
class Student(object):
    sname = 'Sheldon'
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name,self.__score))


bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.age = 0
print(bart.age)

bart.__init__('Sheldon',97)

print(bart.sname)
Student.sname = 'Alpha'
print(bart.sname)
print(lisa.sname)
