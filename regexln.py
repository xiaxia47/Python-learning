# -*- coding:gbk
import re


test = input('please enter your phone number with region code:')
if re.match(r'^\d{3}\-\d{3,8}$',test):
    print('%s is a correct answer' % test)
else:
    print('%s is a wrong number' % test)

print('Numbers your entered are %s ' % (re.split(r'\s+',test).groups()))

validator = re.compile(r'(.*\s+)([0-9a-zA-Z\_]*@[a-zA-Z1-9\.]*\.[a-z]{3}$)')

while re.match(r'[y|Y]',input('please confirm if you wanna continue:(y/n)')):
    if validator.match(input('Please enter your email address:')):
        print('valid address')
    else:
        print('Invalid address')

print('Exit!!!!')







