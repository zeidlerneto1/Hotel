from flask import request, jsonify
from services.promocao_service import PromocaoService
from models.promocao import Promocao

promocao_service = PromocaoService()

def listar_promocoes():
    promocoes = promocao_service.buscar_todos()
    return jsonify([promocao.to_dict() for promocao in promocoes]), 200

def obter_promocao(id):
    promocao = promocao_service.buscar_por_id(id)
    if not promocao:
        return jsonify({'erro': 'Promoção não encontrada'}), 404
    return jsonify(promocao.to_dict()), 200

def criar_promocao():
    data = request.get_json()
    promocao = Promocao(
        descricao=data.get('descricao'),
        data_inicio=data.get('data_inicio'),
        data_fim=data.get('data_fim'),
        desconto=data.get('desconto')
    )
    promocao_service.salvar(promocao)
    return jsonify(promocao.to_dict()), 201

def atualizar_promocao(id):
    data = request.get_json()
    promocao = promocao_service.buscar_por_id(id)
    if not promocao:
        return jsonify({'erro': 'Promoção não encontrada'}), 404
    promocao.id = data.get('id')
    promocao.descricao = data.get('descricao')
    promocao.data_inicio = data.get('data_inicio')
    promocao.data_fim = data.get('data_fim')
    promocao.desconto = data.get('desconto')
    promocao_service.atualizar(promocao)
    return jsonify(promocao.to_dict()), 200

def excluir_promocao(id):
    promocao = promocao_service.buscar_por_id(id)
    if not promocao:
        return jsonify({'erro': 'Promoção não encontrada'}), 404
    promocao_service.excluir(promocao)
    return jsonify({'mensagem': 'Promoção excluída com sucesso'}), 200
