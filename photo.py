# -*- coding:utf-8
from PIL import Image
HOME_PATH = 'C:/Users/Sheldon_xia/Desktop/WorkStation/python learning/2'
im = Image.open(HOME_PATH +'myPhoto.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save(HOME_PATH + 'test.jpg','JPEG')
