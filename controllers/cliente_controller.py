from flask import request, jsonify
from services.cliente_service import ClienteService
from models.cliente import Cliente

cliente_service = ClienteService()


def listar_clientes():
    clientes = cliente_service.buscar_todos()
    return jsonify([cliente.to_dict() for cliente in clientes]), 200

def obter_cliente(id):
    cliente = cliente_service.buscar_por_id(id)
    if not cliente:
        return jsonify({'erro': 'Cliente não encontrado'}), 404
    return jsonify(cliente.to_dict()), 200

def criar_cliente():
    data = request.get_json()
    cliente = Cliente(
        nome=data.get('nome'),
        endereco=data.get('endereco'),
        telefone=data.get('telefone'),
        email=data.get('email'),
        documento_RG_cliente=data.get('documento_RG_cliente')
    )
    cliente_service.salvar(cliente)
    return jsonify(cliente.to_dict()), 201

def atualizar_cliente(id):
    data = request.get_json()
    cliente = cliente_service.buscar_por_id(id)
    if not cliente:
        return jsonify({'erro': 'Cliente não encontrado'}), 404
    cliente.nome = data.get('nome')
    cliente.endereco = data.get('endereco')
    cliente.telefone = data.get('telefone')
    cliente.email = data.get('email')
    cliente.documento_RG_cliente = data.get('documento_RG_cliente')
    cliente_service.atualizar(cliente)
    return jsonify(cliente.to_dict()), 200

def excluir_cliente(id):
    cliente = cliente_service.buscar_por_id(id)
    if not cliente:
        return jsonify({'erro': 'Cliente não encontrado'}), 404
    cliente_service.excluir(cliente)
    return jsonify({'mensagem': 'Cliente excluído com sucesso'}), 200
