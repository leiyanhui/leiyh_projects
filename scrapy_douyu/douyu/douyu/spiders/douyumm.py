# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import scrapy
import json
from .. import items


class DouYuSpider(scrapy.Spider):

    name = "douyumm"
    allowed_domains =[".douyu.com"]
    url="https://www.douyu.com/gapi/rkc/directory/2_201/"

    start = 1


    start_urls =[url+str(start)]

    def parse(self, response):
        data =json.loads(response.text)['data']["rl"]
        for each in data:
            item = items.DouyuItem()
            item["nickName"]=each["nn"]
            item["imageLink"]=each["rs1"]
            print "正在执行parse=================================="
            yield item

        if self.start<4:
            self.start += 1
            print "****************************************************************************************"
            print self.url+str(self.start)
            print "****************************************************************************************"
            yield scrapy.Request(self.url+str(self.start),callback=self.parse,dont_filter=True)