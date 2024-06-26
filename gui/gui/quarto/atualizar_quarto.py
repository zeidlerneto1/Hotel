import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QTextEdit, QPushButton, QMessageBox, QListWidget, QListWidgetItem, QHBoxLayout, QInputDialog, QLineEdit
from PyQt6.QtCore import Qt

class AtualizaQuartos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista e Atualiza Quarto")
        self.setGeometry(100, 100, 600, 400)

        # Widget principal
        widget = QWidget()
        self.setCentralWidget(widget)

        # Layout principal
        layout_principal = QVBoxLayout()
        widget.setLayout(layout_principal)

        # Título
        label_titulo = QLabel("Lista e Atualiza Quarto", self)
        label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(label_titulo)

        # Lista de quartos
        self.lista_quartos = QListWidget(self)
        layout_principal.addWidget(self.lista_quartos)

        # Botão para selecionar quarto
        btn_selecionar_quarto = QPushButton("Selecionar Quarto", self)
        btn_selecionar_quarto.clicked.connect(self.selecionar_quarto)
        layout_principal.addWidget(btn_selecionar_quarto)

        # Campo de texto para exibir detalhes do quarto
        self.text_edit_quarto = QTextEdit(self)
        self.text_edit_quarto.setReadOnly(True)
        layout_principal.addWidget(self.text_edit_quarto)

        # Botões para atualizar tipo e status do quarto
        layout_botoes = QHBoxLayout()
        layout_principal.addLayout(layout_botoes)

        btn_atualizar_tipo = QPushButton("Atualizar Tipo", self)
        btn_atualizar_tipo.clicked.connect(self.atualizar_tipo_quarto)
        layout_botoes.addWidget(btn_atualizar_tipo)

        btn_atualizar_status = QPushButton("Atualizar Status", self)
        btn_atualizar_status.clicked.connect(self.atualizar_status_quarto)
        layout_botoes.addWidget(btn_atualizar_status)

        # Carregar lista de quartos
        self.carregar_lista_quartos()

    def carregar_lista_quartos(self):
        url = "http://127.0.0.1:5000/api/quartos"
        try:
            response = requests.get(url)
            response.raise_for_status()
            quartos = response.json()

            # Limpar a lista antes de adicionar os itens
            self.lista_quartos.clear()

            # Adicionar cada quarto à lista
            for quarto in quartos:
                item = QListWidgetItem(f"ID: {quarto['id']} - Tipo: {quarto['tp_quarto']} - Status: {quarto['status_quarto']}")
                item.quarto_id = quarto['id']  # Armazenar o ID do quarto como um atributo do item
                self.lista_quartos.addItem(item)

        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Erro", f"Erro ao carregar a lista de quartos: {str(e)}")

    def selecionar_quarto(self):
        # Obter o item selecionado na lista
        item = self.lista_quartos.currentItem()
        if not item:
            QMessageBox.warning(self, "Seleção Inválida", "Selecione um quarto na lista.")
            return

        # Obter o ID do quarto selecionado
        quarto_id = item.quarto_id

        # Obter dados atuais do quarto selecionado para mostrar no campo de texto
        url = f"http://127.0.0.1:5000/api/quartos/{quarto_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            quarto = response.json()

            # Mostrar dados do quarto no campo de texto
            self.text_edit_quarto.setText(f"ID: {quarto['id']}\n"
                                          f"Tipo: {quarto['tp_quarto']}\n"
                                          f"Status: {quarto['status_quarto']}\n")

            # Atualizar o quarto selecionado
            self.quarto_selecionado = quarto

        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Erro", f"Erro ao obter dados do quarto: {str(e)}")

    def atualizar_tipo_quarto(self):
        if not hasattr(self, 'quarto_selecionado'):
            QMessageBox.warning(self, "Seleção Inválida", "Selecione um quarto na lista antes de atualizar.")
            return

        tp_quarto, ok = QInputDialog.getText(self, "Atualizar Tipo do Quarto", "Novo Tipo do Quarto:")
        if ok:
            self.quarto_selecionado['tp_quarto'] = tp_quarto
            self.atualizar_quarto()

    def atualizar_status_quarto(self):
        if not hasattr(self, 'quarto_selecionado'):
            QMessageBox.warning(self, "Seleção Inválida", "Selecione um quarto na lista antes de atualizar.")
            return

        status_quarto, ok = QInputDialog.getText(self, "Atualizar Status do Quarto", "Novo Status do Quarto:")
        if ok:
            self.quarto_selecionado['status_quarto'] = status_quarto
            self.atualizar_quarto()

    def atualizar_quarto(self):
        quarto_id = self.quarto_selecionado['id']
        dados_atualizados = {
            'tp_quarto': self.quarto_selecionado['tp_quarto'],
            'status_quarto': self.quarto_selecionado['status_quarto']
        }

        url = f"http://127.0.0.1:5000/api/quartos/{quarto_id}"
        try:
            response = requests.put(url, json=dados_atualizados)
            response.raise_for_status()
            self.text_edit_quarto.append("\nDados do Quarto atualizados com sucesso.")
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Erro", f"Erro ao atualizar dados do quarto: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    lista_atualiza_quartos = AtualizaQuartos()
    lista_atualiza_quartos.show()
    sys.exit(app.exec())
