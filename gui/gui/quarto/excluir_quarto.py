import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QTextEdit, QPushButton, QMessageBox, QListWidget, QListWidgetItem, QHBoxLayout
from PyQt6.QtCore import Qt

class ExcluirQuarto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Excluir Quarto")
        self.setGeometry(100, 100, 600, 400)

        # Widget principal
        widget = QWidget()
        self.setCentralWidget(widget)

        # Layout principal
        layout_principal = QVBoxLayout()
        widget.setLayout(layout_principal)

        # Título
        label_titulo = QLabel("Excluir Quarto", self)
        label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(label_titulo)

        # Lista de quartos
        self.lista_quartos = QListWidget(self)
        layout_principal.addWidget(self.lista_quartos)

        # Botão para selecionar quarto
        btn_selecionar_quarto = QPushButton("Selecionar Quarto", self)
        btn_selecionar_quarto.clicked.connect(self.selecionar_quarto)
        layout_principal.addWidget(btn_selecionar_quarto)

        # Campo de texto para exibir detalhes do quarto selecionado
        self.text_edit_quarto = QTextEdit(self)
        self.text_edit_quarto.setReadOnly(True)
        layout_principal.addWidget(self.text_edit_quarto)

        # Botão para excluir quarto
        btn_excluir_quarto = QPushButton("Excluir Quarto", self)
        btn_excluir_quarto.clicked.connect(self.excluir_quarto)
        layout_principal.addWidget(btn_excluir_quarto)

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

        # Obter o texto completo do item selecionado
        texto_completo = item.text()
        
        # Extrair o ID do quarto do texto
        try:
            quarto_id = int(texto_completo.split("ID: ")[1].split(" ")[0])
        except (IndexError, ValueError):
            QMessageBox.warning(self, "Erro", "Não foi possível extrair o ID do quarto selecionado.")
            return

        # Mostrar detalhes do quarto selecionado no campo de texto
        self.text_edit_quarto.setText(f"ID: {quarto_id}")

    def excluir_quarto(self):
        # Verificar se há um quarto selecionado para excluir
        quarto_id_texto = self.text_edit_quarto.toPlainText()
        if not quarto_id_texto.startswith("ID: "):
            QMessageBox.warning(self, "Seleção Inválida", "Selecione um quarto na lista.")
            return

        # Obter apenas o número do ID do quarto a ser excluído
        quarto_id = int(quarto_id_texto.split("ID: ")[1])

        # Confirmar a exclusão com o usuário
        resposta = QMessageBox.question(self, "Confirmar Exclusão", f"Tem certeza que deseja excluir o quarto ID: {quarto_id}?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if resposta == QMessageBox.StandardButton.Yes:
            # Enviar requisição DELETE para excluir o quarto
            url = f"http://127.0.0.1:5000/api/quartos/{quarto_id}"
            try:
                response = requests.delete(url)
                response.raise_for_status()
                QMessageBox.information(self, "Exclusão", f"Quarto ID: {quarto_id} excluído com sucesso.")
                # Atualizar a lista de quartos após a exclusão
                self.carregar_lista_quartos()
                # Limpar o campo de texto de detalhes do quarto
                self.text_edit_quarto.clear()
            except requests.exceptions.RequestException as e:
                QMessageBox.warning(self, "Erro", f"Erro ao excluir o quarto: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    excluir_quarto = ExcluirQuarto()
    excluir_quarto.show()
    sys.exit(app.exec())
