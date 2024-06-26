from flask import request, jsonify
from services.hospede_service import HospedeService
from models.hospede import Hospede

hospede_service = HospedeService()

def listar_hospedes():
    hospedes = hospede_service.buscar_todos()
    return jsonify([hospede.to_dict() for hospede in hospedes]), 200

def obter_hospede(id):
    hospede = hospede_service.buscar_por_id(id)
    if not hospede:
        return jsonify({'erro': 'Hóspede não encontrado'}), 404
    return jsonify(hospede.to_dict()), 200

def criar_hospede():
    data = request.get_json()
    hospede = Hospede(
        id=data.get('id'),
        nome=data.get('nome'),
        reserva_id=data.get('reserva_id')
    )
    hospede_service.salvar(hospede)
    return jsonify(hospede.to_dict()), 201

def atualizar_hospede(id):
    data = request.get_json()
    hospede = hospede_service.buscar_por_id(id)
    if not hospede:
        return jsonify({'erro': 'Hóspede não encontrado'}), 404
    hospede.id = data.get('id')
    hospede.nome = data.get('nome')
    hospede.reserva_id = data.get('reserva_id')
    hospede_service.atualizar(hospede)
    return jsonify(hospede.to_dict()), 200

def excluir_hospede(id):
    hospede = hospede_service.buscar_por_id(id)
    if not hospede:
        return jsonify({'erro': 'Hóspede não encontrado'}), 404
    hospede_service.excluir(hospede)
    return jsonify({'mensagem': 'Hóspede excluído com sucesso'}), 200