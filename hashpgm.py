# -*- coding:gbk

import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

def calc_md5(password):
    print(md5.update(password.encode('utf-8')))
    print(md5.hexdigest())

#password = input('write your password:')

#calc_md5(password)

db = {}
def register(username,password):
    db[username] = get_md5(password+username+'add some salt')
def get_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

def login(username,password):
    if username not in db:
        register(username,password)
        print('welcome',username,'you are handsome!')
        print('Sorry, I lied')
    elif db[username] == get_md5(password + username + 'add some salt'):
        print('Welcome ~~~:',username)
    else:
        print('invalid login details')


while input('please login(y,n):') == 'y':
    username=input('Username: ')
    password=input('Password: ')
    login(username,password)

