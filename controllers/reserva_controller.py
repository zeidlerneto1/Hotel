from flask import request, jsonify
from services.reserva_service import ReservaService
from models.reserva import Reserva

reserva_service = ReservaService()

def listar_reservas():
    try:
        reservas = reserva_service.buscar_todas()
        reservas_formatadas = []
        for reserva in reservas:
            reserva_dict = reserva.to_dict()
            reserva_dict['nome_cliente'] = reserva.cliente.nome
            reservas_formatadas.append(reserva_dict)
        return jsonify(reservas_formatadas), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

def obter_reserva(id):
    try:
        reserva = reserva_service.buscar_por_id(id)
        if not reserva:
            return jsonify({'erro': 'Reserva não encontrada'}), 404

        # Se você deseja buscar uma reserva pelo nome do cliente, pode adicionar essa lógica aqui
        nome_cliente = request.args.get('nome_cliente')
        if nome_cliente:
            # Aqui você poderia ajustar o serviço para buscar a reserva pelo nome do cliente
            # Vamos supor que seu serviço de reserva tenha um método para buscar por nome de cliente
            reserva = reserva_service.buscar_por_nome_do_cliente(nome_cliente)
            if not reserva:
                return jsonify({'erro': 'Reserva não encontrada para o cliente especificado'}), 404

        return jsonify(reserva.to_dict()), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

def criar_reserva():
    data = request.get_json()
    reserva = Reserva(
        id_quarto=data.get('id_quarto'),
        id_cliente=data.get('id_cliente'),
        data_checkin=data.get('data_checkin'),
        data_checkout=data.get('data_checkout'),
        status_reserva=data.get('status_reserva'),
        custo_adicional=data.get('custo_adicional'),
        custo_total=data.get('custo_total')
    )
    reserva_service.salvar(reserva)
    return jsonify(reserva.to_dict()), 201

def atualizar_reserva(id):
    data = request.get_json()
    reserva = reserva_service.buscar_por_id(id)
    if not reserva:
        return jsonify({'erro': 'Reserva não encontrada'}), 404
    reserva.id_quarto = data.get('id_quarto')
    reserva.id_cliente = data.get('id_cliente')
    reserva.data_checkin = data.get('data_checkin')
    reserva.data_checkout = data.get('data_checkout')
    reserva.status_reserva = data.get('status_reserva')
    reserva.custo_adicional = data.get('custo_adicional')
    reserva.custo_total = data.get('custo_total')
    reserva_service.atualizar(reserva)
    return jsonify(reserva.to_dict()), 200

def atualizar_quarto_reserva(id):
    data = request.get_json()
    novo_quarto_id = data.get('novo_quarto_id')
    custo_adicional = data.get('custo_adicional')
    
    try:
        reserva = reserva_service.atualizar_quarto(id, novo_quarto_id, custo_adicional)
        return jsonify(reserva.to_dict()), 200
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400

def atualizar_quarto(reserva_id):
    data = request.get_json()
    novo_quarto_id = data.get('id_quarto')
    custo_adicional = data.get('custo_adicional')

    reserva = reserva_service.buscar_por_id(reserva_id)
    if not reserva:
        return jsonify({'erro': 'Reserva não encontrada'}), 404

    if novo_quarto_id is not None:
        reserva.id_quarto = novo_quarto_id
    
    if custo_adicional is not None:
        reserva.custo_adicional = custo_adicional

    reserva_service.atualizar(reserva)

    return jsonify({
        'id': reserva.id,
        'id_quarto': reserva.id_quarto,
        'custo_adcional': reserva.custo_adicional
    }), 200

def excluir_reserva(id):
    reserva = reserva_service.buscar_por_id(id)
    if not reserva:
        return jsonify({'erro': 'Reserva não encontrada'}), 404
    reserva_service.excluir(reserva)
    return jsonify({'mensagem': 'Reserva excluída com sucesso'}), 200

def verificar_disponibilidade():
    data = request.get_json()
    data_entrada = data.get('data_entrada')
    data_saida = data.get('data_saida')

    quartos_disponiveis = reserva_service.verificar_disponibilidade(data_entrada, data_saida)
    return jsonify([quarto.to_dict() for quarto in quartos_disponiveis]), 200

def atualizar_reserva(id):
    data = request.get_json()
    reserva = reserva_service.buscar_por_id(id)
    if not reserva:
        return jsonify({'erro': 'Reserva não encontrada'}), 404
    
    nova_data_checkin = data.get('data_checkin')
    nova_data_checkout = data.get('data_checkout')
    
    if reserva_service.verificar_conflito(reserva.id_quarto, nova_data_checkin, nova_data_checkout, id):
        return jsonify({'erro': 'O quarto já está reservado para esse período'}), 400

    reserva.data_checkin = nova_data_checkin
    reserva.data_checkout = nova_data_checkout
    reserva.status_reserva = data.get('status_reserva', reserva.status_reserva)
    reserva.custo_adicional = data.get('custo_adicional', reserva.custo_adicional)
    reserva.custo_total = data.get('custo_total', reserva.custo_total)

    reserva_service.atualizar(reserva)
    return jsonify(reserva.to_dict()), 200