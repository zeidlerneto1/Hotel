import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QTextEdit, QPushButton
from PyQt6.QtCore import Qt

class ListarQuarto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todos os Quartos")
        self.setGeometry(100, 100, 600, 400)

        # Widget principal
        widget = QWidget()
        self.setCentralWidget(widget)

        # Layout principal
        layout_principal = QVBoxLayout()
        widget.setLayout(layout_principal)

        # Título
        label_titulo = QLabel("Lista de Todos os Quartos", self)
        label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(label_titulo)

        # Campo de texto para exibir os dados
        self.text_edit_quartos = QTextEdit(self)
        self.text_edit_quartos.setReadOnly(True)
        layout_principal.addWidget(self.text_edit_quartos)

        # Botão para listar quartos
        self.btn_listar_quartos = QPushButton("Listar Quartos", self)
        self.btn_listar_quartos.clicked.connect(self.listar_quartos)
        layout_principal.addWidget(self.btn_listar_quartos)

    def listar_quartos(self):
        url = "http://127.0.0.1:5000/api/quartos"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Lança uma exceção se o código de status não for 2xx
            quartos = response.json()
            if isinstance(quartos, list):
                # Limpa o campo de texto antes de adicionar os novos dados
                self.text_edit_quartos.clear()
                for quarto in quartos:
                    quarto_id = quarto.get('id', 'ID não especificado')
                    tp_quarto = quarto.get('tp_quarto', 'Tipo não especificado')
                    status_quarto = quarto.get('status_quarto', 'Status não especificado')
                    self.text_edit_quartos.append(f"ID: {quarto_id}, Tipo de Quarto: {tp_quarto}, Status do Quarto: {status_quarto}")
            else:
                self.text_edit_quartos.setText("Não há quartos disponíveis.")
        except requests.exceptions.RequestException as e:
            self.text_edit_quartos.setText(f"Erro ao obter os quartos: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_quartos = ListarQuarto()
    tela_quartos.show()
    sys.exit(app.exec())
