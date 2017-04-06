# -*- coding: utf-8 -*-
from PyQt4 import QtCore


class WebThread(QtCore.QThread):
    finishSignal = QtCore.pyqtSignal(list)

    def __init__(self, keyword, search_engine):
        super(WebThread, self).__init__()
        self.search = search_engine()
        self.search.search_keyword(keyword)

    def run(self):
        mag_generator = self.search.get_iter_mag_result()
        while True:
            try:
                self.try_return(mag_generator)
            except StopIteration:
                self.return_error()
                break
        self.exit()

    def try_return(self, mag_generator):
        self.finishSignal.emit(mag_generator.next())

    def return_error(self):
        self.finishSignal.emit(['FINISHED'])