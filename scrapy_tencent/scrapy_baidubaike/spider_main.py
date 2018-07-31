# -*- coding: utf-8 -*-
import html_downloader
import html_parser
import out_puter
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManage()
        self.downloader =html_downloader.HtmlDownload()
        self.parser =  html_parser.Htmlparse()
        self.outputer = out_puter.OutPut()

    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d:%s'%(count,new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.cpllect_data(new_data)
                if count ==1000:
                    break
                count +=1
            except:
                print("craw faild")
        self.outputer.output_html()

if __name__ == '__main__':
    root_url ='http://baike.baidu.com/item/Python/407313'

    obj_spider = SpiderMain()
    obj_spider.craw(root_url)