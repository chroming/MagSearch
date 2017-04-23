# -*- coding: utf-8 -*-

from crawl_info import *
from tools import *


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
        self.pgnum = 1

    def search_keyword(self, keyword, pgnum=1):
        self.keyword = keyword
        self.pgnum = pgnum

    def __make_postdata__(self):
        pass

    @property
    def postdata(self):
        return self.__make_postdata__()

    @time_sleep
    def web_get(self, url=None):
        return requests.get(url if url else self.url, headers=self.header, timeout=10).text

    @time_sleep
    def web_post(self, url=None):
        return requests.post(url if url else self.url, headers=self.header, data=self.postdata, timeout=10).text


class AliRequest(MagRequests):
    """
    http://alicili.org/ 请求类
    """
    def __init__(self):
        super(AliRequest, self).__init__()
        self.next_page_num = False

    def search_keyword(self, keyword, pgnum=1):
        self.keyword = keyword
        self.pgnum = pgnum
        self.url = 'http://alicili.org/list/%s/1-0-0/' % keyword

    def __make_postdata__(self):
        return {'keyword': self.keyword}

    def get_page_num(self, html):
        """
        获取需要抓取的结果分页数
        :param html: 
        :return: 分页数,int
        """
        next_page_num = re_search(html, u'<div class=\"pages\">\s*<span>共(\d+)页</span>')
        return min(self.pgnum, int(next_page_num[0])) if next_page_num else 1

    def get_mag_page_url(self, url=None):
        """
        获取单个分页上磁力页面的地址
        :param url: 
        :return: 
        """
        html = self.web_post(url)
        if self.next_page_num == False:
            self.next_page_num = self.get_page_num(html)
        return re_search(html, r'%s' % 'http://alicili.org/cili/\S*/')

    def get_all_mag_page_url(self):
        """
        获取所有分页的磁力页面的地址
        """
        all_mag_page_url = self.get_mag_page_url()
        next_page_url_list = self.get_next_page_url(self.next_page_num)
        if next_page_url_list:
            for url in next_page_url_list:
                all_mag_page_url.extend(self.get_mag_page_url(url))
        return all_mag_page_url

    # @requests_error_wrap
    def show_result(self):
        return self.get_all_mag_page_url()

    def get_one_page_mag(self, url):
        result = self.web_get(url)
        return re_search(result,
                         u'<p class=\'dd name\'><strong>(.*?\.torrent)</strong></p>.*?'
                         u'种子哈希：<b>(\w{40})</b><br />\s+文件数目：<b>(\d+)</b>个文件 <br />\s+'
                         u'文件大小：<b>.{1,20}</b>或<b>([\d,]+) Bytes</b><br />\s+收录时间：<b>(.*?)</b><br />\s+'
                         u'已经下载：<b>(\d+)</b>次<br />\s+下载速度：<b>.*?</b><br />\s+最近下载：<b>.*?</b></p>')

    @log_wrap
    @requests_error_wrap
    def choice_result(self, url):
        """
        获取单磁力页面上需要的内容并组合为所需格式
        :param url: 磁力页面url
        :return: 所需结果, [名称, 大小, 磁力连接]
        """
        result = self.get_one_page_mag(url)[0]
        return [result[0], result[3], u'magnet:?xt=urn:btih:' + result[1]]

    def get_all_mag_result(self):
        self.next_page_num = False
        url_list = self.show_result()
        if url_list in requests_error_list:
            return url_list
        mag_list = []
        for url in url_list:
            mag_list.append(self.choice_result(url))
        return mag_list

    def get_iter_mag_result(self):
        self.next_page_num = False
        url_list = self.show_result()
        return self.return_result_generator(url_list)

    def return_result_generator(self, url_list):
        if url_list in requests_error_list:
            return self.error_generator(url_list)
        return self.get_generator(url_list)

    @staticmethod
    def error_generator(result):
        yield result

    def get_generator(self, url_list):
        """
        输入磁力页面list, 以生成器形式返回所需最终结果
        :param url_list: 
        :return: 
        """
        for url in url_list:
            yield self.choice_result(url)

    def get_next_page_url(self, next_page_num):
        if next_page_num > 1:
            return ['http://alicili.org/list/%s/%s-0-0/' % (self.keyword, str(pn)) for pn in xrange(2, next_page_num+1)]


if __name__ == '__main__':
    a = AliRequest()
    a.search_keyword('变形金刚', 2)
    print a.get_all_mag_result()




