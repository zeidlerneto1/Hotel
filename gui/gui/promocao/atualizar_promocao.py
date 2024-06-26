from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog, QDialogButtonBox, QMessageBox
import sys

class TelaAtualizarPromocao(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Atualizar Promoção por ID")
        layout = QVBoxLayout()

        self.label_id = QLabel("ID da Promoção:", self)
        self.edit_id = QLineEdit(self)
        layout.addWidget(self.label_id)
        layout.addWidget(self.edit_id)

        self.label_descricao = QLabel("Nova Descrição:", self)
        self.edit_descricao = QLineEdit(self)
        layout.addWidget(self.label_descricao)
        layout.addWidget(self.edit_descricao)

        self.label_desconto = QLabel("Novo Desconto (%):", self)
        self.edit_desconto = QLineEdit(self)
        layout.addWidget(self.label_desconto)
        layout.addWidget(self.edit_desconto)

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        button_box = QDialogButtonBox(buttons)
        button_box.accepted.connect(self.atualizar_promocao)
        button_box.rejected.connect(self.reject)

        layout.addWidget(button_box)
        self.setLayout(layout)

    def atualizar_promocao(self):
        id_promocao = int(self.edit_id.text())
        descricao = self.edit_descricao.text()
        desconto = int(self.edit_desconto.text())
        # Aqui você chamaria o método para atualizar a promoção pelo ID
        # Exemplo de uso:
        # atualizacao_promo = {'descricao': descricao, 'desconto': desconto}
        # promocao_controller.atualizar_promocao(id_promocao, atualizacao_promo)
        QMessageBox.information(self, "Sucesso", "Promoção atualizada com sucesso!")
        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_atualizar_promocao = TelaAtualizarPromocao()
    if tela_atualizar_promocao.exec() == QDialog.Accepted:
        # Aqui você poderia chamar a função para atualizar a promoção pelo ID
        # Exemplo:
        # atualizar_promocao()
        pass
    sys.exit(app.exec())
