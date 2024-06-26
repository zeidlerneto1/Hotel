import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt6.QtCore import Qt  # Importar Qt corretamente

# Importe aqui as janelas que estão sendo usadas nas funções
from reserva.cadastrar_reserva import CadastroReservaWindow
from reserva.listar_reserva import ListarReservasWindow
from reserva.deletar_reserva import DeletarReservaWindow
from reserva.atualizar_reserva import AtualizarReservaWindow
from reserva.atualizar_quarto import AtualizarQuartoReservaWindow
from reserva.verificar_disponibilidade import VerificarDisponibilidadeWindow
from reserva.obter_reserva import ObterReservaWindow

class Tela_Reserva(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Reserva")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout_principal = QVBoxLayout(central_widget)

        label_titulo = QLabel("Menu de Reservas")
        label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Corrigido para Qt.AlignmentFlag.AlignCenter
        layout_principal.addWidget(label_titulo)

        self.botao_cadastrar_reserva = QPushButton("Cadastrar Reserva")
        self.botao_cadastrar_reserva.clicked.connect(self.show_cadastro_reserva_window)
        layout_principal.addWidget(self.botao_cadastrar_reserva)

        self.botao_listar_reservas = QPushButton("Listar Reservas")
        self.botao_listar_reservas.clicked.connect(self.show_listar_reservas_window)
        layout_principal.addWidget(self.botao_listar_reservas)

        self.botao_deletar_reserva = QPushButton("Deletar Reserva")
        self.botao_deletar_reserva.clicked.connect(self.show_deletar_reserva_window)
        layout_principal.addWidget(self.botao_deletar_reserva)

        self.botao_atualizar_reserva = QPushButton("Atualizar Reserva")
        self.botao_atualizar_reserva.clicked.connect(self.show_atualizar_reserva_window)
        layout_principal.addWidget(self.botao_atualizar_reserva)

        self.botao_atualizar_quarto = QPushButton("Atualizar Quarto")
        self.botao_atualizar_quarto.clicked.connect(self.show_atualizar_quarto_window)
        layout_principal.addWidget(self.botao_atualizar_quarto)

        self.botao_verificar_disponibilidade = QPushButton("Verificar Disponibilidade")
        self.botao_verificar_disponibilidade.clicked.connect(self.show_verificar_disponibilidade_window)
        layout_principal.addWidget(self.botao_verificar_disponibilidade)

        self.botao_obter_reserva = QPushButton("Obter Reserva")
        self.botao_obter_reserva.clicked.connect(self.show_obter_reserva_window)
        layout_principal.addWidget(self.botao_obter_reserva)

        self.cadastro_reserva_window = None
        self.listar_reservas_window = None
        self.deletar_reserva_window = None
        self.atualizar_reserva_window = None
        self.atualizar_quarto_window = None
        self.verificar_disponibilidade_window = None
        self.obter_reserva_window = None

    def show_cadastro_reserva_window(self):
        if self.cadastro_reserva_window is None:
            self.cadastro_reserva_window = CadastroReservaWindow()
        self.cadastro_reserva_window.show()

    def show_listar_reservas_window(self):
        if self.listar_reservas_window is None:
            self.listar_reservas_window = ListarReservasWindow()
        self.listar_reservas_window.show()

    def show_deletar_reserva_window(self):
        if self.deletar_reserva_window is None:
            self.deletar_reserva_window = DeletarReservaWindow()
        self.deletar_reserva_window.show()

    def show_atualizar_reserva_window(self):
        if self.atualizar_reserva_window is None:
            self.atualizar_reserva_window = AtualizarReservaWindow()
        self.atualizar_reserva_window.show()

    def show_atualizar_quarto_window(self):
        if self.atualizar_quarto_window is None:
            self.atualizar_quarto_window = AtualizarQuartoReservaWindow()
        self.atualizar_quarto_window.show()

    def show_verificar_disponibilidade_window(self):
        if self.verificar_disponibilidade_window is None:
            self.verificar_disponibilidade_window = VerificarDisponibilidadeWindow()
        self.verificar_disponibilidade_window.show()

    def show_obter_reserva_window(self):
        if self.obter_reserva_window is None:
            self.obter_reserva_window = ObterReservaWindow()
        self.obter_reserva_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_reserva = Tela_Reserva()
    tela_reserva.show()
    sys.exit(app.exec())
