# -*- coding: utf-8 -*-

import requests
import json

num = [12, 24, 36, 48]
for i in num:
    url = 'https://s.taobao.com/api?_ksTS=1533870843148_226&callback=jsonp227&ajax=true&m=customized&sourceId=tb.index&q=%E4%BC%91%E9%97%B2%E7%94%B7%E8%A3%A4&spm=a21bo.2017.201856-taobao-item.1&s='+'%s'%i+'&imgfile=&initiative_id=tbindexz_20170306&bcoffset=-1&commend=all&ie=utf8&rn=7be9319663468928144beab6a50edb56&ssid=s5-e&search_type=item'

    response = requests.get(url, verify=False)
    html = response.text
    list = html.split('"API.CustomizedApi":')
    json1 = list[1].split("})")[0]
    dict1 = json.loads(json1)
    nums = dict1['itemlist']['auctions']
    n = 0
    for each in nums:
        n += 1
        print "%s\n%s\n%s\n%s\n%s\n%s\n" % (
            each["raw_title"], each["pic_url"], each["detail_url"], each["view_price"], each["item_loc"], each["nick"])
        print(n)
