# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AishhSpider(CrawlSpider):
    name = 'aishh'
    allowed_domains = ['www.aish.pro']
    start_urls = ['http://www.aish.pro/thread-43123-1-1.html']


    pat = '//div[@class="beijing007s"]/a/@href'

    rules = (
        Rule(LinkExtractor(restrict_xpaths=pat), callback='parse-item'),
    )

    def parse_item(self, response):
        lx = LinkExtractor(restrict_xpaths=self.pat)
        print lx.extract_links(response)

        # i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        detail_pat = '//div[@class="mbn savephotop"]/img/@src'

        img_links = response.xpath(detail_pat)

        for link in img_links:
            print link
