import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets
from cliente2.cliente_listar import ListarClientesWindow
from cliente2.cadastro_cliente import CadastroClienteWindow
from cliente2.Deletar_cliente import DeletarClienteWindow
from cliente2.atualizar_cliente import AtualizarClienteWindow
from cliente2.cliente_obter_cliente import ClienteObter

class Ui_Tela_Cliente(object):
    def setupUi(self, Tela_Cliente):
        Tela_Cliente.setObjectName("Tela_Cliente")
        Tela_Cliente.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(Tela_Cliente)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(12)

        self.pushButton_listar_clientes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_listar_clientes.setGeometry(QtCore.QRect(50, 30, 300, 40))
        self.pushButton_listar_clientes.setObjectName("pushButton_listar_clientes")
        self.pushButton_listar_clientes.setFont(font)

        self.pushButton_obter_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_obter_cliente.setGeometry(QtCore.QRect(50, 80, 300, 40))
        self.pushButton_obter_cliente.setObjectName("pushButton_obter_cliente")
        self.pushButton_obter_cliente.setFont(font)

        self.pushButton_cadastrar_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cadastrar_cliente.setGeometry(QtCore.QRect(50, 130, 300, 40))
        self.pushButton_cadastrar_cliente.setObjectName("pushButton_cadastrar_cliente")
        self.pushButton_cadastrar_cliente.setFont(font)

        self.pushButton_atualizar_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_atualizar_cliente.setGeometry(QtCore.QRect(50, 180, 300, 40))
        self.pushButton_atualizar_cliente.setObjectName("pushButton_atualizar_cliente")
        self.pushButton_atualizar_cliente.setFont(font)

        self.pushButton_deletar_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_deletar_cliente.setGeometry(QtCore.QRect(50, 230, 300, 40))
        self.pushButton_deletar_cliente.setObjectName("pushButton_deletar_cliente")
        self.pushButton_deletar_cliente.setFont(font)

        Tela_Cliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tela_Cliente)
        QtCore.QMetaObject.connectSlotsByName(Tela_Cliente)

    def retranslateUi(self, Tela_Cliente):
        _translate = QtCore.QCoreApplication.translate
        Tela_Cliente.setWindowTitle(_translate("Tela_Cliente", "Operações de Cliente"))
        self.pushButton_listar_clientes.setText(_translate("Tela_Cliente", "Listar Clientes"))
        self.pushButton_obter_cliente.setText(_translate("Tela_Cliente", "Obter Cliente"))
        self.pushButton_cadastrar_cliente.setText(_translate("Tela_Cliente", "Cadastrar Cliente"))
        self.pushButton_atualizar_cliente.setText(_translate("Tela_Cliente", "Atualizar Cliente"))
        self.pushButton_deletar_cliente.setText(_translate("Tela_Cliente", "Deletar Cliente"))

class Tela_Cliente(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Tela_Cliente()
        self.ui.setupUi(self)
        self.setStyleSheet("background-color: #f0f0f0;")  # Definindo o estilo da janela principal
        self.ui.pushButton_cadastrar_cliente.clicked.connect(self.show_cadastro_cliente_window)
        self.ui.pushButton_listar_clientes.clicked.connect(self.show_listar_clientes_window)
        self.ui.pushButton_deletar_cliente.clicked.connect(self.show_deletar_cliente_window)
        self.ui.pushButton_atualizar_cliente.clicked.connect(self.show_atualizar_cliente_window)
        self.ui.pushButton_obter_cliente.clicked.connect(self.show_obter_cliente_window)

        # Variáveis para as janelas secundárias
        self.cadastro_cliente_window = None
        self.listar_clientes_window = None
        self.deletar_cliente_window = None
        self.atualizar_cliente_window = None
        self.obter_cliente_window = None

    def show_cadastro_cliente_window(self):
        if self.cadastro_cliente_window is None:
            self.cadastro_cliente_window = CadastroClienteWindow()
        self.cadastro_cliente_window.show()

    def show_listar_clientes_window(self):
        if self.listar_clientes_window is None:
            self.listar_clientes_window = ListarClientesWindow()
        self.listar_clientes_window.show()

    def show_deletar_cliente_window(self):
        if self.deletar_cliente_window is None:
            self.deletar_cliente_window = DeletarClienteWindow()
        self.deletar_cliente_window.show()

    def show_atualizar_cliente_window(self):
        if self.atualizar_cliente_window is None:
            self.atualizar_cliente_window = AtualizarClienteWindow()
        self.atualizar_cliente_window.show()

    def show_obter_cliente_window(self):
        if self.obter_cliente_window is None:
            self.obter_cliente_window = ClienteObter()
        self.obter_cliente_window.show()

    # Intercepta o evento de fechamento da janela
    def closeEvent(self, event):
        event.ignore()  # Ignora o evento padrão de fechamento
        self.hide()     # Oculta a janela ao invés de fechá-la

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_cliente = Tela_Cliente()
    tela_cliente.show()
    sys.exit(app.exec())
