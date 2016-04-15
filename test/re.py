
import urllib2
import re
req=urllib2.urlopen('http://www.imooc.com/course/list')
buf=req.read()
listurl = re.findall(r'http:.+\.jpg',buf)
i=0
for url in listurl:
	f=open('G:\\1test\\'+str(i)+'.jpg','wb')
	req=urllib2,urlopen(url)
	buf = req.read()
	f.write(buf)
	i+=i


 