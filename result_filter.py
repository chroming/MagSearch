# -*- coding: utf-8 -*-
from tools import log_wrap


class ResultFilter(object):
    """
    filter_dict: {'contain':unicode, 'size':[min,max]}
    """
    @log_wrap
    def __call__(self, result_list, filter_dict):
        """
        
        :param result_list: 需要处理的结果列表
        :param filter_dict: 过滤规则, {'contain':unicode, 'size':[min,max]} 
        :return: 过滤结果
        """
        self.result_list = result_list
        self.contain_uni = filter_dict['contain']
        self.size_min, self.size_max = filter_dict['size']
        self._contains_()
        self._size_limits_()
        return self.result_list

    def _contains_(self):
        if self.contain_uni:
            new_result_list = []
            for result in self.result_list:
                if self._contain_(result[0]):
                    new_result_list.append(result)
            self.result_list = new_result_list

    @log_wrap
    def _contain_(self, result):
        return True if self.contain_uni in result else False

    def _size_limits_(self):
        if self.size_min or self.size_max:
            new_result_list = []
            for result in self.result_list:
                if self._size_limit_(int(result[1].replace(',', ''))):
                    new_result_list.append(result)
            self.result_list = new_result_list

    @log_wrap
    def _size_limit_(self, result):
        return True if self.size_min <= result <= self.size_max else False