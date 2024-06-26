from PyQt6 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 700, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Nome", "Endereço", "Telefone", "Email", "RG"])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(50, 20, 100, 25))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.pushButton_refresh.clicked.connect(self.listar_clientes)

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(170, 20, 100, 25))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_back.clicked.connect(MainWindow.close)  # Conectar ao fechamento da janela

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lista de Clientes"))
        self.pushButton_refresh.setText(_translate("MainWindow", "Atualizar"))
        self.pushButton_back.setText(_translate("MainWindow", "Voltar"))

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
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(client['id'])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(client['nome']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(client['endereco']))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(client['telefone']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(client['email']))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(client['documento_RG_cliente']))

    def show_error_message(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg_box.setText("Erro")
        msg_box.setInformativeText(message)
        msg_box.setWindowTitle("Erro")
        msg_box.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
    
    

