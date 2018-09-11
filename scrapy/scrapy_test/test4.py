# -*- coding: utf-8 -*-

import urllib
from urllib.parse import urlparse, urlunparse, parse_qs

s = urlparse('https://www.baidu.com/s?wd=X-Requested-With&rsv_spt=1&rsv_iqid=0x9c03390c0001825b&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=0&rsv_sug3=2&rsv_sug1=1&rsv_sug7=100&prefixsug=X-Requested-With&rsp=0&inputT=166251&rsv_sug4=166251')
print(s)

url = urlunparse(s)
print(url)
print(parse_qs(url))
