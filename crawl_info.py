# -*- coding:utf-8 -*-

import re
from lxml.html import soupparser, tostring, HtmlElement


def re_search(text, exp):
    re_result_list = re.findall(r'%s' % exp, text, re.S)
    return re_result_list


def xpath_search(html, exp):
    root = soupparser.fromstring(html)
    result_ele = root.xpath(exp)
    return __elements_to_unicodes__(result_ele)


def __elements_to_unicodes__(eles):
    xpath_result_list = []
    for r in eles:
        xpath_result_list.append(tostring(r, encoding='utf-8').decode('utf-8') if isinstance(r, HtmlElement) else r)
    return xpath_result_list
