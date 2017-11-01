from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr,retstr,laparams=laparams)
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    print(retstr)
    content = retstr.getvalue()
    retstr.close()
    return content

#filepath='C:/Users/Sheldon_xia/Desktop/Python网络数据采集.pdf'
pdfFile =urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")

outStr = readPDF(pdfFile)
print(outStr)

n=1
outputString = StringIO(outStr)
for line in outputString.readlines():
    print(line.strip('\n'))
    n+=1
    if n > 10:
        break
pdfFile.close()

#with open(filepath,mode='rb') as f:
#    outStr=readPDF(f)
#    print(outStr)
