import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon

class TelaOpcoesPromocoes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Opções de Promoções")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Estilizando os botões
        estilo_botao = """
            QPushButton {
                background-color: #007bff;
                color: white;
                font-size: 16px;
                height: 40px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """

        # Botão Listar Promoções
        btn_listar = QPushButton(QIcon("list_icon.png"), "Listar Promoções")
        btn_listar.setIconSize(btn_listar.sizeHint() / 2)
        btn_listar.setStyleSheet(estilo_botao)
        btn_listar.clicked.connect(self.listar_promocoes)
        layout.addWidget(btn_listar)

        # Botão Obter Promoção por ID
        btn_obter = QPushButton(QIcon("get_icon.png"), "Obter Promoção por ID")
        btn_obter.setIconSize(btn_obter.sizeHint() / 2)
        btn_obter.setStyleSheet(estilo_botao)
        btn_obter.clicked.connect(self.obter_promocao)
        layout.addWidget(btn_obter)

        # Botão Criar Nova Promoção
        btn_criar = QPushButton(QIcon("create_icon.png"), "Criar Nova Promoção")
        btn_criar.setIconSize(btn_criar.sizeHint() / 2)
        btn_criar.setStyleSheet(estilo_botao)
        btn_criar.clicked.connect(self.criar_promocao)
        layout.addWidget(btn_criar)

        # Botão Atualizar Promoção por ID
        btn_atualizar = QPushButton(QIcon("update_icon.png"), "Atualizar Promoção por ID")
        btn_atualizar.setIconSize(btn_atualizar.sizeHint() / 2)
        btn_atualizar.setStyleSheet(estilo_botao)
        btn_atualizar.clicked.connect(self.atualizar_promocao)
        layout.addWidget(btn_atualizar)

        # Botão Excluir Promoção por ID
        btn_excluir = QPushButton(QIcon("delete_icon.png"), "Excluir Promoção por ID")
        btn_excluir.setIconSize(btn_excluir.sizeHint() / 2)
        btn_excluir.setStyleSheet(estilo_botao)
        btn_excluir.clicked.connect(self.excluir_promocao)
        layout.addWidget(btn_excluir)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Aplicando folha de estilo global para a aplicação
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
        """)

    def listar_promocoes(self):
        QMessageBox.information(self, "Opção Selecionada", "Você selecionou Listar Promoções.")

    def obter_promocao(self):
        QMessageBox.information(self, "Opção Selecionada", "Você selecionou Obter Promoção por ID.")

    def criar_promocao(self):
        QMessageBox.information(self, "Opção Selecionada", "Você selecionou Criar Nova Promoção.")

    def atualizar_promocao(self):
        QMessageBox.information(self, "Opção Selecionada", "Você selecionou Atualizar Promoção por ID.")

    def excluir_promocao(self):
        QMessageBox.information(self, "Opção Selecionada", "Você selecionou Excluir Promoção por ID.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_opcoes = TelaOpcoesPromocoes()
    tela_opcoes.show()
    sys.exit(app.exec())
