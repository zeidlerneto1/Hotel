from flask import request, jsonify
from services.servicos_adicionais_service import ServicosAdicionaisService
from models.servicos_adicionais import servicos_adc

servicos_adicionais_service = ServicosAdicionaisService()


def listar_servicos_adicionais():
    servicos_adicionais = servicos_adicionais_service.buscar_todos()
    return jsonify([servico.to_dict() for servico in servicos_adicionais]), 200

def obter_servico_adicional(id):
    servico_adicional = servicos_adicionais_service.buscar_por_id(id)
    if not servico_adicional:
        return jsonify({'erro': 'Serviço adicional não encontrado'}), 404
    return jsonify(servico_adicional.to_dict()), 200

def criar_servico_adicional():
    data = request.get_json()
    servico_adicional = servicos_adc(
        nome_servico=data.get('nome_servico'),
        descricao=data.get('descricao'),
        preco=data.get('preco'),
        id_reserva=data.get('id_reserva')
    )
    servicos_adicionais_service.salvar(servico_adicional)
    return jsonify(servico_adicional.to_dict()), 201

def atualizar_servico_adicional(id):
    data = request.get_json()
    servico_adicional = servicos_adicionais_service.buscar_por_id(id)
    if not servico_adicional:
        return jsonify({'erro': 'Serviço adicional não encontrado'}), 404
    servico_adicional.nome_servico = data.get('nome_servico')
    servico_adicional.descricao = data.get('descricao')
    servico_adicional.preco = data.get('preco')
    servico_adicional.id_reserva = data.get('id_reserva')
    servicos_adicionais_service.atualizar(servico_adicional)
    return jsonify(servico_adicional.to_dict()), 200

def excluir_servico_adicional(id):
    servico_adicional = servicos_adicionais_service.buscar_por_id(id)
    if not servico_adicional:
        return jsonify({'erro': 'Serviço adicional não encontrado'}), 404
    servicos_adicionais_service.excluir(servico_adicional)
    return jsonify({'mensagem': 'Serviço adicional excluído com sucesso'}), 200
