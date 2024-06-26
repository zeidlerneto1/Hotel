from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import db


class Cliente(db.Model):
    __tablename__ = 'cliente'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    documento_RG_cliente = db.Column(db.String(50), unique=True, nullable=False)
    
    feedbacks = relationship("Feedback", back_populates="cliente")

    
    def to_dict(cliente):
        return {
        'id': cliente.id,
        'nome': cliente.nome,
        'endereco': cliente.endereco,
        'telefone': cliente.telefone,
        'email': cliente.email,
        'documento_RG_cliente': cliente.documento_RG_cliente
        }