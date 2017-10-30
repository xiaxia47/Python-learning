# -*- coding:gbk
import sqlite3,os

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id = ?',('1',))
value = cursor.fetchall()
print(str(value))

'''
cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user(id,name) values(\'1\',\'Michael\')')
print(cursor.rowcount)
conn.commit()
'''
cursor.close()
conn.close()

db_file = os.path.join(os.path.dirname(__file__),'test.db')
print(db_file)
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key,name varchar(20),'+
               'score int)')
cursor.execute(r"insert into user values('A-001','Adam',95)")
cursor.execute(r"insert into user values('A-002','Bart',62)")
cursor.execute(r"insert into user values('A-003','Lisa',78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low,high):
    inx = []
    conn = sqlite3.connect(db_file)
    cursor= conn.cursor()
    cursor.execute('select name from user where score between ? and ? ' +
                   'order by score ',(low,high))
    value =  cursor.fetchall()
    print(value)
    for row in value:
        print(row[0])
        inx.append(row[0])
    return inx


assert get_score_in(80,95) == ['Adam']
assert get_score_in(60,80) == ['Bart','Lisa']
assert get_score_in(60,100) == ['Bart','Lisa','Adam']
