from models.base import db
from models.hospede import Hospede

class HospedeRepository:
    def salvar(self, hospede):
        db.session.add(hospede)
        db.session.commit()

    def atualizar(self, hospede):
        db.session.commit()

    def excluir(self, hospede):
        db.session.delete(hospede)
        db.session.commit()

    def buscar_por_id(self, hospede_id):
        return Hospede.query.get(hospede_id)

    def buscar_todos(self):
        return Hospede.query.all()
