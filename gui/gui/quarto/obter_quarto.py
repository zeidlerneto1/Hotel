import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QTextEdit, QPushButton, QInputDialog
from PyQt6.QtCore import Qt

class ObterQuarto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operações de Quarto")
        self.setGeometry(100, 100, 600, 400)

        # Widget principal
        widget = QWidget()
        self.setCentralWidget(widget)

        # Layout principal
        layout_principal = QVBoxLayout()
        widget.setLayout(layout_principal)

        # Título
        label_titulo = QLabel("Operações de Quarto", self)
        label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(label_titulo)

        # Campo de texto para exibir os dados
        self.text_edit_quarto = QTextEdit(self)
        self.text_edit_quarto.setReadOnly(True)
        layout_principal.addWidget(self.text_edit_quarto)

        # Botão para obter quarto
        self.btn_obter_quarto = QPushButton("Obter Quarto", self)
        self.btn_obter_quarto.clicked.connect(self.obter_quarto)
        layout_principal.addWidget(self.btn_obter_quarto)

    def obter_quarto(self):
        quarto_id, ok = QInputDialog.getInt(self, "Obter Quarto", "ID do Quarto:")
        if ok:
            url = f"http://127.0.0.1:5000/api/quartos/{quarto_id}"
            try:
                response = requests.get(url)
                response.raise_for_status()  # Lança uma exceção se o código de status não for 2xx
                quarto = response.json()
                if isinstance(quarto, dict):
                    quarto_id = quarto.get('id', 'ID não especificado')
                    tp_quarto = quarto.get('tp_quarto', 'Tipo não especificado')
                    status_quarto = quarto.get('status_quarto', 'Status não especificado')
                    self.text_edit_quarto.setText(f"ID: {quarto_id}\nTipo de Quarto: {tp_quarto}\nStatus do Quarto: {status_quarto}")
                else:
                    self.text_edit_quarto.setText(f"Não foi possível encontrar o quarto com ID {quarto_id}.")
            except requests.exceptions.RequestException as e:
                self.text_edit_quarto.setText(f"Erro ao obter o quarto: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_quarto = ObterQuarto()
    tela_quarto.show()
    sys.exit(app.exec())
