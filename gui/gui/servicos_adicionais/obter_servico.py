import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLineEdit, QLabel
from PyQt6.QtCore import Qt

class ObterServicoAdicional(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Obter Serviço Adicional")
        self.setGeometry(100, 100, 400, 300)
        self.setFixedSize(400, 300)  # Fixa o tamanho da janela

        # Label e campo de entrada para o ID do serviço adicional
        self.label_id = QLineEdit(self)
        self.label_id.setPlaceholderText("ID do Serviço Adicional")
        self.label_id.setGeometry(50, 30, 300, 30)

        # Botão para obter o serviço adicional
        btn_obter = QPushButton("Obter Serviço", self)
        btn_obter.setGeometry(50, 80, 300, 40)
        btn_obter.clicked.connect(self.obter_servico)

        # Label para exibir os dados do serviço adicional
        self.text_edit_servico = QLabel(self)
        self.text_edit_servico.setGeometry(50, 140, 300, 120)
        self.text_edit_servico.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.text_edit_servico.setWordWrap(True)
        self.text_edit_servico.setStyleSheet("background-color: white; border: 1px solid black; padding: 10px;")

    def obter_servico(self):
        servico_id = self.label_id.text()
        if not servico_id:
            QMessageBox.warning(self, "Erro", "Informe o ID do serviço adicional.")
            return

        url = f"http://127.0.0.1:5000/api/servicos_adicionais/{servico_id}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                servico = response.json()
                self.mostrar_dados(servico)
            else:
                QMessageBox.warning(self, "Erro", f"Não foi possível obter o serviço adicional com ID {servico_id}.")
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Erro de Conexão", f"Erro ao conectar com o servidor: {str(e)}")

    def mostrar_dados(self, servico):
        id_servico = servico.get('id', '')
        nome_servico = servico.get('nome_servico', '')
        descricao = servico.get('descricao', '')
        preco = servico.get('preco', '')
        id_reserva = servico.get('id_reserva', '')

        texto = f"<b>ID:</b> {id_servico}<br>"
        texto += f"<b>Nome:</b> {nome_servico}<br>"
        texto += f"<b>Descrição:</b> {descricao}<br>"
        texto += f"<b>Preço:</b> R$ {preco}<br>"
        texto += f"<b>ID da Reserva:</b> {id_reserva}<br>"

        self.text_edit_servico.setText(texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_obter_servico = ObterServicoAdicional()
    tela_obter_servico.show()
    sys.exit(app.exec())
