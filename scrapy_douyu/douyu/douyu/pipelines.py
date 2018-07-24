# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline

import os


class DouyuPipeline(ImagesPipeline):
    image_store = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["imageLink"]
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_path = [x for ok, x in results if ok]
        # print "************************************************************************************"
        # print self.image_store, "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        # print  image_path[0]["path"]
        # print "************************************************************************************"
        os.rename(self.image_store+"/"+str(image_path[0]["path"]),self.image_store+"/full/"+item["nickName"]+".jpg")
        item['imagePath'] = self.image_store+"/full/"+item["nickName"]+".jpg"
        return item


