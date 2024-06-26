from models.feedback import Feedback
from models.base import db

class FeedbackRepository:
    def salvar(self, feedback):
        db.session.add(feedback)
        db.session.commit()

    def buscar_por_id(self, feedback_id):
        return Feedback.query.get(feedback_id)

    def buscar_todos(self):
        return Feedback.query.all()

    def atualizar(self, feedback):
        db.session.commit()

    def excluir(self, feedback):
        db.session.delete(feedback)
        db.session.commit()