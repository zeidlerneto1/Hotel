from PyQt6 import QtCore, QtGui, QtWidgets
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_url = QtWidgets.QLabel(self.centralwidget)
        self.label_url.setGeometry(QtCore.QRect(50, 30, 61, 21))
        self.label_url.setObjectName("label_url")
        
        self.lineEdit_url = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_url.setGeometry(QtCore.QRect(120, 30, 231, 21))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.lineEdit_url.setText("http://127.0.0.1:5000/api")
        
        self.label_search = QtWidgets.QLabel(self.centralwidget)
        self.label_search.setGeometry(QtCore.QRect(50, 70, 131, 21))
        self.label_search.setObjectName("label_search")
        
        self.lineEdit_search_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search_id.setGeometry(QtCore.QRect(190, 70, 71, 21))
        self.lineEdit_search_id.setObjectName("lineEdit_search_id")
        
        self.pushButton_search_id = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search_id.setGeometry(QtCore.QRect(270, 70, 75, 23))
        self.pushButton_search_id.setObjectName("pushButton_search_id")
        
        self.pushButton_search_all = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search_all.setGeometry(QtCore.QRect(360, 70, 111, 23))
        self.pushButton_search_all.setObjectName("pushButton_search_all")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 110, 701, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Nome", "Endereço", "Telefone", "Email", "RG"])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(50, 390, 71, 16))
        self.label_name.setObjectName("label_name")
        
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(50, 410, 141, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")
        
        self.label_address = QtWidgets.QLabel(self.centralwidget)
        self.label_address.setGeometry(QtCore.QRect(200, 390, 71, 16))
        self.label_address.setObjectName("label_address")
        
        self.lineEdit_address = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_address.setGeometry(QtCore.QRect(200, 410, 141, 21))
        self.lineEdit_address.setObjectName("lineEdit_address")
        
        self.label_phone = QtWidgets.QLabel(self.centralwidget)
        self.label_phone.setGeometry(QtCore.QRect(350, 390, 71, 16))
        self.label_phone.setObjectName("label_phone")
        
        self.lineEdit_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_phone.setGeometry(QtCore.QRect(350, 410, 141, 21))
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(500, 390, 71, 16))
        self.label_email.setObjectName("label_email")
        
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(500, 410, 141, 21))
        self.lineEdit_email.setObjectName("lineEdit_email")
        
        self.label_rg = QtWidgets.QLabel(self.centralwidget)
        self.label_rg.setGeometry(QtCore.QRect(650, 390, 71, 16))
        self.label_rg.setObjectName("label_rg")
        
        self.lineEdit_rg = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_rg.setGeometry(QtCore.QRect(650, 410, 101, 21))
        self.lineEdit_rg.setObjectName("lineEdit_rg")
        
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(50, 450, 75, 23))
        self.pushButton_create.setObjectName("pushButton_create")
        
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(140, 450, 75, 23))
        self.pushButton_update.setObjectName("pushButton_update")
        
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(230, 450, 75, 23))
        self.pushButton_delete.setObjectName("pushButton_delete")
        
        self.label_url.setText("URL:")
        self.label_search.setText("Buscar por ID:")
        self.label_name.setText("Nome:")
        self.label_address.setText("Endereço:")
        self.label_phone.setText("Telefone:")
        self.label_email.setText("Email:")
        self.label_rg.setText("RG:")
        self.pushButton_search_id.setText("Buscar")
        self.pushButton_search_all.setText("Buscar Todos")
        self.pushButton_create.setText("Criar")
        self.pushButton_update.setText("Atualizar")
        self.pushButton_delete.setText("Deletar")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerenciamento de Clientes"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_search_id.clicked.connect(self.search_client_by_id)
        self.pushButton_search_all.clicked.connect(self.search_all_clients)
        self.pushButton_create.clicked.connect(self.create_client)
        self.pushButton_update.clicked.connect(self.update_client)
        self.pushButton_delete.clicked.connect(self.delete_client)

    def search_client_by_id(self):
        client_id = self.lineEdit_search_id.text()
        if client_id.isdigit():
            url = f"{self.lineEdit_url.text()}/clientes/{client_id}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    client = response.json()
                    self.update_table([client])
                elif response.status_code == 404:
                    self.show_info_message("Cliente não encontrado.")
                    self.clear_fields()
                else:
                    self.show_error_message(f"Erro ao buscar cliente: {response.status_code}")
            except requests.exceptions.RequestException as e:
                self.show_error_message(f"Erro de conexão: {e}")
        else:
            self.show_error_message("ID do cliente deve ser um número inteiro.")

    def search_all_clients(self):
        url = f"{self.lineEdit_url.text()}/clientes"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                clients = response.json()
                self.update_table(clients)
            else:
                self.show_error_message(f"Erro ao buscar clientes: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Erro de conexão: {e}")

    def create_client(self):
        name = self.lineEdit_name.text()
        address = self.lineEdit_address.text()
        phone = self.lineEdit_phone.text()
        email = self.lineEdit_email.text()
        rg = self.lineEdit_rg.text()
        if name and address and phone and email and rg:
            data = {
                "nome": name,
                "endereco": address,
                "telefone": phone,
                "email": email,
                "documento_RG_cliente": rg
            }
            url = f"{self.lineEdit_url.text()}/clientes"
            try:
                response = requests.post(url, json=data)
                if response.status_code == 201:
                    self.show_info_message("Cliente criado com sucesso!")
                    self.clear_fields()
                else:
                    self.show_error_message(f"Erro ao criar cliente: {response.status_code}")
            except requests.exceptions.RequestException as e:
                self.show_error_message(f"Erro de conexão: {e}")
        else:
            self.show_error_message("Por favor, preencha todos os campos.")

    def update_client(self):
        client_id = self.lineEdit_search_id.text()
        name = self.lineEdit_name.text()
        address = self.lineEdit_address.text()
        phone = self.lineEdit_phone.text()
        email = self.lineEdit_email.text()
        rg = self.lineEdit_rg.text()
        if client_id.isdigit() and name and address and phone and email and rg:
            data = {
                "nome": name,
                "endereco": address,
                "telefone": phone,
                "email": email,
                "documento_RG_cliente": rg
            }
            url = f"{self.lineEdit_url.text()}/clientes/{client_id}"
            try:
                response = requests.put(url, json=data)
                if response.status_code == 200:
                    self.show_info_message("Dados do cliente atualizados com sucesso!")
                    self.clear_fields()
                elif response.status_code == 404:
                    self.show_info_message("Cliente não encontrado.")
                    self.clear_fields()
                else:
                    self.show_error_message(f"Erro ao atualizar cliente: {response.status_code}")
            except requests.exceptions.RequestException as e:
                self.show_error_message(f"Erro de conexão: {e}")
        else:
            self.show_error_message("Por favor, preencha todos os campos e forneça um ID válido.")

    def delete_client(self):
        client_id = self.lineEdit_search_id.text()
        if client_id.isdigit():
            url = f"{self.lineEdit_url.text()}/clientes/{client_id}"
            try:
                response = requests.delete(url)
                if response.status_code == 200:
                    self.show_info_message("Cliente deletado com sucesso!")
                    self.clear_fields()
                elif response.status_code == 404:
                    self.show_info_message("Cliente não encontrado.")
                    self.clear_fields()
                else:
                    self.show_error_message(f"Erro ao deletar cliente: {response.status_code}")
            except requests.exceptions.RequestException as e:
                self.show_error_message(f"Erro de conexão: {e}")
        else:
            self.show_error_message("ID do cliente deve ser um número inteiro.")

    def update_table(self, clients):
        self.tableWidget.setRowCount(len(clients))
        for row, client in enumerate(clients):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(client.get("id", ""))))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(client.get("nome", "")))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(client.get("endereco", "")))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(client.get("telefone", "")))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(client.get("email", "")))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(client.get("documento_RG_cliente", "")))

    def show_info_message(self, message):
        QtWidgets.QMessageBox.information(self, "Informação", message)

    def show_error_message(self, message):
        QtWidgets.QMessageBox.critical(self, "Erro", message)

    def clear_fields(self):
        self.lineEdit_name.clear()
        self.lineEdit_address.clear()
        self.lineEdit_phone.clear()
        self.lineEdit_email.clear()
        self.lineEdit_rg.clear()
        self.lineEdit_search_id.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
