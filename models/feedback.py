from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, func
from sqlalchemy.orm import relationship
from models.base import db

class Feedback(db.Model):
    __tablename__ = 'feedback'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    data_feedback = Column(DateTime, nullable=False, default=func.now())
    texto = Column(Text, nullable=False)
    
    cliente = relationship("Cliente", back_populates="feedbacks")

    def to_dict(self):
        return {
            'id': self.id,
            'cliente_id': self.cliente_id,
            'data_feedback': self.data_feedback,
            'texto': self.texto
        }