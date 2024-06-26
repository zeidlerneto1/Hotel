from repositories.cliente_repository import ClienteRepository
from models.cliente import Cliente
from email_validator import validate_email, EmailNotValidError

class ClienteService:
    def __init__(self):
        self.repository = ClienteRepository()
        
    def validar_email(self, email):
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False

    def salvar(self, cliente):
        if not self.validar_email(cliente.email):
            raise ValueError("E-mail inválido")
        self.repository.salvar(cliente)

    def atualizar(self, cliente):
        if not self.validar_email(cliente.email):
            raise ValueError("E-mail inválido")
        self.repository.atualizar(cliente)

    def excluir(self, cliente):
        self.repository.excluir(cliente)

    def buscar_por_id(self, cliente_id):
        return self.repository.buscar_por_id(cliente_id)

    def buscar_todos(self):
        return self.repository.buscar_todos()