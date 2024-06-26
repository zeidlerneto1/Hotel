from models.tarifa import Tarifa, db

class TarifaRepository:
    def buscar_todas(self):
        return Tarifa.query.all()

    def buscar_por_id(self, id):
        return Tarifa.query.get(id)

    def salvar(self, tarifa):
        db.session.add(tarifa)
        db.session.commit()

    def atualizar(self, tarifa):
        db.session.commit()

    def excluir(self, tarifa):
        db.session.delete(tarifa)
        db.session.commit()