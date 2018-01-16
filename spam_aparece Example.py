import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QApplication, QHBoxLayout, QWidget, QLabel, QPushButton,
                             QGridLayout, QVBoxLayout, QLineEdit, QAction)


class AddWord(QWidget):
    def __init__(self):
        self.setWindowTitle('New Word')
        self.label_word = QLabel('word', self)
        self.label_kind_word = QLabel('grammar word', self)
        self.label_translation = QLabel('traslation', self)
        self.label_example = QLabel('example', self)


class Spam(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_GUI()

    def init_GUI(self):

        # Creamos una etiqueta para status. Recordar que los os Widget simples
        # no tienen StatusBar.
        self.label1 = QLabel('hola', self)
        self.edit1 = QLineEdit('', self)

        # Creamos la grilla para ubicar los Widget (botones) de manera matricial
        self.grilla = QGridLayout()

        valores = ['1', '2', '3',
                   '4', '5', '6',
                   '7', '8', '9',
                   '0', 'CE', 'C']

        # Generamos las posiciones de los botones en la grilla y le asociamos
        # el texto que debe desplegar cada boton guardados en la lista valores

        posicion = [(i, j) for i in range(4) for j in range(3)]

        for posicion, valor in zip(posicion, valores):
            if valor == '':
                continue

            boton = QPushButton(valor)
            boton.clicked.connect(self.muestra_boton)

            # El * permite convertir los elementos de la tupla como argumentos
            # independientes
            self.grilla.addWidget(boton, *posicion)

        # Creamos un layout vertical
        vbox = QVBoxLayout()

        # Agregamos el label al layout con addWidget
        vbox.addWidget(self.label1)
        vbox.addWidget(self.edit1)

        # Agregamos el layout de la grilla al layout vertical con addLayout
        vbox.addLayout(self.grilla)
        self.setLayout(vbox)

        self.move(300, 150)
        self.setWindowTitle('Calculator')

    def muestra_boton(self):
        sender = self.sender()
        print(sender.text())


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

        print(self.__dict__)

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
        """
        Este método es el encargado ejecutar una acción cada vez que el botón
        es presionado. En esta caso, realiza el cambio en label2 y el status bar
        mediate la emisión de una señal en la cual se envía el texto correspondiente.
        """
        self.label2.setText('Echo texto: {}'.format(self.edit.text()))
        self.status_bar.emit('Qedit: {}'.format(self.edit.text()))

    def load_status_bar(self, signal):
        """
        Este método recibirá una señal desde el MainWindow que permitirá hacer cambios
        en el status bar desde el widget central.
        """
        self.status_bar = signal


class MainWindow(QMainWindow):
    """
    Esta señal permite comunicar la barra de estados con el resto de los widgets
    en el formulario, incluidos el central widget.
    """
    onchange_statusbar = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        """Configuramos la geometría de la ventana."""
        self.setWindowTitle('Ventana con Boton')
        self.setGeometry(200, 100, 300, 250)
        self.spam = Spam()

        """Configuramos las acciones."""
        ver_status = QAction(QIcon(None), '&Cambiar Status', self)
        ver_status.setStatusTip('Este es un ítem de prueba')
        ver_status.triggered.connect(self.cambiar_status_bar)

        spam_test = QAction(QIcon(None), '&Spam aparece', self)
        spam_test.setStatusTip('debería lanzar otra ventana')
        spam_test.triggered.connect(self.spam_aparece)

        salir = QAction(QIcon(None), '&Exit', self)
        salir.setShortcut('Ctrl+Q')
        salir.setStatusTip('Exit application')
        salir.triggered.connect(QApplication.quit)

        """Creamos la barra de menú."""
        menubar = self.menuBar()
        archivo_menu = menubar.addMenu('&Archivo')  # primer menú
        archivo_menu.addAction(ver_status)
        archivo_menu.addAction(spam_test)
        archivo_menu.addAction(salir)

        otro_menu = menubar.addMenu('&Otro Menú')  # segundo menú

        """Incluímos la barra de estado."""
        self.statusBar().showMessage('Listo')
        self.onchange_statusbar.connect(self.update_status_bar)

        """
        Configuramos el widget central con una instancia de la clase
        Formulario(). Además cargamos la señal en el central widget para 
        que este pueda interactuar con la barra de estados de la ventana 
        principal.
        """
        self.form = MiFormulario()
        self.setCentralWidget(self.form)
        self.form.load_status_bar(self.onchange_statusbar)

    def cambiar_status_bar(self):
        self.statusBar().showMessage('Cambié el Status')

    def update_status_bar(self, msg):
        self.statusBar().showMessage(msg)

    def spam_aparece(self):
        self.spam.show()


if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
