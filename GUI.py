# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui
import sys
import os

os.chdir("/Users/kilimetr/Desktop/python/Billet&Schultes")

import packings_list



class Window(QtWidgets.QMainWindow):

	def __init__(self,**kwargs):
		super(Window, self).__init__(**kwargs)
		self.setWindowTitle("Hydraulic Calculation for Packings Column")
		self.init_gui()
		self.show()

	def init_gui(self):
		formular 	   = QtWidgets.QWidget()
		formularLayout = QtWidgets.QVBoxLayout()
		formular.setLayout(formularLayout)

		boxLayout1 = QtWidgets.QHBoxLayout() # user parameters area = INPUT
		boxLayout2 = QtWidgets.QHBoxLayout() # results area = OUTPUT

		formularLayout.addStretch()
		formularLayout.addLayout(boxLayout1)
		formularLayout.addLayout(boxLayout2)
		formularLayout.addStretch()

		self.packingsLabel = QtWidgets.QLabel("Packing Type", self)
		self.packingsLabel.setFont(QtGui.QFont("Arial",12, QtGui.QFont.Black))

		self.packingsTypeComboBox = QtWidgets.QComboBox(self)
		self.packingsTypeComboBox.addItems(packings_list.export_packing_name)
		self.packingsTypeComboBox.activated.connect(self.packingsTypeChanged)

		boxLayout1.addWidget(self.packingsLabel)
		boxLayout2.addWidget(self.packingsTypeComboBox)

		self.setCentralWidget(formular)

	def packingsTypeChanged(self):
		export_packing_surfacearea = []

		for item in packings_list.packings:
  		  if item["name"] == type_packing:
 		       export_packing_surfacearea.append(item["a"])

		print(export_packing_surfacearea)
	


aplikace = QtWidgets.QApplication(sys.argv)
okno = Window()
sys.exit(aplikace.exec_())


# app = QtWidgets.QApplication([])

# # QComboBox - políčko pro výběr z několika možností
# box = QtWidgets.QComboBox()
# box.addItem('First Option')
# box.addItem('Second Option')

# # Základní varianta napojí na activated[int]
# box.activated.connect(print)

# # Výběr varianty signálu pomocí hranatých závorek
# box.activated[str].connect(print)
# box.activated[int].connect(print)

# # Hlavní okno
# main = QtWidgets.QWidget()
# main.setWindowTitle('Hello Qt')

# # Layout pro hlavní okno
# layout = QtWidgets.QHBoxLayout()
# main.setLayout(layout)

# # Nápis
# label = QtWidgets.QLabel('Click the button to change me')
# # Přidáním do layoutu se nápis automaticky stane potomkem hlavního okna
# layout.addWidget(label)

# # Tlačítko
# button = QtWidgets.QPushButton('Click me')
# layout.addWidget(button)

# # Funkcionalita
# def change_label():
#     label.setText('Good job. +100 points.')

# button.clicked.connect(change_label)

# # Spuštění
# main.show()
# box.show()
# app.exec()

