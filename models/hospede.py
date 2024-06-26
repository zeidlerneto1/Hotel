from .reserva import Reserva
from models.quarto import Quarto
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base import db

class Hospede(db.Model):
    __tablename__ = 'hospede'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    reserva_id = db.Column(db.Integer, ForeignKey("reserva.id"))
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'reserva_id': self.reserva_id
        }

reserva = relationship('Reserva', back_populates='hospedes')

