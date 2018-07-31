# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_tencent.items import ScrapyTencentItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?keywords=&lid=2175&tid=87&start=0']
    xp = r"position\.php\?keywords=&lid=2175&tid=87&start=\d+"
    rules = (
        Rule(LinkExtractor(allow=xp), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        tr_list = response.xpath("//tr[@class='even']|//tr[@class='odd']")

        for each in tr_list:
            
            item = ScrapyTencentItem()
            # 职位名称
            job_name = each.xpath("./td[1]/a/text()").extract()
            # 职位类别
            job__type = each.xpath("./td[2]/text()").extract()
            # 招聘人数
            job_num = each.xpath("./td[3]/text()").extract()
            # 工作地点
            job_location = each.xpath("./td[4]/text()").extract()
            # 发布日期
            job_data = each.xpath("./td[5]/text()").extract()

            item['job_name'] = job_name[0]
            item['job__type'] = job__type[0]
            item['job_num'] = job_num[0]
            item['job_location'] = job_location[0]
            item['job_data'] = job_data[0]
            yield item
