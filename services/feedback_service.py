from models.feedback import Feedback
from repositories.feedback_repository import FeedbackRepository
from sqlalchemy.exc import SQLAlchemyError
from models.base import db


class FeedbackService:
    def __init__(self):
        self.repository = FeedbackRepository()

    def salvar(self, feedback):
        self.repository.salvar(feedback)

    def buscar_por_id(self, feedback_id):
        return self.repository.buscar_por_id(feedback_id)

    def buscar_todos(self):
        return self.repository.buscar_todos()

    def atualizar(self, feedback):
        self.repository.atualizar(feedback)

    def excluir(self, feedback):
        self.repository.excluir(feedback)