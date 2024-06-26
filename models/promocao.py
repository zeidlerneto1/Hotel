
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import db

class Promocao(db.Model):
    __tablename__ = 'promocao'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(255),nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    desconto = db.Column(db.Float, nullable=False)

    
    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'data_inicio': self.data_inicio,
            'data_fim': self.data_fim,
            'desconto': self.desconto
        }