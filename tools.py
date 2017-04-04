# -*- coding:utf-8 -*-
import logging
from functools import wraps
import requests
import time
import random

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def log_wrap(func):
    """
    输出函数参数作为日志的装饰器
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # logging.info("ARG INFO: %s %s %s" % (func.__name__, args, kwargs))
        print("ARG INFO: %s %s %s" % (func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return wrapper

requests_error = {
    'TIMEOUT!': u"访问超时!",
    'NETWORKERROR!': u"网络连接错误!",
    'SERVERRETURNERROR!': u"服务器返回错误!",
    'UNKNOWNERROR!': u"未知网络错误!"
}


def requests_error_wrap(func):
    """
    requests的错误装饰器
    用于在requests网络访问错误时输出错误类型而不是raise error
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except requests.exceptions.Timeout:
            return 'TIMEOUT!'
        except requests.exceptions.ConnectionError:
            return 'NETWORKERROR!'
        except requests.exceptions.HTTPError:
            return 'SERVERRETURNERROR!'
        except Exception, e:
            return 'UNKNOWNERROR!'
    return wrapper


def time_sleep(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(1+random.random())
        return func(*args, **kwargs)
    return wrapper


class QtToPython(object):
    """
    获取Qt界面元素的Python类型属性
    """
    @staticmethod
    def get_line_edit_unicode(line_edit):
        return line_edit.text().toUtf8().data().decode('utf-8')

    @staticmethod
    def get_line_edit_string(line_edit):
        return line_edit.text().toUtf8().data()

    @staticmethod
    def get_line_edit_int(line_edit):
        return int(line_edit.text().toUtf8().data())

    @staticmethod
    def get_current_item_string(tree_widget, column):
        return tree_widget.currentItem().text(column).toUtf8().data() if tree_widget.currentItem() else ''