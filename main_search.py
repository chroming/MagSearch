# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import sys
from search_mag import AliRequest
from tools import *
from result_filter import ResultFilter
from mag_search_ui import Ui_MainWindow
from web_thread import WebThread


class MainSearchUi(QtGui.QMainWindow, Ui_MainWindow, QtToPython):
    def __init__(self):
        super(MainSearchUi, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('MagSearch V0.0.2')
        self.search_pushbutton.clicked.connect(self.search_button_clicked)
        self.result_treewidget.customContextMenuRequested.connect(self.result_tree_widget_context)

    def show_status(self, message, timeout=5000):
        return self.statusbar.showMessage(message, timeout)

    def get_search_text(self):
        return self.get_line_edit_unicode(self.input_lineedit)

    def search_button_clicked(self):
        self.search_clear()
        search_text = self.get_search_text()
        self.show_status(u"开始搜索 %s , 请稍后……" % search_text)
        self.web_thread = WebThread(search_text, AliRequest)
        self.web_thread.finishSignal.connect(self.web_thread_finished)
        self.web_thread.start()

    def web_thread_finished(self, all_mag_list):
        self.filter_before_show(all_mag_list)

    def search_clear(self):
        self.result_treewidget.clear()

    @log_wrap
    def filter_before_show(self, result_list):
        self.show_status(requests_error[result_list[0]]) if result_list in requests_error_list else \
                        self.show_search_result_list(ResultFilter()(result_list, self.get_filter_dict()))

    def get_filter_dict(self):
        return {'contain': self.get_line_edit_unicode(self.filter_lineedit)
                if self.use_filter_checkbox.isChecked() else False, 'size': self.get_size_limit_from_gui()}

    def get_size_limit_from_gui(self):
        if self.size_limit_checkbox.isChecked():
            return [self.get_line_edit_int(self.more_than_lineedit)*1024*1024 if self.more_than_lineedit.text else 0,
                    self.get_line_edit_int(self.less_than_lineedit)*1024*1024 if self.less_than_lineedit.text else 10000000000000]
        else:
            return [False, False]

    @log_wrap
    def show_search_result_list(self, result_list):
        for result in result_list:
            self.show_status(requests_error[result[0]]) if result in requests_error_list \
                else self.show_search_result(result)
        self.show_status(u"搜索结束!", 10000)

    def show_search_result(self, result):
        return self.result_treewidget.addTopLevelItem(QtGui.QTreeWidgetItem(result))

    def result_tree_widget_context(self):
        context_menu = QtGui.QMenu()
        context_menu.addAction(u"复制磁力链接", self.copy_magnet)
        context_menu.exec_(QtGui.QCursor.pos())

    def copy_magnet(self):
        clip = app.clipboard()
        clip.setText(self.get_current_item_string(self.result_treewidget, 2))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainSearchUi()
    window.show()
    sys.exit(app.exec_())



