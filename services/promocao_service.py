from models.promocao import Promocao, db
from repositories.promocao_repository import PromocaoRepository


class PromocaoService:
    def __init__(self):
        self.repository = PromocaoRepository()

    def salvar(self, promocao):
        self.repository.salvar(promocao)

    def atualizar(self, promocao):
        self.repository.atualizar(promocao)

    def excluir(self, promocao):
        self.repository.excluir(promocao)

    def buscar_por_id(self, promocao_id):
        return self.repository.buscar_por_id(promocao_id)

    def buscar_todos(self):
        return self.repository.buscar_todos()