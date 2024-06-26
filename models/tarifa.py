from models.base import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.quarto import Quarto

class Tarifa(db.Model): 
    __tablename_ = 'tarifa'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_quarto = db.Column(db.Integer,ForeignKey("quarto.id"))
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'id_quarto': self.id_quarto,
            'data_inicio': self.data_inicio,
            'data_fim': self.data_fim,
            'preco': self.preco
        }
    
    
Quarto = relationship('quarto', backref=db.backref('tarifa', lazy=True))
    

