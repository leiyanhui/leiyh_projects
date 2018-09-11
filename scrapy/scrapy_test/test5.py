# -*- coding: utf-8 -*-

import requests
from lxml import etree

url = "http://httpbin.org/get"
response = requests.get(url)

html = response.text.encode('utf-8')
print(html)
html = etree.HTML(html)
print(html)
