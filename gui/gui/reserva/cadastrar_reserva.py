import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class CadastroReservaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cadastro de Reserva')
        self.setGeometry(100, 100, 400, 400)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label_id_quarto = QLabel('ID do Quarto:')
        self.input_id_quarto = QLineEdit()
        self.layout.addWidget(self.label_id_quarto)
        self.layout.addWidget(self.input_id_quarto)

        self.label_id_cliente = QLabel('ID do Cliente:')
        self.input_id_cliente = QLineEdit()
        self.layout.addWidget(self.label_id_cliente)
        self.layout.addWidget(self.input_id_cliente)

        self.label_data_checkin = QLabel('Data de Check-In:')
        self.input_data_checkin = QLineEdit()
        self.layout.addWidget(self.label_data_checkin)
        self.layout.addWidget(self.input_data_checkin)

        self.label_data_checkout = QLabel('Data de Check-Out:')
        self.input_data_checkout = QLineEdit()
        self.layout.addWidget(self.label_data_checkout)
        self.layout.addWidget(self.input_data_checkout)

        self.label_status_reserva = QLabel('Status da Reserva:')
        self.input_status_reserva = QLineEdit()
        self.layout.addWidget(self.label_status_reserva)
        self.layout.addWidget(self.input_status_reserva)

        self.label_custo_adicional = QLabel('Custo Adicional:')
        self.input_custo_adicional = QLineEdit()
        self.layout.addWidget(self.label_custo_adicional)
        self.layout.addWidget(self.input_custo_adicional)

        self.label_custo_total = QLabel('Custo Total:')
        self.input_custo_total = QLineEdit()
        self.layout.addWidget(self.label_custo_total)
        self.layout.addWidget(self.input_custo_total)

        self.btn_cadastrar = QPushButton('Cadastrar')
        self.btn_cadastrar.clicked.connect(self.cadastrar_reserva)
        self.layout.addWidget(self.btn_cadastrar)

        self.setLayout(self.layout)

    def cadastrar_reserva(self):
        url = 'http://127.0.0.1:5000/api/reservas'
        headers = {'Content-Type': 'application/json'}

        data = {
            'id_quarto': int(self.input_id_quarto.text()),
            'id_cliente': int(self.input_id_cliente.text()),
            'data_checkin': self.input_data_checkin.text(),
            'data_checkout': self.input_data_checkout.text(),
            'status_reserva': self.input_status_reserva.text(),
            'custo_adicional': float(self.input_custo_adicional.text()),
            'custo_total': float(self.input_custo_total.text())
        }

        try:
            response = requests.post(url, json=data, headers=headers)

            if response.status_code == 201:
                QMessageBox.information(self, 'Cadastro de Reserva', 'Reserva cadastrada com sucesso!')
                self.limpar_campos()
            else:
                QMessageBox.warning(self, 'Cadastro de Reserva', f'Erro ao cadastrar reserva: {response.status_code}')
        
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'Erro de Conexão', f'Erro ao conectar à API: {str(e)}')

    def limpar_campos(self):
        self.input_id_quarto.clear()
        self.input_id_cliente.clear()
        self.input_data_checkin.clear()
        self.input_data_checkout.clear()
        self.input_status_reserva.clear()
        self.input_custo_adicional.clear()
        self.input_custo_total.clear()


def main():
    app = QApplication(sys.argv)
    window = CadastroReservaWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
