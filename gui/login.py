import sys
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.uic import loadUi

# Classe da interface de login
class LoginDialog(QDialog):
    # Sinal para login bem-sucedido
    login_successful = pyqtSignal()

    def __init__(self):
        super().__init__()
        loadUi('login.ui', self)

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.close)

    def login(self):
        # Aqui você implementa a lógica de verificação de login
        # Por exemplo, verificar se o usuário e senha estão corretos
        if self.lineEdit.text() == "admin" and self.lineEdit_2.text() == "admin":
            self.login_successful.emit()  # Emitir sinal de login bem-sucedido
            self.accept()  # Fechar a janela de login

# Função para abrir a janela principal após o login bem-sucedido
def open_inicio():
    from inicio import MainWindow  # Importar a classe MainWindow do arquivo inicio.py
    inicio_window = MainWindow()
    inicio_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_dialog = LoginDialog()

    # Conectar o sinal de login bem-sucedido para abrir a janela de início
    login_dialog.login_successful.connect(open_inicio)

    login_dialog.show()
    sys.exit(app.exec())
