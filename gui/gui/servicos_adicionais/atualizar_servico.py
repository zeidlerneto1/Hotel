import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget, QVBoxLayout, QWidget, QLineEdit, QMessageBox, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt

class TelaAtualizarServicoAdicional(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atualizar Serviço Adicional")
        self.setGeometry(100, 100, 500, 500)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout_principal = QVBoxLayout(central_widget)

        self.lista_servicos = QListWidget(self)
        layout_principal.addWidget(self.lista_servicos)

        form_layout = QVBoxLayout()

        self.label_nome = QLineEdit(self)
        self.label_nome.setPlaceholderText("Novo Nome do Serviço")
        form_layout.addWidget(self.label_nome)

        self.label_descricao = QLineEdit(self)
        self.label_descricao.setPlaceholderText("Nova Descrição do Serviço")
        form_layout.addWidget(self.label_descricao)

        self.label_preco = QLineEdit(self)
        self.label_preco.setPlaceholderText("Novo Preço do Serviço")
        form_layout.addWidget(self.label_preco)

        layout_principal.addLayout(form_layout)

        btn_carregar = QPushButton(QIcon("carregar.png"), "Carregar Serviço", self)
        btn_carregar.clicked.connect(self.carregar_servico)
        layout_principal.addWidget(btn_carregar)

        btn_atualizar = QPushButton(QIcon("atualizar.png"), "Atualizar Serviço", self)
        btn_atualizar.clicked.connect(self.atualizar_servico)
        layout_principal.addWidget(btn_atualizar)

        self.carregar_lista_servicos()

    def carregar_lista_servicos(self):
        self.lista_servicos.clear()
        url = "http://127.0.0.1:5000/api/servicos_adicionais"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                servicos = response.json()
                for servico in servicos:
                    self.lista_servicos.addItem(f"ID: {servico['id']} - {servico['nome_servico']}")
            else:
                QMessageBox.warning(self, "Erro", "Não foi possível carregar os serviços adicionais.")
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Erro de Conexão", f"Erro ao conectar com o servidor: {str(e)}")

    def carregar_servico(self):
        item_selecionado = self.lista_servicos.currentItem()
        if item_selecionado:
            servico_id = int(item_selecionado.text().split()[1])  # Extrai o ID do serviço selecionado
            url = f"http://127.0.0.1:5000/api/servicos_adicionais/{servico_id}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    servico = response.json()
                    self.label_nome.setText(servico['nome_servico'])
                    self.label_descricao.setText(servico['descricao'])
                    self.label_preco.setText(str(servico['preco']))
                else:
                    QMessageBox.warning(self, "Erro", f"Não foi possível carregar o serviço adicional {servico_id}.")
            except requests.exceptions.RequestException as e:
                QMessageBox.warning(self, "Erro de Conexão", f"Erro ao conectar com o servidor: {str(e)}")

    def atualizar_servico(self):
        item_selecionado = self.lista_servicos.currentItem()
        if item_selecionado:
            servico_id = int(item_selecionado.text().split()[1])  # Extrai o ID do serviço selecionado
            novo_nome = self.label_nome.text()
            nova_descricao = self.label_descricao.text()
            novo_preco = self.label_preco.text()

            if not novo_nome or not nova_descricao or not novo_preco:
                QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
                return

            try:
                novo_preco = float(novo_preco)
            except ValueError:
                QMessageBox.warning(self, "Erro", "O preço deve ser um valor numérico.")
                return

            data = {
                'nome_servico': novo_nome,
                'descricao': nova_descricao,
                'preco': novo_preco
            }
            url = f"http://127.0.0.1:5000/api/servicos_adicionais/{servico_id}"
            try:
                response = requests.put(url, json=data)
                if response.status_code == 200:
                    QMessageBox.information(self, "Sucesso", f"Serviço adicional {servico_id} atualizado com sucesso.")
                    self.limpar_campos()
                    self.carregar_lista_servicos()
                else:
                    QMessageBox.warning(self, "Erro", f"Não foi possível atualizar o serviço adicional {servico_id}.")
            except requests.exceptions.RequestException as e:
                QMessageBox.warning(self, "Erro de Conexão", f"Erro ao conectar com o servidor: {str(e)}")

    def limpar_campos(self):
        self.label_nome.clear()
        self.label_descricao.clear()
        self.label_preco.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Estilo para os botões
    app.setStyle("Fusion")
    font = QFont()
    font.setPointSize(12)
    app.setFont(font)

    tela_atualizar_servico = TelaAtualizarServicoAdicional()
    tela_atualizar_servico.show()
    sys.exit(app.exec())
