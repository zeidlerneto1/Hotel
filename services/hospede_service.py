from repositories.hospede_repository import HospedeRepository
from models.hospede import Hospede

class HospedeService:
    def __init__(self):
        self.repository = HospedeRepository()

    def salvar(self, hospede):
        self.repository.salvar(hospede)

    def atualizar(self, hospede):
        self.repository.atualizar(hospede)

    def excluir(self, hospede):
        self.repository.excluir(hospede)

    def buscar_por_id(self, hospede_id):
        return self.repository.buscar_por_id(hospede_id)

    def buscar_todos(self):
        return self.repository.buscar_todos()
