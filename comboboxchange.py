import sys
import os
 
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout

os.chdir("/Users/kilimetr/Desktop/python/Billet&Schultes")

import packings_list
 
class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
 
        self._items = {
            "a": ["1", "2", "3"],
            "b": ["a", "b", "b"]}
 
        self._combobox_1 = QComboBox()
        self._combobox_2 = QComboBox()
        self._combobox_3 = QComboBox()
        self._combobox_4 = QComboBox()

        # self._combobox_1.addItems(self._items.keys())
        packingList = []
        for item in packings_list.packings:
            packingList.append(item["name"])

        self._combobox_1.addItems(packingList)
        self._combobox_3.addItems(packings_list.export_packing_name)

        layout = QVBoxLayout()
        layout.addWidget(self._combobox_1)
        layout.addWidget(self._combobox_2)
        layout.addWidget(self._combobox_3)
        layout.addWidget(self._combobox_4)
        
        self._handle_item_change()
 
        self.setLayout(layout)
 
        self._combobox_1.activated.connect(self._handle_item_change)
        self._combobox_3.activated.connect(self._handle_item_change)

    # @pyqtSlot()
    def _handle_item_change(self):
        cb_item = self._combobox_1.currentText()
        cb_pack = self._combobox_3.currentText()
        # print(cb_pack)

        self._combobox_2.clear()
        self._combobox_4.clear()
        # self._combobox_2.addItems(self._items[cb_item])
        # self._combobox_4.addItems()

        packingsArea = []
        for item in packings_list.packings:
            if item["name"] == cb_pack:
                packingsArea.append(str(item["a"]))

        # print(packingsArea)
        self._combobox_4.addItems(packingsArea)

 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
sys.exit(app.exec_())