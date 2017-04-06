# -*- coding: utf-8 -*-
from tools import *


class ResultFilter(object):
    """
    filter_dict: {'contain':unicode, 'size':[min,max]}
    """
    @log_wrap
    def __call__(self, result, filter_dict, result_type='list'):
        """
        
        :param result: 需要处理的结果, 可能为结果列表或单项结果
        :param filter_dict: 过滤规则, {'contain':unicode, 'size':[min,max]} 
        :return: 过滤结果
        """
        self.result_list = result
        self.contain_uni = filter_dict['contain']
        self.size_min, self.size_max = filter_dict['size']
        return self.__all_or_one__(result_type)

    def __all_or_one__(self, result_type):
        return self.receive_all_result() if result_type == 'list' else self.receive_one_result()

    def receive_all_result(self):
        self._contains_()
        self._size_limits_()
        return self.result_list

    def receive_one_result(self):
        return (self._contain_(self.result_list) if self.contain_uni else True) & \
               (self._size_limit_(self.result_list) if self.size_min or self.size_max else True)

    def _contains_(self):
        if self.contain_uni:
            new_result_list = []
            for result in self.result_list:
                if self._contain_(result):
                    new_result_list.append(result)
            self.result_list = new_result_list

    @log_wrap
    def _contain_(self, result):
        return True if self.contain_uni in result[0] else False

    def _size_limits_(self):
        if self.size_min or self.size_max:
            self.result_list = [result for result in self.result_list if self._size_limit_(result)]

    @log_wrap
    def _size_limit_(self, result):
        return True if self.size_min <= int(result[1].replace(',', '')) <= self.size_max else False