# -*- coding=utf-8
import requests
from requests_toolbelt  import MultipartEncoder

MY_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Host':'sydwjg.sdbb.gov.cn',
    'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundary7sOKIfzWoqt273WF',
    'Content-Length':'907',
    'Referer':'http://sydwjg.sdbb.gov.cn/website/seeNdbggkAction!selNdbggk.action',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
my_payload = {'xydm':'',
              'certificate':'',
              'unit_name':'',
              'jbdw':'',
              'province':'',
              'city':'',
              'coun':'',
              'year':'2016',
              'confirm_before_do':'查询'}

m = MultipartEncoder(my_payload)
MY_HEADERS['Content-Type'] = m.content_type
url ='http://sydwjg.sdbb.gov.cn/website/seeNdbggkAction!seeNdbggkListBySel.action?certificate=&coun=&province=37&xydm=&year=2016&unit_name=&confirm_before_do=%E6%9F%A5+++%E8%AF%A2&jbdw=&city=&cpage=1'
url_origin = 'http://sydwjg.sdbb.gov.cn/website/seeNdbggkAction!seeNdbggkListBySel.action'
resp = requests.post(url_origin, headers=MY_HEADERS, data=m, timeout=10)
print(resp.status_code)
with open('mypage.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)

