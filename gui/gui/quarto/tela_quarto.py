import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from quarto.listar_quarto import ListarQuarto
from quarto.obter_quarto import ObterQuarto
from quarto.criar_quarto import CriaQuarto
from quarto.atualizar_quarto import AtualizaQuartos
from quarto.excluir_quarto import ExcluirQuarto

class Tela_Quarto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operações de Quarto")
        self.setGeometry(100, 100, 400, 300)

        # Criando os botões
        self.btn_listar_quartos = QPushButton("Listar Quartos", self)
        self.btn_listar_quartos.setGeometry(50, 30, 300, 40)
        self.btn_listar_quartos.clicked.connect(self.abrir_listar_quartos)

        self.btn_obter_quarto = QPushButton("Obter Quarto", self)
        self.btn_obter_quarto.setGeometry(50, 80, 300, 40)
        self.btn_obter_quarto.clicked.connect(self.abrir_obter_quarto)

        self.btn_criar_quarto = QPushButton("Criar Quarto", self)
        self.btn_criar_quarto.setGeometry(50, 130, 300, 40)
        self.btn_criar_quarto.clicked.connect(self.abrir_criar_quarto)

        self.btn_atualizar_quarto = QPushButton("Atualizar Quarto", self)
        self.btn_atualizar_quarto.setGeometry(50, 180, 300, 40)
        self.btn_atualizar_quarto.clicked.connect(self.abrir_atualizar_quarto)

        self.btn_excluir_quarto = QPushButton("Excluir Quarto", self)
        self.btn_excluir_quarto.setGeometry(50, 230, 300, 40)
        self.btn_excluir_quarto.clicked.connect(self.abrir_excluir_quarto)

    def abrir_listar_quartos(self):
        self.listar_quartos = ListarQuarto()
        self.listar_quartos.show()

    def abrir_obter_quarto(self):
        self.obter_quarto = ObterQuarto()
        self.obter_quarto.show()

    def abrir_criar_quarto(self):
        self.criar_quarto = CriaQuarto()
        self.criar_quarto.show()

    def abrir_atualizar_quarto(self):
        self.atualizar_quarto = AtualizaQuartos()
        self.atualizar_quarto.show()

    def abrir_excluir_quarto(self):
        self.excluir_quarto = ExcluirQuarto()
        self.excluir_quarto.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_quarto = Tela_Quarto()
    tela_quarto.show()
    sys.exit(app.exec())
