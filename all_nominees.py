#befor use --use command line to type "sudo pip install wikipedia"
# -*- coding: utf-8 -*-
import wikipedia
import requests
years = 2016
seq = years - 1942
n = wikipedia.page(str(seq) + "th Golden Globe Awards")
link = n.url.encode('utf-8')
response = requests.get(link)
text = response.text.encode('utf-8')

str1 = "Best Motion Picture – Drama"
res = []
origin = text.find(str1)-32
text = text[origin:]
start = text.find("title=\"")
end = text.find("\">") 
count = 1

while start != -1 and count < 334:
	end = text.find("\">")
	if text[start+7:end+1]:
		res.append(text[start+7:end])
		count += 1
	start = end+2
	text = text[start:]
	start = text.find("title=\"")
	if "valign=\"top\"" in text[:start]:
		res.append('====as followings======')

for i in res:
	print i

