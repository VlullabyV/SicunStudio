# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import re

account = input("Please input your username:")
url = "https://github.com/"+account+"?tab=repositories" #目标链接

headers = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)" #请求报头

req = request.Request(url)
req.add_header("User-Agent",headers)
response = request.urlopen(req)
data = response.read()
data = data.decode('UTF-8')
soup = BeautifulSoup(data,"html.parser") #还没有完全搞清楚BeautifulSoup的用法
data = soup.find_all(itemprop="name codeRepository") 
for i in data:
	print(i.string)