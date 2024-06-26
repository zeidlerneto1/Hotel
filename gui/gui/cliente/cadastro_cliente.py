import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

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


def main():
    app = QApplication(sys.argv)
    window = CadastroClienteWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
