from PyQt6 import QtCore, QtGui, QtWidgets
import requests
from PIL import Image
from io import BytesIO
import subprocess

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(535, 374)
        Dialog.setStyleSheet("background-image: url(\"https://arteref.com/wp-content/uploads/2023/04/DESTAQUE-16.jpg?w=700\");\n"
"")
        # Frame para o título
        self.frame_titulo = QtWidgets.QFrame(Dialog)
        self.frame_titulo.setGeometry(QtCore.QRect(0, 0, 535, 80))
        self.frame_titulo.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);")  # Fundo semitransparente
        self.label_titulo = QtWidgets.QLabel(self.frame_titulo)
        self.label_titulo.setGeometry(QtCore.QRect(0, 0, 535, 80))
        self.label_titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        self.label_titulo.setText("<html><head/><body><p><span style=\" font-size:20pt; color:#333333;\">LOGIN SISTEMA HOTEL</span></p></body></html>")

        # Rótulo e campo de texto para Usuário
        self.label_usuario = QtWidgets.QLabel(Dialog)
        self.label_usuario.setGeometry(QtCore.QRect(70, 100, 51, 21))
        self.label_usuario.setObjectName("label_usuario")
        self.label_usuario.setText("Usuário")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 100, 191, 21))
        self.lineEdit.setObjectName("lineEdit")

        # Rótulo e campo de texto para Senha
        self.label_senha = QtWidgets.QLabel(Dialog)
        self.label_senha.setGeometry(QtCore.QRect(70, 130, 51, 21))
        self.label_senha.setObjectName("label_senha")
        self.label_senha.setText("Senha")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 130, 191, 21))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.abrir_inicio)  # Conectar o botão a função abrir_inicio

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.sair)  # Conectar o botão "Sair" à função sair

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(-120, 0, 791, 481))
        self.label_4.setStyleSheet("image: url(:/icons/background-image.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.frame_titulo.raise_()
        self.label_usuario.raise_()
        self.label_senha.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login Sistema Hotel"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.pushButton_2.setText(_translate("Dialog", "Sair"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Digite seu usuário"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Digite sua senha"))

    def abrir_inicio(self):
        # Função para abrir a interface Inicio.py
        subprocess.Popen(["python", "C:/Users/peter/OneDrive/Documentos/programação/PAV/hotel2_Atual/gui/gui/Inicio.py"])

    def sair(self):
        # Função para encerrar a aplicação
        QtWidgets.QApplication.instance().quit()

    def carregar_imagem(self, url):
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        qt_image = self.convert_pil_to_qimage(image)
        pixmap = QtGui.QPixmap.fromImage(qt_image)
        self.label_4.setPixmap(pixmap)

    def convert_pil_to_qimage(self, pil_image):
        data = pil_image.convert("RGBA").tobytes("raw", "RGBA")
        q_image = QtGui.QImage(data, pil_image.width, pil_image.height, QtGui.QImage.Format.Format_RGBA8888)
        return q_image

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.carregar_imagem("https://arteref.com/wp-content/uploads/2023/04/DESTAQUE-16.jpg?w=700")
    Dialog.show()
    sys.exit(app.exec())
