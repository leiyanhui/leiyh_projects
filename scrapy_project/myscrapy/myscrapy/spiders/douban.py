# -*- coding: utf-8 -*-
import scrapy

from myscrapy.items import MyscrapyItem




class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['http://movie.douban.com/chart']

    def parse(self, response):
        filename ="movies.html"
        # with open(filename,"w") as f:
            # f.write(response.body)
        movie_list = response.xpath('//tr[@class="item"]//div[@class="pl2"]')

        movie_items =[]

        for movieEle in movie_list:
            item = MyscrapyItem()

            name = "".join(movieEle.xpath('a/text()').extract()).replace("\n", "").replace(" ", "") + "".join(
                movieEle.xpath('a/span/text()').extract()).replace("\n", "").replace(" ", "")
            rating_nums = movieEle.xpath('.//span[@class="rating_nums"]/text()').extract()[0]
            pl = movieEle.xpath('.//span[@class="pl"]/text()').extract()[0]

            item["name"] = name
            item["rating_nums"] = rating_nums
            item["pl"] = pl

            movie_items.append(item)

        yield movie_items
