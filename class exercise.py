from types import MethodType

def set_city(self, city):
          self.city = city


class Student(object):
          __slots__ = ('name','age')
          pass

Student.set_city = MethodType(set_city,Student)
print(dir(Student))
a = Student()
a.set_city('Beijing')
print(a.city)
print(dir(a))
