# -*- coding: utf-8 -*-
from PyQt4 import QtCore
import types


class WebThread(QtCore.QThread):
    # finishSignal = QtCore.pyqtSignal(types.GeneratorType)
    finishSignal = QtCore.pyqtSignal(list)

    def __init__(self, keyword, search_engine):
        super(WebThread, self).__init__()
        self.search = search_engine()
        self.search.search_keyword(keyword)

    def run(self):
        # all_mag_list = self.search.get_all_mag_result()
        all_mag_list = self.search.get_iter_mag_result()
        for i in all_mag_list:
            self.finishSignal.emit(i)