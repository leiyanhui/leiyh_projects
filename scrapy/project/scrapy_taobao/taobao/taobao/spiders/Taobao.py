# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TaobaoSpider(CrawlSpider):
    name = 'Taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E7%94%B7%E8%A3%A4%E5%AD%90%E4%BC%91%E9%97%B2%E7%94%B7&suggest=0_2&_input_charset=utf-8&wq=nanku&suggest_query=nanku&source=suggest']
    detail_pat = '//div[@class="item J_MouserOnverReq item-ad  "]/div[@class="pic-box J_MouseEneterLeave J_PicBox"]/div[@class="pic-box-inner"]/div[@class="pic"]/a/@href'

    rules = (
        Rule(LinkExtractor(restrict_xpaths=pat), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
