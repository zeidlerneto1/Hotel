from models.reserva import Reserva, db
from models.quarto import Quarto
from models.hospede import Hospede
from models.cliente import Cliente
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy import SQLAlchemy

class ReservaRepository:
    
    def buscar_por_nome_do_cliente(self, nome_cliente):
        try:
            return Reserva.query.join(Cliente).filter(Cliente.nome == nome_cliente).all()
        except SQLAlchemyError as e:
            raise e
    
    def buscar_todas(self):
        return Reserva.query.all()

    def buscar_por_id(self, id):
        return Reserva.query.get(id)

    def salvar(self, reserva):
        db.session.add(reserva)
        db.session.commit()

    def atualizar(self, reserva):
        db.session.commit()

    def excluir(self, reserva):
        db.session.delete(reserva)
        db.session.commit()

    def verificar_conflito(self, id_quarto, nova_data_checkin, nova_data_checkout, reserva_id=None):
        query = db.session.query(Reserva).filter(
            Reserva.id_quarto == id_quarto,
            Reserva.id != reserva_id,
            ((Reserva.data_checkin <= nova_data_checkout) & (Reserva.data_checkout >= nova_data_checkin))
        )
        return db.session.query(query.exists()).scalar()

    def verificar_disponibilidade(self, data_entrada, data_saida):
        subquery = db.session.query(Reserva.id_quarto).filter(
            (Reserva.data_checkin <= data_saida) & (Reserva.data_checkout >= data_entrada)
        ).subquery()

        quartos_disponiveis = db.session.query(Quarto).filter(
            ~Quarto.id.in_(subquery),
            Quarto.status_quarto == 'disponível'
        ).all()

        return quartos_disponiveis
