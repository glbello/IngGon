import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QApplication, QHBoxLayout, QWidget, QLabel, QPushButton,
                             QGridLayout, QVBoxLayout, QLineEdit, QAction)


class MiFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):
        """
        Este método inicializa el main widget y sus elementos.
        """
        self.label1 = QLabel('Texto', self)
        self.label2 = QLabel('Echo texto:', self)

        self.edit = QLineEdit('', self)
        self.edit.setGeometry(45, 15, 100, 20)

        self.boton = QPushButton('&Procesar', self)
        self.boton.resize(self.boton.sizeHint())
        self.boton.clicked.connect(self.boton1_callback)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label1)
        hbox.addWidget(self.edit)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label2)
        hbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.boton)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def boton1_callback(self):
        self.label2.setText('Echo texto: {}'.format(self.edit.text()))


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ventana con Boton')
        self.setGeometry(500, 300, 300, 150)

        menubar = self.menuBar()
        archivo_menu = menubar.addMenu('&Archivo')  # primer menú


        self.form = MiFormulario()
        self.setCentralWidget(self.form)

    # def update_status_bar(self, msg):
    #     self.statusBar().showMessage(msg)


if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
