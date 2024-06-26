import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QTextEdit, QPushButton, QMessageBox, QLineEdit
from PyQt6.QtCore import Qt


class CriaQuarto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criar Quarto")
        self.setGeometry(100, 100, 600, 400)

        # Widget principal
        widget = QWidget()
        self.setCentralWidget(widget)

        # Layout principal
        layout_principal = QVBoxLayout()
        widget.setLayout(layout_principal)

        # Título
        label_titulo = QLabel("Criar Novo Quarto", self)
        label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(label_titulo)

        # Campos para tipo e status do quarto
        self.input_tp_quarto = QLineEdit(self)
        self.input_tp_quarto.setPlaceholderText("Tipo do Quarto (ex: Standard)")
        layout_principal.addWidget(self.input_tp_quarto)

        self.input_status_quarto = QLineEdit(self)
        self.input_status_quarto.setPlaceholderText("Status do Quarto (ex: Disponível)")
        layout_principal.addWidget(self.input_status_quarto)

        # Campo de texto para exibir mensagens
        self.text_edit_quarto = QTextEdit(self)
        self.text_edit_quarto.setReadOnly(True)
        layout_principal.addWidget(self.text_edit_quarto)

        # Botão para criar quarto
        self.btn_criar_quarto = QPushButton("Criar Quarto", self)
        self.btn_criar_quarto.clicked.connect(self.criar_quarto)
        layout_principal.addWidget(self.btn_criar_quarto)

    def criar_quarto(self):
        # Obter os dados dos campos de entrada
        tp_quarto = self.input_tp_quarto.text().strip()
        status_quarto = self.input_status_quarto.text().strip()

        # Validar se os campos estão preenchidos
        if not tp_quarto or not status_quarto:
            QMessageBox.warning(self, "Campos Vazios", "Por favor, preencha todos os campos.")
            return

        # Dados do quarto para criar
        dados_quarto = {
            'tp_quarto': tp_quarto,
            'status_quarto': status_quarto
        }

        url_post_quarto = "http://127.0.0.1:5000/api/quartos"
        try:
            response = requests.post(url_post_quarto, json=dados_quarto)
            response.raise_for_status()
            self.text_edit_quarto.setText("Quarto criado com sucesso!")
        except requests.exceptions.RequestException as e:
            self.text_edit_quarto.setText(f"Erro ao criar o quarto: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cria_quarto = CriaQuarto()
    cria_quarto.show()
    sys.exit(app.exec())
