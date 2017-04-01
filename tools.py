# -*- coding:utf-8 -*-
import logging
from functools import wraps

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def logwap(func):
    """
    输出函数参数作为日志的装饰器
    调用choice_sli 将单条日志长度限制在limit_len个字符串内
    :param func: 装饰的函数
    :return: 装饰后的函数
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("ARG INFO: %s %s %s" % (func.__name__, args, kwargs))
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
