import sys
import requests
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,
    QFormLayout, QMessageBox, QSizePolicy
)

class DeletarClienteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Deletar Cliente')
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        # Layout principal
        self.layout_principal = QHBoxLayout()

        # Layout para a lista de clientes à esquerda
        self.layout_lista = QVBoxLayout()
        
        self.label_lista = QLabel('Lista de Clientes')
        self.lista_clientes = QListWidget()
        self.lista_clientes.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.lista_clientes.itemClicked.connect(self.exibir_dados_cliente)
        
        self.layout_lista.addWidget(self.label_lista)
        self.layout_lista.addWidget(self.lista_clientes)

        # Layout para os dados do cliente à direita
        self.layout_dados = QVBoxLayout()
        
        self.label_dados = QLabel('Dados do Cliente')
        self.layout_dados.addWidget(self.label_dados)

        self.form_layout = QFormLayout()
        
        self.label_id = QLabel('ID:')
        self.input_id = QLineEdit()
        self.input_id.setReadOnly(True)
        self.form_layout.addRow(self.label_id, self.input_id)

        self.label_nome = QLabel('Nome:')
        self.input_nome = QLineEdit()
        self.form_layout.addRow(self.label_nome, self.input_nome)

        self.label_endereco = QLabel('Endereço:')
        self.input_endereco = QLineEdit()
        self.form_layout.addRow(self.label_endereco, self.input_endereco)

        self.label_telefone = QLabel('Telefone:')
        self.input_telefone = QLineEdit()
        self.form_layout.addRow(self.label_telefone, self.input_telefone)

        self.label_email = QLabel('Email:')
        self.input_email = QLineEdit()
        self.form_layout.addRow(self.label_email, self.input_email)

        self.label_documento = QLabel('Documento (RG):')
        self.input_documento = QLineEdit()
        self.form_layout.addRow(self.label_documento, self.input_documento)
        
        self.layout_dados.addLayout(self.form_layout)
        
        # Botão para deletar cliente
        self.btn_deletar = QPushButton('Deletar Cliente')
        self.btn_deletar.clicked.connect(self.deletar_cliente)
        self.layout_dados.addWidget(self.btn_deletar)

        # Adicionar layouts principais à janela
        self.layout_principal.addLayout(self.layout_lista)
        self.layout_principal.addLayout(self.layout_dados)

        self.setLayout(self.layout_principal)

        # Inicializar a lista de clientes
        self.carregar_lista_clientes()

    def carregar_lista_clientes(self):
        try:
            url = 'http://127.0.0.1:5000/api/clientes'
            response = requests.get(url)
            clientes = response.json()

            self.lista_clientes.clear()  # Limpar a lista de clientes antes de carregar novamente

            for cliente in clientes:
                item = QListWidgetItem(cliente['nome'])
                item.setData(1, cliente)  # Armazenar dados completos do cliente como data do item
                self.lista_clientes.addItem(item)

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'Erro de Conexão', f'Erro ao conectar à API: {str(e)}')

    def exibir_dados_cliente(self, item):
        cliente = item.data(1)  # Recuperar dados do cliente armazenados no item
        self.input_id.setText(str(cliente['id']))
        self.input_nome.setText(cliente['nome'])
        self.input_endereco.setText(cliente['endereco'])
        self.input_telefone.setText(cliente['telefone'])
        self.input_email.setText(cliente['email'])
        self.input_documento.setText(cliente['documento_RG_cliente'])

    def deletar_cliente(self):
        cliente_id = self.input_id.text()
        nome_cliente = self.input_nome.text().strip()

        if not nome_cliente:
            QMessageBox.warning(self, 'Deletar Cliente', 'Por favor, selecione um cliente da lista.')
            return

        confirmacao = QMessageBox.question(self, 'Deletar Cliente', f'Deseja realmente deletar o cliente {nome_cliente}?',
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmacao == QMessageBox.StandardButton.Yes:
            url = f'http://127.0.0.1:5000/api/clientes/{cliente_id}'

            try:
                response = requests.delete(url)

                if response.status_code == 200:
                    QMessageBox.information(self, 'Deletar Cliente', 'Cliente deletado com sucesso!')
                    self.limpar_campos()
                    self.carregar_lista_clientes()  # Atualizar a lista de clientes após a exclusão
                else:
                    QMessageBox.warning(self, 'Deletar Cliente', f'Erro ao deletar cliente: {response.status_code}')

            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, 'Erro de Conexão', f'Erro ao conectar à API: {str(e)}')

    def limpar_campos(self):
        self.input_id.clear()
        self.input_nome.clear()
        self.input_endereco.clear()
        self.input_telefone.clear()
        self.input_email.clear()
        self.input_documento.clear()


def main():
    app = QApplication(sys.argv)
    window = DeletarClienteWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
