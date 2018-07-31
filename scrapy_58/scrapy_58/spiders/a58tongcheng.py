# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from scrapy_58.items import Scrapy58Item


class A58tongchengSpider(CrawlSpider):
    name = '58tongcheng'
    allowed_domains = ['sh.58.com']
    start_urls = ['http://sh.58.com/pudongxinqu/zufang/j3/pn1/?PGTID=0d300008-0058-36db-e632-b9dba788aa12&ClickID=2']
    lx = r'http://sh\.58\.com/pudongxinqu/zufang/j3/pn(\d{1,2})/\?PGTID=0d300008-0058-36db-e632-b9dba788aa12&ClickID=2'

    rules = (
        Rule(LinkExtractor(allow=lx), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        pat = '//div[@class="des"]/h2/a/@href'
        urls_list = response.xpath(pat)
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        print(urls_list)
        for url in urls_list:
            print("***********************************************************")
            item = Scrapy58Item()
            new_url = url.extract()
            print(new_url)
            html = detail_parse("http:"+new_url)
            print("*************************************************************")
            print("*************************************************************")
            print(html)
            print("*************************************************************")
            print("*************************************************************")
            item["house_prize"] = html.xpath('//b[@class="f36"]/text()')[0]
            item["rend_style"] = html.xpath('//ul[@class="f14"]/li[1]/span[2]/text()')[0]
            item["house_style"] = html.xpath('//ul[@class="f14"]/li[2]/span[2]/text()')[0]
            item["house_faceto"] = html.xpath('//ul[@class="f14"]/li[3]/span[2]/text()')[0]
            item["house_zone"] = html.xpath('//ul[@class="f14"]/li[4]/span[2]/a/text()')[0]
            item["house_location"] = html.xpath('//ul[@class="f14"]/li[5]/span[2]/text()')[0]
            item["house_addressw"] = html.xpath('//ul[@class="f14"]/li[6]/span[2]/text()')[0]
            print(item)
            yield item



def detail_parse(url):
    import requests
    from lxml import etree
    headers = {
        "User-Agent": "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50\
            (KHTML,likeGecko)Version/5.1Safari/534.50",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
    }
    print("????????????????????????????????????????????????????????????????????????????????")
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    print("888888888888888888888888888888888888888888888888888888888888888888888888888888888")
    return html



