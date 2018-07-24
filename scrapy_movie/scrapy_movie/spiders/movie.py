# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['list.iqiyi.com']
    start_urls = ['http://list.iqiyi.com/www/1/2-------------11-3-1-iqiyi--.html']
    lx = r"www\.iqiyi\.com/v_19rr"
    rules = (
        Rule(LinkExtractor(allow=lx), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        pat = "/html/body/div[3]/div/div/div[3]/div/ul/li/div[1]/a/@href"
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
