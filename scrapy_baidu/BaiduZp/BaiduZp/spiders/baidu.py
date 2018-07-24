# -*- coding: utf-8 -*-
import scrapy

import json

from BaiduZp.items import BaiduzpItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['talent.baidu.com']
    url = 'https://talent.baidu.com/baidu/web/httpservice/getPostList?postType=0/1227/10002&workPlace=0/4/10/11&recruitType=2&keyWord=&pageSize=10&curPage='

    curPage = 1

    start_urls = [url+str(curPage)]

    def parse(self, response):

        # 处理响应回来的数据

        context= response.body
        content = json.loads(context)

        result = content["postList"]
        # return (content["postList"][0]["name"])

        for each in result:
            item =BaiduzpItem()

            job_name = each["name"]
            job_type = each["postType"]
            job_location = each["workPlace"]
            job_num = each["recruitNum"]
            job_time = each["publishDate"]

            item["job_name"]=job_name
            item["job_type"]=job_type
            item["job_location"]=job_location
            item["job_num"]=job_num
            item["job_time"]=job_time

            yield item

        if self.curPage<14:

            self.curPage+=1

        yield  scrapy.Request(self.url+str(self.curPage),callback=self.parse)









