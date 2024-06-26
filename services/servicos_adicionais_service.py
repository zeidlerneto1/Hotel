from models.servicos_adicionais import servicos_adc, db
from repositories.servicos_adicionais_repository import ServicosAdicionaisRepository
class ServicosAdicionaisService:
    def __init__(self):
        self.repository = ServicosAdicionaisRepository()

    def salvar(self, servico_adicional):
        self.repository.salvar(servico_adicional)

    def atualizar(self, servico_adicional):
        self.repository.atualizar(servico_adicional)

    def excluir(self, servico_adicional):
        self.repository.excluir(servico_adicional)

    def buscar_por_id(self, servico_adicional_id):
        return self.repository.buscar_por_id(servico_adicional_id)

    def buscar_todos(self):
        return self.repository.buscar_todos()