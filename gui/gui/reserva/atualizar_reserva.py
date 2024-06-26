import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class AtualizarReservaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Atualizar Reserva')
        self.setGeometry(100, 100, 400, 400)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label_id_reserva = QLabel('ID da Reserva:', self)
        self.input_id_reserva = QLineEdit(self)
        self.layout.addWidget(self.label_id_reserva)
        self.layout.addWidget(self.input_id_reserva)

        self.label_id_quarto = QLabel('Novo ID do Quarto:', self)
        self.input_id_quarto = QLineEdit(self)
        self.layout.addWidget(self.label_id_quarto)
        self.layout.addWidget(self.input_id_quarto)

        self.label_id_cliente = QLabel('Novo ID do Cliente:', self)
        self.input_id_cliente = QLineEdit(self)
        self.layout.addWidget(self.label_id_cliente)
        self.layout.addWidget(self.input_id_cliente)

        self.label_data_checkin = QLabel('Nova Data de Check-In:', self)
        self.input_data_checkin = QLineEdit(self)
        self.layout.addWidget(self.label_data_checkin)
        self.layout.addWidget(self.input_data_checkin)

        self.label_data_checkout = QLabel('Nova Data de Check-Out:', self)
        self.input_data_checkout = QLineEdit(self)
        self.layout.addWidget(self.label_data_checkout)
        self.layout.addWidget(self.input_data_checkout)

        self.label_status_reserva = QLabel('Novo Status da Reserva:', self)
        self.input_status_reserva = QLineEdit(self)
        self.layout.addWidget(self.label_status_reserva)
        self.layout.addWidget(self.input_status_reserva)

        self.label_custo_adicional = QLabel('Novo Custo Adicional:', self)
        self.input_custo_adicional = QLineEdit(self)
        self.layout.addWidget(self.label_custo_adicional)
        self.layout.addWidget(self.input_custo_adicional)

        self.label_custo_total = QLabel('Novo Custo Total:', self)
        self.input_custo_total = QLineEdit(self)
        self.layout.addWidget(self.label_custo_total)
        self.layout.addWidget(self.input_custo_total)

        self.btn_atualizar = QPushButton('Atualizar Reserva', self)
        self.btn_atualizar.clicked.connect(self.atualizar_reserva)
        self.layout.addWidget(self.btn_atualizar)

        self.setLayout(self.layout)

    def atualizar_reserva(self):
        reserva_id = self.input_id_reserva.text().strip()
        url = f'http://127.0.0.1:5000/api/reservas/{reserva_id}'
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
            response = requests.put(url, json=data, headers=headers)

            if response.status_code == 200:
                QMessageBox.information(self, 'Atualização de Reserva', 'Reserva atualizada com sucesso!')
                self.limpar_campos()
            else:
                QMessageBox.warning(self, 'Atualização de Reserva', f'Erro ao atualizar reserva: {response.status_code}')
        
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'Erro de Conexão', f'Erro ao conectar à API: {str(e)}')

    def limpar_campos(self):
        self.input_id_reserva.clear()
        self.input_id_quarto.clear()
        self.input_id_cliente.clear()
        self.input_data_checkin.clear()
        self.input_data_checkout.clear()
        self.input_status_reserva.clear()
        self.input_custo_adicional.clear()
        self.input_custo_total.clear()

def main():
    app = QApplication(sys.argv)
    window = AtualizarReservaWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
