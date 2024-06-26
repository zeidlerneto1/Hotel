from models.promocao import Promocao, db

class PromocaoRepository:
    def buscar_todos(self):
        return Promocao.query.all()

    def buscar_por_id(self, id):
        return Promocao.query.get(id)

    def salvar(self, promocao):
        db.session.add(promocao)
        db.session.commit()

    def atualizar(self, promocao):
        db.session.commit()

    def excluir(self, promocao):
        db.session.delete(promocao)
        db.session.commit()