import sys
import requests
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,
    QFormLayout, QMessageBox, QSizePolicy
)

class DeletarReservaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Deletar Reserva')
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        # Layout principal
        self.layout_principal = QHBoxLayout()

        # Layout para a lista de reservas à esquerda
        self.layout_lista = QVBoxLayout()
        
        self.label_lista = QLabel('Lista de Reservas')
        self.lista_reservas = QListWidget()
        self.lista_reservas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.lista_reservas.itemClicked.connect(self.exibir_dados_reserva)
        
        self.layout_lista.addWidget(self.label_lista)
        self.layout_lista.addWidget(self.lista_reservas)

        # Layout para os dados da reserva à direita
        self.layout_dados = QVBoxLayout()
        
        self.label_dados = QLabel('Dados da Reserva')
        self.layout_dados.addWidget(self.label_dados)

        self.form_layout = QFormLayout()
        
        self.label_id = QLabel('ID:')
        self.input_id = QLineEdit()
        self.input_id.setReadOnly(True)
        self.form_layout.addRow(self.label_id, self.input_id)

        self.label_cliente = QLabel('Cliente:')
        self.input_cliente = QLineEdit()
        self.form_layout.addRow(self.label_cliente, self.input_cliente)

        self.label_quarto = QLabel('Quarto:')
        self.input_quarto = QLineEdit()
        self.form_layout.addRow(self.label_quarto, self.input_quarto)

        self.label_data_inicio = QLabel('Data de Início:')
        self.input_data_inicio = QLineEdit()
        self.form_layout.addRow(self.label_data_inicio, self.input_data_inicio)

        self.label_data_fim = QLabel('Data de Fim:')
        self.input_data_fim = QLineEdit()
        self.form_layout.addRow(self.label_data_fim, self.input_data_fim)
        
        self.layout_dados.addLayout(self.form_layout)
        
        # Botão para deletar reserva
        self.btn_deletar = QPushButton('Deletar Reserva')
        self.btn_deletar.clicked.connect(self.deletar_reserva)
        self.layout_dados.addWidget(self.btn_deletar)

        # Adicionar layouts principais à janela
        self.layout_principal.addLayout(self.layout_lista)
        self.layout_principal.addLayout(self.layout_dados)

        self.setLayout(self.layout_principal)

        # Inicializar a lista de reservas
        self.carregar_lista_reservas()

    def carregar_lista_reservas(self):
        try:
            url = 'http://127.0.0.1:5000/api/reservas'
            response = requests.get(url)
            reservas = response.json()

            self.lista_reservas.clear()  # Limpar a lista de reservas antes de carregar novamente

            for reserva in reservas:
                item = QListWidgetItem(f"ID: {reserva['id']} - Cliente: {reserva['id_cliente']}")
                item.setData(1, reserva)  # Armazenar dados completos da reserva como data do item
                self.lista_reservas.addItem(item)

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'Erro de Conexão', f'Erro ao conectar à API: {str(e)}')

    def exibir_dados_reserva(self, item):
        reserva = item.data(1)  # Recuperar dados da reserva armazenados no item
        self.input_id.setText(str(reserva['id']))
        self.input_cliente.setText(str(reserva['id_cliente']))  # Pegando o ID do cliente
        self.input_quarto.setText(str(reserva['id_quarto']))    # Pegando o ID do quarto
        self.input_data_inicio.setText(reserva['data_checkin'])  # Pegando a data de check-in
        self.input_data_fim.setText(reserva['data_checkout'])   # Pegando a data de check-out

    def deletar_reserva(self):
        reserva_id = self.input_id.text()
        cliente_reserva = self.input_cliente.text().strip()  # Pegando o ID do cliente para exibição

        if not cliente_reserva:
            QMessageBox.warning(self, 'Deletar Reserva', 'Por favor, selecione uma reserva da lista.')
            return

        confirmacao = QMessageBox.question(self, 'Deletar Reserva', f'Deseja realmente deletar a reserva do cliente {cliente_reserva}?',
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmacao == QMessageBox.StandardButton.Yes:
            url = f'http://127.0.0.1:5000/api/reservas/{reserva_id}'

            try:
                response = requests.delete(url)

                if response.status_code == 200:
                    QMessageBox.information(self, 'Deletar Reserva', 'Reserva deletada com sucesso!')
                    self.limpar_campos()
                    self.carregar_lista_reservas()  # Atualizar a lista de reservas após a exclusão
                else:
                    QMessageBox.warning(self, 'Deletar Reserva', f'Erro ao deletar reserva: {response.status_code}')

            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, 'Erro de Conexão', f'Erro ao conectar à API: {str(e)}')

    def limpar_campos(self):
        self.input_id.clear()
        self.input_cliente.clear()
        self.input_quarto.clear()
        self.input_data_inicio.clear()
        self.input_data_fim.clear()

def main():
    app = QApplication(sys.argv)
    window = DeletarReservaWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
