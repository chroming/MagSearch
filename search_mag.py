# -*- coding: utf-8 -*-

import requests
from crawl_info import *
from tools import logwap


class MagRequests(object):
    """
    请求基类
    """
    def __init__(self):
        self.url = ''
        self.keyword = ''
        self.re_exp = ''
        self.xpath_exp = ''
        self.header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1'
    }

    def search_keyword(self, keyword):
        self.keyword = keyword

    def __make_postdata__(self):
        pass

    @property
    def postdata(self):
        return self.__make_postdata__()

    def web_get(self, url=None):
        return requests.get(url if url else self.url, headers=self.header).text

    def web_post(self, url=None):
        return requests.post(url if url else self.url, headers=self.header, data=self.postdata).text

    def get_result(self):
        pass


class AliRequest(MagRequests):
    """
    http://alicili.org/ 请求类
    """
    def __init__(self):
        super(AliRequest, self).__init__()

    def search_keyword(self, keyword):
        self.keyword = keyword
        self.url = 'http://alicili.org/list/%s/1-0-0/' % keyword

    def __make_postdata__(self):
        return {'keyword': self.keyword}

    def get_result(self):
        result = self.web_post()
        return re_search(result, r'%s' % 'http://alicili.org/cili/\S*/')

    def show_result(self):
        return self.get_result()

    def get_mag_result(self, url):
        result = self.web_get(url)
        # return re_search(result, r'%s' % 'magnet:\?xt=urn:btih:\S{40}')
        return re_search(result,
                         u'<p class=\'dd name\'><strong>(.*?\.torrent)</strong></p>.*?'
                         u'种子哈希：<b>(\w{40})</b><br />\s+文件数目：<b>(\d+)</b>个文件 <br />\s+'
                         u'文件大小：<b>.{1,20}</b>或<b>([\d,]+) Bytes</b><br />\s+收录时间：<b>(.*?)</b><br />\s+'
                         u'已经下载：<b>(\d+)</b>次<br />\s+下载速度：<b>.*?</b><br />\s+最近下载：<b>.*?</b></p>')

    @logwap
    def choice_result(self, url):
        result = self.get_mag_result(url)[0]
        print result
        return [result[0], result[3], u'magnet:?xt=urn:btih:'+ result[1], 'alicili.org']

    def get_all_mag_result(self):
        url_list = self.show_result()
        mag_list = []
        for url in url_list:
            mag_list.append(self.choice_result(url))
        return mag_list

if __name__ == '__main__':
    a = AliRequest()
    a.search_keyword('soe-917')
    a.get_all_mag_result()




