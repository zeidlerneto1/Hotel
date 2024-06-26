from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        font = QtGui.QFont()
        font.setPointSize(12)

        self.pushButton_listar_clientes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_listar_clientes.setGeometry(QtCore.QRect(50, 30, 300, 40))
        self.pushButton_listar_clientes.setObjectName("pushButton_listar_clientes")
        self.pushButton_listar_clientes.setFont(font)
        
        self.pushButton_obter_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_obter_cliente.setGeometry(QtCore.QRect(50, 80, 300, 40))
        self.pushButton_obter_cliente.setObjectName("pushButton_obter_cliente")
        self.pushButton_obter_cliente.setFont(font)
        
        self.pushButton_cadastrar_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cadastrar_cliente.setGeometry(QtCore.QRect(50, 130, 300, 40))
        self.pushButton_cadastrar_cliente.setObjectName("pushButton_cadastrar_cliente")
        self.pushButton_cadastrar_cliente.setFont(font)
        
        self.pushButton_atualizar_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_atualizar_cliente.setGeometry(QtCore.QRect(50, 180, 300, 40))
        self.pushButton_atualizar_cliente.setObjectName("pushButton_atualizar_cliente")
        self.pushButton_atualizar_cliente.setFont(font)
        
        self.pushButton_deletar_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_deletar_cliente.setGeometry(QtCore.QRect(50, 230, 300, 40))
        self.pushButton_deletar_cliente.setObjectName("pushButton_deletar_cliente")
        self.pushButton_deletar_cliente.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)  # Adicione essa linha

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Operações de Cliente"))
        self.pushButton_listar_clientes.setText(_translate("MainWindow", "Listar Clientes"))
        self.pushButton_obter_cliente.setText(_translate("MainWindow", "Obter Cliente"))
        self.pushButton_cadastrar_cliente.setText(_translate("MainWindow", "Cadastrar Cliente"))
        self.pushButton_atualizar_cliente.setText(_translate("MainWindow", "Atualizar Cliente"))
        self.pushButton_deletar_cliente.setText(_translate("MainWindow", "Deletar Cliente"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet("background-color: #f0f0f0;")  # Definindo o estilo da janela principal

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
