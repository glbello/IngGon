import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout,
                             QVBoxLayout, QStackedLayout)
from PyQt5.QtCore import (QThread, pyqtSignal, QTimer, QObject, Qt)


class MiVentana1(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_GUI()

    """ 
        Este método configura la interfaz y todos sus widgets una vez que se
        llama __init__().
        """

    def init_GUI(self):
        # Ajustamos la geometria de la ventana
        self.setGeometry(200, 100, 300, 300)
        self.setWindowTitle('Ventana con Boton1')

        # # Agregamos etiquetas usando el widget QLabel
        # # self.label1 = QLabel('Texto1:', self)
        # # self.label1.move(10, 15)
        # #
        # # self.label2 = QLabel('Esta etiqueta es variable1', self)
        # # self.label2.move(10, 50)
        # #
        # # # Agregamos cuadros de texto mediante QLineEdit
        # # self.edit1 = QLineEdit('', self)
        # # self.edit1.setGeometry(45, 15, 100, 20)

        self.boton1 = QPushButton('&Next', self)
        self.boton1.resize(self.boton1.sizeHint())

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.boton1)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)


class MiVentana2(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_GUI()

    def init_GUI(self):
        """
        Este método configura la interfaz y todos sus widgets una vez que se
        llama __init__().
        """

        # Ajustamos la geometria de la ventana
        self.setGeometry(200, 100, 300, 300)
        self.setWindowTitle('Ventana con Boton2')

        #
        # # Agregamos etiquetas usando el widget QLabel
        # self.label1 = QLabel('Texto2:', self)
        # self.label1.move(10, 15)
        #
        # self.label2 = QLabel('Esta etiqueta es variable2', self)
        # self.label2.move(10, 50)
        #
        # # Agregamos cuadros de texto mediante QLineEdit
        # self.edit1 = QtWidgets.QLineEdit('', self)
        # self.edit1.setGeometry(45, 15, 100, 20)

        self.boton2 = QPushButton('&Next', self)
        self.boton2.resize(self.boton2.sizeHint())

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.boton2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)


class Principal(QMainWindow):
    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.wid1 = MiVentana1()
        self.wid2 = MiVentana2()

        self.stack_main = QStackedLayout()
        self.stack_main.addWidget(self.wid1)
        self.stack_main.addWidget(self.wid2)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stack_main)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec_())
