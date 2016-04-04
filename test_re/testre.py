import re
import urllib.request


req=urllib.request.urlopen("http://www.imooc.com/course/list")
buf=req.read()
data = buf.decode('utf-8')
listurl = re.findall(r'http:.+\.jpg',data)
i=0
for url in listurl:
    f=open('G:\\1test\\'+str(i)+'.jpg','wb')
    req=urllib.request.urlopen(url)
    buf=req.read()
    f.write(buf)
    i+=1