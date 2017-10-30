# -*- coding:gbk
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id = Column(String(20),primary_key = True)
    name = Column(String(20))

engine = create_engine('mysql+pymysql://student:python@45.32.62.10:3306/test')
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id = '6',name = 'Bob')
session.add(new_user)
session.commit()
session.close()
