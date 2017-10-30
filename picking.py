# -*- coding:gbk
import pickle
import os
import json


class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

d = dict(name='Bob',age=20,score=88)
curPath = os.path.abspath('.')
newFile = os.path.join(curPath,'picking.txt')

#with open(newFile,'wb') as f:
#    pickle.dump(d,f)


#with open(newFile,'rb') as f :
#    print(pickle.load(f))

with open(newFile,'w') as f:
    json.dump(d,f)

with open(newFile,'r') as f:
    print(json.load(f))


s = Student('Bob',88,22)
print(json.dumps(s,default=student2dict))
#把任意class的实例转变为dict
print(json.dumps(s,default=lambda x: x.__dict__))
    



