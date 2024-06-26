import sys
import requests
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
)
from PyQt6 import QtCore, QtWidgets

class ListarReservasWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 700, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)  # Ajustar para a quantidade de colunas das reservas
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "ID Quarto", "ID Cliente", "Data Check-in", "Data Check-out", "Status Reserva", "Custo Adicional", "Custo Total"])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        self.pushButton_refresh = QPushButton(self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(50, 20, 100, 25))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.pushButton_refresh.setText("Atualizar")
        self.pushButton_refresh.clicked.connect(self.listar_reservas)

        self.pushButton_back = QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(170, 20, 100, 25))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_back.setText("Voltar")
        self.pushButton_back.clicked.connect(self.close)  # Conectar ao fechamento da janela

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.setWindowTitle("Lista de Reservas")
        self.setupUi()

    def setupUi(self):
        self.pushButton_refresh.clicked.connect(self.listar_reservas)

    def listar_reservas(self):
        url = "http://127.0.0.1:5000/api/reservas"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                reservas = response.json()
                self.update_table(reservas)
            else:
                self.show_error_message(f"Erro ao buscar reservas: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Erro de conexão: {e}")

    def update_table(self, reservas):
        self.tableWidget.setRowCount(len(reservas))
        for row, reserva in enumerate(reservas):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(reserva['id'])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(reserva['id_quarto'])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(reserva['id_cliente'])))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(reserva['data_checkin']))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(reserva['data_checkout']))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(reserva['status_reserva']))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(str(reserva['custo_adicional'])))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(str(reserva['custo_total'])))

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setText("Erro")
        msg_box.setInformativeText(message)
        msg_box.setWindowTitle("Erro")
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListarReservasWindow()
    window.show()
    sys.exit(app.exec())
