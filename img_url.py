import re
import urllib
u=input("Enter the url of the website")
a=urllib.urlopen(u)
pattern=re.compile("<img\s+[^>]*?src=("|')([^"]+)\1")
b=re.findall(pattern,a.read())
f=open("img_url.txt","w")
for i in range(len(b)):
	f.write(u+b[i][2])
	f.write("\n")
f.close()	
