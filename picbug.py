from lxml import etree
from selenium import webdriver
import time
from requests import Session
import json
import re
import urllib
import os
url='http://i.sporttery.cn/api/fb_match_info/get_team_cup/?'
api='http://i.sporttery.cn/api/fb_match_info/get_team_data/?f_callback=footb_info&tid=886'
data={'f_callback':'footb_info','tid':886,'_':None}

s = Session()
s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
				  'Referer':url})
filedir = './picture/'
#driver = webdriver.Chrome(executable_path='D:/Python Learning/tools/chromedriver')

html = s.get(api).content.decode('gbk')
jd = html.split('(')[1].split(')')[0]
js = json.loads(jd)['result']

print('start print data')
print(js['team_pic'],js['club_name'])
if not os.path.exists(filedir):
	print(filedir,' does not exit!Creating in process')
	os.mkdir(filedir)
print(filedir)
urllib.request.urlretrieve(js['team_pic'],filename=(filedir+js['club_name']+'.'+js['team_pic'].split('.')[-1]))




#r=driver.find_element_by_xpath("//div[@class='m-left-logo']/img").get_attribute('src')
#print(r)
#driver.quit()