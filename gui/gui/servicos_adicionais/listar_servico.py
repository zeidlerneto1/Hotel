import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QPushButton, QMessageBox
from PyQt6.QtCore import Qt

class TelaListarServicos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Listar Serviços Adicionais")
        self.setGeometry(100, 100, 500, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout_principal = QVBoxLayout(central_widget)

        self.lista_servicos = QListWidget(self)
        layout_principal.addWidget(self.lista_servicos)

        btn_listar = QPushButton("Listar Serviços", self)
        btn_listar.clicked.connect(self.listar_servicos)
        layout_principal.addWidget(btn_listar)

    def listar_servicos(self):
        self.lista_servicos.clear()
        url = "http://127.0.0.1:5000/api/servicos_adicionais"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                servicos = response.json()
                for servico in servicos:
                    item = f"ID: {servico['id']} - {servico['nome_servico']}"
                    self.lista_servicos.addItem(item)
            else:
                QMessageBox.warning(self, "Erro", "Não foi possível listar os serviços adicionais.")
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Erro de Conexão", f"Erro ao conectar com o servidor: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_listar_servicos = TelaListarServicos()
    tela_listar_servicos.show()
    sys.exit(app.exec())
