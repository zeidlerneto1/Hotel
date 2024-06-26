from models.reserva import Reserva, db
from models.quarto import Quarto
from models.hospede import Hospede
from repositories.reserva_repository import ReservaRepository
from repositories.quarto_repository import QuartoRepository
from repositories.hospede_repository import HospedeRepository
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError


class ReservaService:
    def __init__(self):
        self.reserva_repository = ReservaRepository()
        self.quarto_repository = QuartoRepository()
        self.hospede_repository = HospedeRepository()
    
    def buscar_por_nome_do_cliente(self, nome_cliente):
        try:
            return ReservaRepository.buscar_por_nome_do_cliente(nome_cliente)
        except SQLAlchemyError as e:
            raise e

    def buscar_todas(self):
        return self.reserva_repository.buscar_todas()

    def buscar_por_id(self, id):
        return self.reserva_repository.buscar_por_id(id)

    def salvar(self, reserva):
        self.reserva_repository.salvar(reserva)

    def atualizar(self, reserva):
        self.reserva_repository.atualizar(reserva)

    def excluir(self, reserva):
        self.reserva_repository.excluir(reserva)

    def atualizar_status_quarto_para_disponivel(self, reserva):
        quarto = self.quarto_repository.buscar_por_id(reserva.id_quarto)
        if quarto:
            quarto.status_quarto = 'disponível'
            self.quarto_repository.atualizar(quarto)

    def atualizar_quarto(self, reserva_id, novo_quarto_id, custo_adicional):
        reserva = self.buscar_por_id(reserva_id)
        if not reserva:
            return {'erro': 'Reserva não encontrada'}, 404

        novo_quarto = self.quarto_repository.buscar_por_id(novo_quarto_id)
        if not novo_quarto or novo_quarto.status_quarto != 'disponível':
            return {'erro': 'Quarto não disponível'}, 400

        antigo_quarto = self.quarto_repository.buscar_por_id(reserva.id_quarto)
        if not antigo_quarto:
            return {'erro': 'Quarto antigo não encontrado'}, 404

        reserva.id_quarto = novo_quarto_id
        reserva.custo_total += custo_adicional
        novo_quarto.status_quarto = 'reservado'
        antigo_quarto.status_quarto = 'disponível'

        self.reserva_repository.atualizar(reserva)
        self.quarto_repository.atualizar(novo_quarto)
        self.quarto_repository.atualizar(antigo_quarto)
        
        return reserva, 200

    def verificar_conflito(self, id_quarto, nova_data_checkin, nova_data_checkout, reserva_id=None):
        return self.reserva_repository.verificar_conflito(id_quarto, nova_data_checkin, nova_data_checkout, reserva_id)

    def verificar_disponibilidade(self, data_entrada, data_saida):
        return self.reserva_repository.verificar_disponibilidade(data_entrada, data_saida)

    def adicionar_hospedes(self, reserva_id, hospedes):
        reserva = self.buscar_por_id(reserva_id)
        if not reserva:
            raise ValueError('Reserva não encontrada')

        custo_adicional_por_hospede = 50
        for hospede_data in hospedes:
            hospede = Hospede(nome=hospede_data['nome'], reserva_id=reserva_id)
            self.hospede_repository.salvar(hospede)
            reserva.custo_total += custo_adicional_por_hospede

        self.reserva_repository.atualizar(reserva)
        return reserva
