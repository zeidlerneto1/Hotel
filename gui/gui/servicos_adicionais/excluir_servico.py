import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QPushButton, QMessageBox
from PyQt6.QtCore import Qt

class TelaExcluirServico(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Excluir Serviço Adicional")
        self.setGeometry(100, 100, 500, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout_principal = QVBoxLayout(central_widget)

        self.lista_servicos = QListWidget(self)
        layout_principal.addWidget(self.lista_servicos)

        btn_listar = QPushButton("Listar Serviços", self)
        btn_listar.clicked.connect(self.listar_servicos)
        layout_principal.addWidget(btn_listar)

        btn_excluir = QPushButton("Excluir Serviço", self)
        btn_excluir.clicked.connect(self.excluir_servico)
        layout_principal.addWidget(btn_excluir)

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

    def excluir_servico(self):
        item_selecionado = self.lista_servicos.currentItem()
        if item_selecionado:
            servico_id = int(item_selecionado.text().split()[1])  # Extrai o ID do serviço selecionado
            url = f"http://127.0.0.1:5000/api/servicos_adicionais/{servico_id}"
            try:
                response = requests.delete(url)
                if response.status_code == 200:
                    QMessageBox.information(self, "Sucesso", f"Serviço adicional {servico_id} excluído com sucesso.")
                    self.listar_servicos()  # Atualiza a lista após exclusão
                else:
                    QMessageBox.warning(self, "Erro", f"Não foi possível excluir o serviço adicional {servico_id}. Código HTTP: {response.status_code}")
            except requests.exceptions.RequestException as e:
                QMessageBox.warning(self, "Erro de Conexão", f"Erro ao conectar com o servidor: {str(e)}")
        else:
            QMessageBox.warning(self, "Seleção Inválida", "Selecione um serviço adicional para excluir.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_excluir_servico = TelaExcluirServico()
    tela_excluir_servico.show()
    sys.exit(app.exec())
