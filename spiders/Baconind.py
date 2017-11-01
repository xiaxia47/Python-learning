from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pymysql


def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url= %s",(url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages(url) VALUES(%s)",(url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId= %s AND toPageId = %s",
                (int(fromPageId),int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links(fromPageId, toPageId) VALUES(%s, %s)",
                    (int(fromPageId), int(toPageId)))
        conn.commit()


def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return;
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            #遇到一个新页面，加入集合并搜索里面的词条链接
            newPage = link.attrs['href']
            pages.add(newPage)
            getLinks(newPage,recursionLevel+1)

pages = set()
try:
    conn = pymysql.connect(host='',port=3306,unix_socket='/var/run/mysqld/mysqld.sock',
                           user='pythonuser',password='',
                           db='wikipedia',charset='utf8')
    cur = conn.cursor()
    cur.execute("USE wikipedia")
    getLinks("/wiki/Kevin_Bacon",0)
finally:
    cur.close()
    conn.close()
        
