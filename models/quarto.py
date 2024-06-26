from .base import db

class Quarto(db.Model):
    __tablename__ = 'quarto'
    
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    tp_quarto= db.Column(db.String(50), nullable=False)
    status_quarto= db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'tp_quarto': self.tp_quarto,
            'status_quarto': self.status_quarto
        }