#-*- coding=utf-8
from requests import Session
from random import random
import subprocess 
import time
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
}
SEARCH_PAGE = 'http://wenshu.court.gov.cn/list/list/'
API_URL = 'http://wenshu.court.gov.cn/List/ListContent'
fromdata = {"Param":"案件类型:刑事案件","Index":"1","Page":"5",
            "Order":"法院层级","Direction":"asc",
            "vl5x":None,
            "number":None,
            "guid":None}

def getvjkl5(session):
    init_data = {'sorttype':'1',"conditions":None}
    session.get(SEARCH_PAGE,params=init_data)
    return session.cookies['vjkl5']


def getNumber(session,guid):
    fromdata_number = {'guid':guid}
    resp = session.post('http://wenshu.court.gov.cn/ValiCode/GetCode',data=fromdata_number)
    return resp.text


def getGuid():
    createGuid = lambda:hex(int((1+random())*65536) | 0)[3::]
    guid = "{}{}-{}-{}{}-{}{}{}".format(createGuid(),createGuid(),createGuid(),createGuid(),\
                                        createGuid(),createGuid(),createGuid(),createGuid())
    return guid


def getkey(code):
    return subprocess.check_output(['node','result.js',code]).decode('utf-8').replace('\n','')


with Session() as s:
    s.headers.update(headers)
    vl5x_code = getvjkl5(s)
    fromdata['vl5x'] = getkey(vl5x_code)
    fromdata['guid'] = getGuid() #getguid()
    fromdata['number']=getNumber(s,fromdata['guid'])
    #翻页功能
    for page in range(1,3):
        fromdata['Index']=page
        resp = s.post(API_URL,fromdata)
        time.sleep(0.5)
        print(resp.text)


