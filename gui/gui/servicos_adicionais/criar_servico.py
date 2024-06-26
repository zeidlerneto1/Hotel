import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QMessageBox

class TelaCriarServicoAdicional(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criar Serviço Adicional")
        self.setGeometry(100, 100, 400, 250)

        self.label_nome = QLineEdit(self)
        self.label_nome.setPlaceholderText("Nome do Serviço")
        self.label_nome.setGeometry(50, 30, 300, 30)

        self.label_descricao = QLineEdit(self)
        self.label_descricao.setPlaceholderText("Descrição do Serviço")
        self.label_descricao.setGeometry(50, 80, 300, 30)

        self.label_preco = QLineEdit(self)
        self.label_preco.setPlaceholderText("Preço do Serviço")
        self.label_preco.setGeometry(50, 130, 300, 30)

        self.label_id_reserva = QLineEdit(self)
        self.label_id_reserva.setPlaceholderText("ID da Reserva")
        self.label_id_reserva.setGeometry(50, 180, 300, 30)

        btn_criar = QPushButton("Criar Serviço", self)
        btn_criar.setGeometry(50, 230, 150, 40)
        btn_criar.clicked.connect(self.criar_servico)

    def criar_servico(self):
        nome = self.label_nome.text()
        descricao = self.label_descricao.text()
        preco = self.label_preco.text()
        id_reserva = self.label_id_reserva.text()

        if not nome or not descricao or not preco or not id_reserva:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        try:
            preco = float(preco)
            id_reserva = int(id_reserva)
        except ValueError:
            QMessageBox.warning(self, "Erro", "O preço deve ser um valor numérico e o ID da reserva um número inteiro.")
            return

        data = {
            'nome_servico': nome,
            'descricao': descricao,
            'preco': preco,
            'id_reserva': id_reserva
        }
        url = "http://127.0.0.1:5000/api/servicos_adicionais"
        try:
            response = requests.post(url, json=data)
            print(f"Status Code da Resposta: {response.status_code}")  # Debug: Verifica o status code da resposta
            if response.status_code == 201:
                QMessageBox.information(self, "Sucesso", "Serviço adicional criado com sucesso.")
                self.limpar_campos()
            else:
                QMessageBox.warning(self, "Erro", f"Não foi possível criar o serviço adicional. Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Erro de Conexão", f"Erro ao conectar com o servidor: {str(e)}")

    def limpar_campos(self):
        self.label_nome.clear()
        self.label_descricao.clear()
        self.label_preco.clear()
        self.label_id_reserva.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_criar_servico = TelaCriarServicoAdicional()
    tela_criar_servico.show()
    sys.exit(app.exec())
