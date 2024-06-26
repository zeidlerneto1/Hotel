from models.base import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .quarto import Quarto
from models.cliente import Cliente

class Reserva(db.Model):
    __tablename__ = 'reserva'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_quarto = db.Column(db.Integer,ForeignKey('quarto.id'))
    id_cliente = db.Column(db.Integer,ForeignKey('cliente.id'))
    data_checkin = db.Column(db.Date, nullable=False)
    data_checkout = db.Column(db.Date, nullable=False)
    status_reserva= db.Column(db.String(20), nullable=False)
    custo_adicional= db.Column(db.Float, nullable=False)
    custo_total= db.Column(db.Float, nullable=False)
    
    quarto = relationship('Quarto', backref=db.backref('reservas', lazy=True))
    cliente = relationship('Cliente', backref=db.backref('reservas', lazy=True))
    
    def to_dict(reserva):
        return {
            'id': reserva.id,
            'id_quarto': reserva.id_quarto,
            'id_cliente': reserva.id_cliente,
            'data_checkin': reserva.data_checkin,
            'data_checkout': reserva.data_checkout,
            'status_reserva': reserva.status_reserva,
            'custo_adicional': reserva.custo_adicional,
            'custo_total': reserva.custo_total
        }
        
