# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['www.renren.com']
    start_urls = ["http://www.renren.com/PLogin.do"]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                'email':'1139656712@qq.com',
                'password':'qwe123123'
            },
            callback=self.after_login
        )

    def after_login(self, response):
        with open("aa.html", "wb") as f:
            f.write(response.body)
