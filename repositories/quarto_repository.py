from models.quarto import Quarto, db

class QuartoRepository:
    def buscar_todos(self):
        return Quarto.query.all()

    def buscar_por_id(self, id):
        return Quarto.query.get(id)

    def salvar(self, quarto):
        db.session.add(quarto)
        db.session.commit()

    def atualizar(self, quarto):
        db.session.commit()

    def excluir(self, quarto):
        db.session.delete(quarto)
        db.session.commit()