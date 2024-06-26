import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Importando as classes adicionais necessárias
from servicos_adicionais.atualizar_servico import TelaAtualizarServicoAdicional
from servicos_adicionais.criar_servico import TelaCriarServicoAdicional
from servicos_adicionais.excluir_servico import TelaExcluirServico
from servicos_adicionais.listar_servico import TelaListarServicos
from servicos_adicionais.obter_servico import ObterServicoAdicional

class Tela_Servicos_Adicionais(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operações de Serviços Adicionais")
        self.setGeometry(100, 100, 400, 300)

        # Criando os botões
        self.btn_listar_servicos = QPushButton("Listar Serviços", self)
        self.btn_listar_servicos.setGeometry(50, 30, 300, 40)
        self.btn_listar_servicos.clicked.connect(self.abrir_tela_listar_servicos)

        self.btn_obter_servico = QPushButton("Obter Serviço", self)
        self.btn_obter_servico.setGeometry(50, 80, 300, 40)
        self.btn_obter_servico.clicked.connect(self.abrir_tela_obter_servico)

        self.btn_criar_servico = QPushButton("Criar Serviço", self)
        self.btn_criar_servico.setGeometry(50, 130, 300, 40)
        self.btn_criar_servico.clicked.connect(self.abrir_tela_criar_servico)

        self.btn_atualizar_servico = QPushButton("Atualizar Serviço", self)
        self.btn_atualizar_servico.setGeometry(50, 180, 300, 40)
        self.btn_atualizar_servico.clicked.connect(self.abrir_tela_atualizar_servico)

        self.btn_excluir_servico = QPushButton("Excluir Serviço", self)
        self.btn_excluir_servico.setGeometry(50, 230, 300, 40)
        self.btn_excluir_servico.clicked.connect(self.abrir_tela_excluir_servico)

        # Definindo atributos para as telas adicionais
        self.tela_listar_servicos = None
        self.obter_servico = None
        self.criar_servico = None
        self.atualizar_servico = None
        self.excluir_servico = None

    def abrir_tela_listar_servicos(self):
        self.tela_listar_servicos = TelaListarServicos()
        self.tela_listar_servicos.show()

    def abrir_tela_obter_servico(self):
        self.obter_servico = ObterServicoAdicional()
        self.obter_servico.show()

    def abrir_tela_criar_servico(self):
        self.criar_servico = TelaCriarServicoAdicional()
        self.criar_servico.show()

    def abrir_tela_atualizar_servico(self):
        self.atualizar_servico = TelaAtualizarServicoAdicional()
        self.atualizar_servico.show()

    def abrir_tela_excluir_servico(self):
        self.excluir_servico = TelaExcluirServico()
        self.excluir_servico.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_servicos = Tela_Servicos_Adicionais()
    tela_servicos.show()
    sys.exit(app.exec())
