# -*- coding: utf-8 -*-
import urllib2


class HtmlDownload(object):
    def download(self, url):
        if url is None:
            return  None
        reponse = urllib2.urlopen(url)

        if reponse.getcode() !=200:
            return None
        return reponse.read()