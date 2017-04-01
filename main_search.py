from PyQt4 import QtGui, uic
import sys
from search_mag import AliRequest
from tools import QtToPython

Ui_MainWindow, QtBaseClass = uic.loadUiType('mag_search.ui')


class MainSearchUi(QtGui.QMainWindow, Ui_MainWindow, QtToPython):
    def __init__(self):
        super(MainSearchUi, self).__init__()
        self.setupUi(self)
        self.ali = AliRequest()
        self.search_pushbutton.clicked.connect(self.search_button_clicked)

    def get_search_text(self):
        return self.get_line_edit_unicode(self.input_lineedit)

    def search_button_clicked(self):
        search_text = self.get_search_text()
        self.ali.search_keyword(search_text)
        self.show_search_result_list(self.ali.get_all_mag_result())

    def search_clear(self):
        self.result_treewidget.clear()

    def show_search_result_list(self, result_list):
        for result in result_list:
            self.show_search_result(result)

    def show_search_result(self, result):
        return self.result_treewidget.addTopLevelItem(QtGui.QTreeWidgetItem(result))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainSearchUi()
    window.show()
    sys.exit(app.exec_())



