import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
from datetime import datetime

class VerificarDisponibilidadeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Verificar Disponibilidade de Quartos')
        self.setGeometry(100, 100, 600, 400)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label_data_entrada = QLabel('Data de Entrada (YYYY-MM-DD):', self)
        self.input_data_entrada = QLineEdit(self)
        self.layout.addWidget(self.label_data_entrada)
        self.layout.addWidget(self.input_data_entrada)

        self.label_data_saida = QLabel('Data de Saída (YYYY-MM-DD):', self)
        self.input_data_saida = QLineEdit(self)
        self.layout.addWidget(self.label_data_saida)
        self.layout.addWidget(self.input_data_saida)

        self.btn_verificar = QPushButton('Verificar Disponibilidade', self)
        self.btn_verificar.clicked.connect(self.verificar_disponibilidade)
        self.layout.addWidget(self.btn_verificar)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['ID do Quarto', 'Status'])
        self.layout.addWidget(self.tableWidget)

        self.setLayout(self.layout)

    def verificar_disponibilidade(self):
        data_entrada = self.input_data_entrada.text().strip()
        data_saida = self.input_data_saida.text().strip()

        if not data_entrada or not data_saida:
            QMessageBox.warning(self, 'Verificar Disponibilidade', 'Por favor, preencha as datas de entrada e saída.')
            return

        try:
            datetime.strptime(data_entrada, '%Y-%m-%d')
            datetime.strptime(data_saida, '%Y-%m-%d')
        except ValueError:
            QMessageBox.warning(self, 'Verificar Disponibilidade', 'Formato de data inválido. Utilize o formato YYYY-MM-DD.')
            return

        url = f'http://127.0.0.1:5000/api/reservas/disponibilidade'
        headers = {'Content-Type': 'application/json'}

        data = {
            'data_entrada': data_entrada,
            'data_saida': data_saida
        }

        try:
            response = requests.post(url, json=data, headers=headers)

            if response.status_code == 200:
                quartos_disponiveis = response.json()
                self.update_table(quartos_disponiveis)
            else:
                QMessageBox.warning(self, 'Verificar Disponibilidade', f'Erro ao verificar disponibilidade: {response.status_code}')
        
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'Erro de Conexão', f'Erro ao conectar à API: {str(e)}')

    def update_table(self, quartos_disponiveis):
        self.tableWidget.setRowCount(len(quartos_disponiveis))
        for row, quarto in enumerate(quartos_disponiveis):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(quarto['id'])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(quarto['status_quarto']))

def main():
    app = QApplication(sys.argv)
    window = VerificarDisponibilidadeWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
