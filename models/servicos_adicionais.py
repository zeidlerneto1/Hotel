from models.base import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.reserva import Reserva

class servicos_adc(db.Model):
    __tablename__ = 'servicos_adicionais'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_servico = db.Column(db.String(100), nullable=False)
    descricao =db.Column(db.Text, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    id_reserva = db.Column(db.Integer,ForeignKey("reserva.id"))

    def to_dict(self):
        return {
            'id': self.id,
            'nome_servico': self.nome_servico,
            'descricao': self.descricao,
            'preco': self.preco,
            'id_reserva': self.id_reserva,
        }
    
Reserva = relationship('Reserva', backref=db.backref('servicos_adicionais', lazy=True))
