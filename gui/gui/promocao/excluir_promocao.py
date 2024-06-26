import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox, QMessageBox
from PyQt6.QtCore import Qt

class TelaExcluirPromocao(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Excluir Promoção por ID")

        layout = QVBoxLayout()

        self.label_id = QLabel("ID da Promoção:")
        self.edit_id = QLineEdit()

        layout.addWidget(self.label_id)
        layout.addWidget(self.edit_id)

        # Botões de Ok e Cancelar
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.excluir_promocao)
        button_box.rejected.connect(self.reject)

        layout.addWidget(button_box)

        self.setLayout(layout)

    def excluir_promocao(self):
        try:
            id_promocao = int(self.edit_id.text())
            # Aqui você chamaria o método para excluir a promoção pelo ID
            # Exemplo de uso:
            # promocao_controller.excluir_promocao(id_promocao)
            QMessageBox.information(self, "Sucesso", "Promoção excluída com sucesso!")
            self.accept()
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um ID válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    tela_excluir_promocao = TelaExcluirPromocao()
    tela_excluir_promocao.show()

    sys.exit(app.exec())
