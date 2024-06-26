import sys
import requests
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
)
from PyQt6 import QtCore, QtWidgets

class ObterReservaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label_pesquisa = QLabel("Pesquisar por ID da Reserva:", self.centralwidget)
        self.label_pesquisa.setGeometry(QtCore.QRect(50, 20, 200, 25))
        self.label_pesquisa.setObjectName("label_pesquisa")

        self.input_pesquisa = QLineEdit(self.centralwidget)
        self.input_pesquisa.setGeometry(QtCore.QRect(250, 20, 150, 25))
        self.input_pesquisa.setObjectName("input_pesquisa")

        self.pushButton_pesquisar = QPushButton("Pesquisar", self.centralwidget)
        self.pushButton_pesquisar.setGeometry(QtCore.QRect(420, 20, 100, 25))
        self.pushButton_pesquisar.setObjectName("pushButton_pesquisar")
        self.pushButton_pesquisar.clicked.connect(self.obter_reserva)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 60, 700, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)  # Ajustar para a quantidade de colunas das reservas
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "ID Quarto", "ID Cliente", "Data Check-in", "Data Check-out", "Status Reserva", "Custo Adicional", "Custo Total"])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        self.pushButton_back = QPushButton("Voltar", self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(550, 20, 100, 25))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_back.clicked.connect(self.close)  # Conectar ao fechamento da janela

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.setWindowTitle("Obter Reserva")
        self.setupUi()

    def setupUi(self):
        pass

    def obter_reserva(self):
        reserva_id = self.input_pesquisa.text().strip()

        if not reserva_id:
            QMessageBox.warning(self, 'Pesquisar Reserva', 'Por favor, insira o ID da reserva.')
            return

        url = f"http://127.0.0.1:5000/api/reservas/{reserva_id}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                reserva = response.json()
                self.update_table(reserva)
            else:
                self.show_error_message(f"Erro ao buscar reserva: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Erro de conexão: {e}")

    def update_table(self, reserva):
        self.tableWidget.setRowCount(1)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(str(reserva['id'])))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(str(reserva['id_quarto'])))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(str(reserva['id_cliente'])))
        self.tableWidget.setItem(0, 3, QTableWidgetItem(reserva['data_checkin']))
        self.tableWidget.setItem(0, 4, QTableWidgetItem(reserva['data_checkout']))
        self.tableWidget.setItem(0, 5, QTableWidgetItem(reserva['status_reserva']))
        self.tableWidget.setItem(0, 6, QTableWidgetItem(str(reserva['custo_adicional'])))
        self.tableWidget.setItem(0, 7, QTableWidgetItem(str(reserva['custo_total'])))

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setText("Erro")
        msg_box.setInformativeText(message)
        msg_box.setWindowTitle("Erro")
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ObterReservaWindow()
    window.show()
    sys.exit(app.exec())
