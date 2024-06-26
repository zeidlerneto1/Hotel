from models.quarto import Quarto, db
from repositories.quarto_repository import QuartoRepository

class QuartoService:
    def __init__(self):
        self.repository = QuartoRepository()

    def salvar(self, quarto):
        self.repository.salvar(quarto)

    def atualizar(self, quarto):
        self.repository.atualizar(quarto)

    def excluir(self, quarto):
        self.repository.excluir(quarto)

    def buscar_por_id(self, quarto_id):
        return self.repository.buscar_por_id(quarto_id)

    def buscar_todos(self):
        return self.repository.buscar_todos()
