from flask import request, jsonify
from services.quarto_service import QuartoService
from models.quarto import Quarto

quarto_service = QuartoService()

def listar_quartos():
    quartos = quarto_service.buscar_todos()
    return jsonify([quarto.to_dict() for quarto in quartos]), 200

def obter_quarto(id):
    quarto = quarto_service.buscar_por_id(id)
    if not quarto:
        return jsonify({'erro': 'Quarto não encontrado'}), 404
    return jsonify(quarto.to_dict()), 200

def criar_quarto():
    data = request.get_json()
    quarto = Quarto(
        tp_quarto=data.get('tp_quarto'),
        status_quarto=data.get('status_quarto')
    )
    quarto_service.salvar(quarto)
    return jsonify(quarto.to_dict()), 201

def atualizar_quarto(id):
    data = request.get_json()
    quarto = quarto_service.buscar_por_id(id)
    if not quarto:
        return jsonify({'erro': 'Quarto não encontrado'}), 404
    
    quarto.tp_quarto = data.get('tp_quarto', quarto.tp_quarto)
    quarto.status_quarto = data.get('status_quarto', quarto.status_quarto)
    
    quarto_service.atualizar(quarto)
    return jsonify(quarto.to_dict()), 200

'''
def criar_quarto():
    data = request.get_json()
    quarto = {
        'tp_quarto': data.get('tp_quarto'),
        'status_quarto': data.get('status_quarto')
    }
    quarto_service.salvar(quarto)
    return jsonify(quarto), 201

def atualizar_quarto(id):
    data = request.get_json()
    quarto = quarto_service.buscar_por_id(id)
    if not quarto:
        return jsonify({'erro': 'Quarto não encontrado'}), 404
    quarto.tp_quarto = data.get('tp_quarto')
    quarto.status_quarto = data.get('status_quarto')
    quarto_service.atualizar(quarto)
    return jsonify(quarto.to_dict()), 200
'''
def excluir_quarto(id):
    quarto = quarto_service.buscar_por_id(id)
    if not quarto:
        return jsonify({'erro': 'Quarto não encontrado'}), 404
    quarto_service.excluir(quarto)
    return jsonify({'mensagem': 'Quarto excluído com sucesso'}), 200
