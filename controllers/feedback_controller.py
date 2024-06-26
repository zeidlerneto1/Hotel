from flask import jsonify, request
from services.feedback_service import FeedbackService
from models.feedback import Feedback

feedback_service = FeedbackService()

def criar_feedback(data):
    data = request.get_json()
    novo_feedback = Feedback(
        cliente_id=data.get('cliente_id'),
        texto=data.get('texto')
    )
    feedback_service.salvar(novo_feedback)
    return jsonify(novo_feedback.to_dict()), 201

def obter_feedback(feedback_id):
    feedback = feedback_service.buscar_por_id(feedback_id)
    if feedback:
        return jsonify(feedback.to_dict()), 200
    else:
        return jsonify({"erro": "Feedback não encontrado"}), 404

def listar_feedbacks():
    feedbacks = feedback_service.buscar_todos()
    return jsonify([feedback.to_dict() for feedback in feedbacks]), 200

def atualizar_feedback(feedback_id):
    data = request.get_json()
    feedback = feedback_service.buscar_por_id(feedback_id)
    if not feedback:
        return jsonify({"erro": "Feedback não encontrado"}), 404
    
    feedback.cliente_id = data.get('cliente_id', feedback.cliente_id)
    feedback.texto = data.get('texto', feedback.texto)

    feedback_service.atualizar(feedback)
    return jsonify(feedback.to_dict()), 200

def excluir_feedback(id):
    feedback = feedback_service.buscar_por_id(id)
    if feedback:
        feedback_service.excluir(feedback)
        return jsonify({"mensagem": "Feedback excluído com sucesso"}), 200
    else:
        return jsonify({"erro": "Feedback não encontrado"}), 404
