# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy58Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house_prize = scrapy.Field()
    rend_style = scrapy.Field()
    house_style = scrapy.Field()
    house_faceto = scrapy.Field()
    house_zone = scrapy.Field()
    house_location = scrapy.Field()
    house_addressw = scrapy.Field()

