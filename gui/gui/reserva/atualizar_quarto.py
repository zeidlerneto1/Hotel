import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class AtualizarQuartoReservaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Atualizar Quarto da Reserva')
        self.setGeometry(100, 100, 400, 300)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label_id_reserva = QLabel('ID da Reserva:', self)
        self.input_id_reserva = QLineEdit(self)
        self.layout.addWidget(self.label_id_reserva)
        self.layout.addWidget(self.input_id_reserva)

        self.label_novo_id_quarto = QLabel('Novo ID do Quarto:', self)
        self.input_novo_id_quarto = QLineEdit(self)
        self.layout.addWidget(self.label_novo_id_quarto)
        self.layout.addWidget(self.input_novo_id_quarto)

        self.label_custo_adicional = QLabel('Custo Adicional:', self)
        self.input_custo_adicional = QLineEdit(self)
        self.layout.addWidget(self.label_custo_adicional)
        self.layout.addWidget(self.input_custo_adicional)

        self.btn_atualizar = QPushButton('Atualizar Quarto da Reserva', self)
        self.btn_atualizar.clicked.connect(self.atualizar_quarto_reserva)
        self.layout.addWidget(self.btn_atualizar)

        self.setLayout(self.layout)

    def atualizar_quarto_reserva(self):
        reserva_id = self.input_id_reserva.text().strip()
        novo_quarto_id = self.input_novo_id_quarto.text().strip()
        custo_adicional = float(self.input_custo_adicional.text().strip())

        if not reserva_id or not novo_quarto_id:
            QMessageBox.warning(self, 'Atualizar Quarto da Reserva', 'Por favor, preencha todos os campos.')
            return

        url = f'http://127.0.0.1:5000/api/reservas/{reserva_id}/atualizar_quarto'
        headers = {'Content-Type': 'application/json'}

        data = {
            'novo_quarto_id': int(novo_quarto_id),
            'custo_adicional': custo_adicional
        }

        try:
            response = requests.put(url, json=data, headers=headers)

            if response.status_code == 200:
                QMessageBox.information(self, 'Atualizar Quarto da Reserva', 'Quarto da reserva atualizado com sucesso!')
                self.limpar_campos()
            else:
                QMessageBox.warning(self, 'Atualizar Quarto da Reserva', f'Erro ao atualizar quarto da reserva: {response.status_code}')
        
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'Erro de Conexão', f'Erro ao conectar à API: {str(e)}')

    def limpar_campos(self):
        self.input_id_reserva.clear()
        self.input_novo_id_quarto.clear()
        self.input_custo_adicional.clear()

def main():
    app = QApplication(sys.argv)
    window = AtualizarQuartoReservaWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
