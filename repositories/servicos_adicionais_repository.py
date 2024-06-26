from models.servicos_adicionais import servicos_adc, db

class ServicosAdicionaisRepository:
    def buscar_todos(self):
        return servicos_adc.query.all()

    def buscar_por_id(self, id):
        return servicos_adc.query.get(id)

    def salvar(self, servico_adicional):
        db.session.add(servico_adicional)
        db.session.commit()

    def atualizar(self, servico_adicional):
        db.session.commit()

    def excluir(self, servico_adicional):
        db.session.delete(servico_adicional)
        db.session.commit()