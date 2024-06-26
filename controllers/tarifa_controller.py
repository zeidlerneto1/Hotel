from flask import request, jsonify
from services.tarifa_service import TarifaService
from models.tarifa import Tarifa

tarifa_service = TarifaService()

def listar_tarifas():
    tarifas = tarifa_service.buscar_todas()
    return jsonify([tarifa.to_dict() for tarifa in tarifas]), 200

def obter_tarifa(id):
    tarifa = tarifa_service.buscar_por_id(id)
    if not tarifa:
        return jsonify({'erro': 'Tarifa não encontrada'}), 404
    return jsonify(tarifa.to_dict()), 200

def criar_tarifa():
    data = request.get_json()
    tarifa = Tarifa(
        id_quarto=data.get('id_quarto'),
        data_inicio=data.get('data_inicio'),
        data_fim= data.get('data_fim'),
        preco= data.get('preco')
    )
    tarifa_service.salvar(tarifa)
    return jsonify(tarifa.to_dict()), 201

def atualizar_tarifa(id):
    data = request.get_json()
    tarifa = tarifa_service.buscar_por_id(id)
    if not tarifa:
        return jsonify({'erro': 'Tarifa não encontrada'}), 404
    tarifa.id = data.get('id')
    tarifa.id_quarto = data.get('id_quarto')
    tarifa.data_inicio = data.get('data_inicio')
    tarifa.data_fim = data.get('data_fim')
    tarifa.preco = data.get('preco')
    tarifa_service.atualizar(tarifa)
    return jsonify(tarifa.to_dict()), 200

def excluir_tarifa(id):
    tarifa = tarifa_service.buscar_por_id(id)
    if not tarifa:
        return jsonify({'erro': 'Tarifa não encontrada'}), 404
    tarifa_service.excluir(tarifa)
    return jsonify({'mensagem': 'Tarifa excluída com sucesso'}), 200
