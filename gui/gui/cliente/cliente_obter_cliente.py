import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox

class ClienteApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Consulta de Cliente')
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Digite o nome do cliente')
        self.layout.addWidget(self.name_input)

        self.search_button = QPushButton('Buscar', self)
        self.search_button.clicked.connect(self.buscar_cliente)
        self.layout.addWidget(self.search_button)

        self.result_label = QLabel('Resultados:', self)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def buscar_cliente(self):
        nome = self.name_input.text()
        if not nome:
            QMessageBox.warning(self, 'Erro', 'Por favor, digite o nome do cliente')
            return

        # Primeira busca por nome
        url = f'http://127.0.0.1:5000/api/clientes?nome={nome}'
        response = requests.get(url)

        if response.status_code == 200:
            clientes = response.json()
            if isinstance(clientes, dict):
                clientes = [clientes]  # Garante que seja uma lista, mesmo se um único cliente for retornado.

            if clientes:
                # Pega o ID do primeiro cliente encontrado
                cliente_id = clientes[0]['id']
                # Busca os detalhes completos do cliente pelo ID
                self.buscar_cliente_por_id(cliente_id)
            else:
                self.result_label.setText('Cliente não encontrado.')
        else:
            QMessageBox.critical(self, 'Erro', 'Erro ao buscar o cliente')

    def buscar_cliente_por_id(self, cliente_id):
        url = f'http://127.0.0.1:5000/api/clientes/{cliente_id}'
        response = requests.get(url)

        if response.status_code == 200:
            cliente = response.json()
            resultados = self.formatar_cliente(cliente)
            self.result_label.setText(resultados)
        else:
            QMessageBox.critical(self, 'Erro', 'Erro ao buscar os detalhes do cliente')

    def formatar_cliente(self, cliente):
        cliente_formatado = []
        if 'id' in cliente:
            cliente_formatado.append(f"ID: {cliente['id']}")
        if 'nome' in cliente:
            cliente_formatado.append(f"Nome: {cliente['nome']}")
        if 'endereco' in cliente:
            cliente_formatado.append(f"Endereço: {cliente['endereco']}")
        if 'telefone' in cliente:
            cliente_formatado.append(f"Telefone: {cliente['telefone']}")
        if 'email' in cliente:
            cliente_formatado.append(f"Email: {cliente['email']}")
        if 'documento_RG_cliente' in cliente:
            cliente_formatado.append(f"Documento RG: {cliente['documento_RG_cliente']}")
        return "\n".join(cliente_formatado)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ClienteApp()
    ex.show()
    sys.exit(app.exec())
