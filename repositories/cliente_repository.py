from models.base import db
from models.cliente import Cliente

class ClienteRepository:
    @staticmethod
    def salvar(cliente):
        db.session.add(cliente)
        db.session.commit()

    @staticmethod
    def atualizar(cliente):
        db.session.commit()

    @staticmethod
    def excluir(cliente):
        db.session.delete(cliente)
        db.session.commit()

    @staticmethod
    def buscar_por_id(cliente_id):
        return Cliente.query.get(cliente_id)

    @staticmethod
    def buscar_todos():
        return Cliente.query.all()