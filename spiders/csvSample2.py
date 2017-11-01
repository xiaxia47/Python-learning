import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html,"html.parser")
#主对比表格是当前页面上的第一个表格
table = bsObj.findAll("table",{"class":"wikitable"})[0]
rows = table.findAll("tr")

csvFile = "../files/editors.csv"
csvFilePath = os.path.dirname(csvFile)
if os.path.exists(csvFilePath) != True:
    os.mkdir(csvFilePath)
    print('folder created: ' + scvFilePath)
with open(csvFile,'wt',newline="",encoding='utf-8') as csvf:
    writer = csv.writer(csvf) 
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
           csvRow.append(cell.get_text())
        writer.writerow(csvRow)
            
