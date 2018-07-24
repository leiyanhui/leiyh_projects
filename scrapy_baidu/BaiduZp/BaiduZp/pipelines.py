# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class BaiduzpPipeline(object):

    def __init__(self):
        self.file = open("job.json", "w")

    def process_item(self, item, spider):

        text = json.dumps(dict(item), ensure_ascii=False)+"\n"

        self.file.write(text.encode("utf-8"))

        return item

    def close_spider(self):

        self.file.close()