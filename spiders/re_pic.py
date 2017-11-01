from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")
#处理子标签和其他后代标签
#for child in bsObj.find("table",{"id":"giftList"}).children:
#    print(child)

#for child in bsObj.find("table",{"id":"giftList"}).descendants:
#   print(child)

#处理兄弟标签
#for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#    print(sibling)
images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img*")})
for image in images:
    print(image["src"])


