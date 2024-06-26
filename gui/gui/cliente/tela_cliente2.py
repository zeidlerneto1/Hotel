import sys
import requests
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox
)
from PyQt6 import QtCore, QtGui, QtWidgets

class CadastroClienteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cadastro de Clientes')
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label_nome = QLabel('Nome:')
        self.input_nome = QLineEdit()
        self.layout.addWidget(self.label_nome)
        self.layout.addWidget(self.input_nome)

        self.label_endereco = QLabel('Endereço:')
        self.input_endereco = QLineEdit()
        self.layout.addWidget(self.label_endereco)
        self.layout.addWidget(self.input_endereco)

        self.label_telefone = QLabel('Telefone:')
        self.input_telefone = QLineEdit()
        self.layout.addWidget(self.label_telefone)
        self.layout.addWidget(self.input_telefone)

        self.label_email = QLabel('Email:')
        self.input_email = QLineEdit()
        self.layout.addWidget(self.label_email)
        self.layout.addWidget(self.input_email)

        self.label_documento = QLabel('Documento (RG):')
        self.input_documento = QLineEdit()
        self.layout.addWidget(self.label_documento)
        self.layout.addWidget(self.input_documento)

        self.btn_cadastrar = QPushButton('Cadastrar')
        self.btn_cadastrar.clicked.connect(self.cadastrar_cliente)
        self.layout.addWidget(self.btn_cadastrar)

        self.setLayout(self.layout)

    def cadastrar_cliente(self):
        url = 'http://127.0.0.1:5000/api/clientes'
        headers = {'Content-Type': 'application/json'}

        data = {
            'nome': self.input_nome.text(),
            'endereco': self.input_endereco.text(),
            'telefone': self.input_telefone.text(),
            'email': self.input_email.text(),
            'documento_RG_cliente': self.input_documento.text()
        }

        try:
            response = requests.post(url, json=data, headers=headers)

            if response.status_code == 201:
                QMessageBox.information(self, 'Cadastro de Cliente', 'Cliente cadastrado com sucesso!')
                self.limpar_campos()
            else:
                QMessageBox.warning(self, 'Cadastro de Cliente', f'Erro ao cadastrar cliente: {response.status_code}')

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'Erro de Conexão', f'Erro ao conectar à API: {str(e)}')

    def limpar_campos(self):
        self.input_nome.clear()
        self.input_endereco.clear()
        self.input_telefone.clear()
        self.input_email.clear()
        self.input_documento.clear()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Operações de Cliente"))
        self.pushButton_listar_clientes.setText(_translate("MainWindow", "Listar Clientes"))
        self.pushButton_obter_cliente.setText(_translate("MainWindow", "Obter Cliente"))
        self.pushButton_cadastrar_cliente.setText(_translate("MainWindow", "Cadastrar Cliente"))
        self.pushButton_atualizar_cliente.setText(_translate("MainWindow", "Atualizar Cliente"))
        self.pushButton_deletar_cliente.setText(_translate("MainWindow", "Deletar Cliente"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet("background-color: #f0f0f0;")  # Definindo o estilo da janela principal
        self.ui.pushButton_cadastrar_cliente.clicked.connect(self.show_cadastro_cliente_window)
        self.cadastro_cliente_window = None

    def show_cadastro_cliente_window(self):
        if self.cadastro_cliente_window is None:
            self.cadastro_cliente_window = CadastroClienteWindow()
        self.cadastro_cliente_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
