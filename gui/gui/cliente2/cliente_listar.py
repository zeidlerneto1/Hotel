import sys
import requests
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
)
from PyQt6 import QtCore, QtGui, QtWidgets

class ListarClientesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 700, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Nome", "Endereço", "Telefone", "Email", "RG"])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        self.pushButton_refresh = QPushButton(self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(50, 20, 100, 25))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.pushButton_refresh.setText("Atualizar")
        self.pushButton_refresh.clicked.connect(self.listar_clientes)

        self.pushButton_back = QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(170, 20, 100, 25))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_back.setText("Voltar")
        self.pushButton_back.clicked.connect(self.close)  # Conectar ao fechamento da janela

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.setWindowTitle("Lista de Clientes")
        self.setupUi()

    def setupUi(self):
        self.pushButton_refresh.clicked.connect(self.listar_clientes)

    def listar_clientes(self):
        url = "http://127.0.0.1:5000/api/clientes"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                clients = response.json()
                self.update_table(clients)
            else:
                self.show_error_message(f"Erro ao buscar clientes: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Erro de conexão: {e}")

    def update_table(self, clients):
        self.tableWidget.setRowCount(len(clients))
        for row, client in enumerate(clients):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(client['id'])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(client['nome']))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(client['endereco']))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(client['telefone']))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(client['email']))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(client['documento_RG_cliente']))

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setText("Erro")
        msg_box.setInformativeText(message)
        msg_box.setWindowTitle("Erro")
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListarClientesWindow()
    window.show()
    sys.exit(app.exec())
