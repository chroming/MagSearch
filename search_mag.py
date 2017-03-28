# -*- coding: utf-8 -*-

import requests
from crawl_info import *


class MagRequests(object):

    def __init__(self, keyword):
        self.url = ''
        self.keyword = keyword
        self.header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1'
    }

    @property
    def postdata(self):
        return self.__make_postdata__()

    def __make_postdata__(self):
        pass

    def web_get(self):
        return requests.get(self.url, headers=self.header).text

    def web_post(self):
        return requests.post(self.url, headers=self.header, data=self.postdata).text

    @staticmethod
    def get_result(result):
        pass
