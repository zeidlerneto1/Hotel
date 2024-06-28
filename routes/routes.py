from flask import Blueprint,request
from controllers import cliente_controller
from controllers import hospede_controller
from controllers import reserva_controller
from controllers import quarto_controller
from controllers import tarifa_controller
from controllers import servicos_adicionais_controller
from controllers import promocao_controller
from controllers import feedback_controller


cliente_bp = Blueprint('cliente_bp', __name__)


@cliente_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    return cliente_controller.listar_clientes()

@cliente_bp.route('/clientes/<int:id>', methods=['GET'])
def obter_cliente(id):
    return cliente_controller.obter_cliente(id)

@cliente_bp.route('/clientes', methods=['POST'])
def criar_cliente():
    return cliente_controller.criar_cliente()

@cliente_bp.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    return cliente_controller.atualizar_cliente(id)

@cliente_bp.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    return cliente_controller.excluir_cliente(id)

hospede_bp = Blueprint('hospede_bp', __name__)

@hospede_bp.route('/hospedes', methods=['GET'])
def listar_hospedes():
    return hospede_controller.listar_hospedes()

@hospede_bp.route('/hospedes/<int:id>', methods=['GET'])
def obter_hospede(id):
    return hospede_controller.obter_hospede(id)

@hospede_bp.route('/hospedes', methods=['POST'])
def criar_hospede():
    return hospede_controller.criar_hospede()

@hospede_bp.route('/hospedes/<int:id>', methods=['PUT'])
def atualizar_hospede(id):
    return hospede_controller.atualizar_hospede(id)

@hospede_bp.route('/hospedes/<int:id>', methods=['DELETE'])
def excluir_hospede(id):
    return hospede_controller.excluir_hospede(id)

@hospede_bp.route('/reservas/<int:id_reserva>/hospedes', methods=['POST'])
def adicionar_hospedes_reserva(id_reserva):
    return reserva_controller.adicionar_hospedes_reserva(id_reserva, request.get_json())

reserva_bp = Blueprint('reserva_bp', __name__)

@reserva_bp.route('/reservas', methods=['GET'])
def listar_reservas():
    return reserva_controller.listar_reservas()

@reserva_bp.route('/reservas/<int:id>', methods=['GET'])
def obter_reserva(id):
    return reserva_controller.obter_reserva(id)

@reserva_bp.route('/reservas', methods=['POST'])
def criar_reserva():
    return reserva_controller.criar_reserva()

@reserva_bp.route('/reservas/<int:id>', methods=['PUT'])
def atualizar_reserva(id):
    return reserva_controller.atualizar_reserva(id)

@reserva_bp.route('/reservas/<int:id>', methods=['DELETE'])
def excluir_reserva(id):
    return reserva_controller.excluir_reserva(id)

@reserva_bp.route('/reservas/<int:reserva_id>/atualizar_quarto', methods=['PUT'])
def atualizar_quarto(reserva_id):
    return reserva_controller.atualizar_quarto(reserva_id)

@reserva_bp.route('/reservas/disponibilidade', methods=['POST'])
def verificar_disponibilidade():
    return reserva_controller.verificar_disponibilidade()

@reserva_bp.route('/reservas/<int:id>/quarto', methods=['PUT'])
def atualizar_quarto_reserva(id): #(mesma funcao que @reserva_bp.route('/reservas/<int:reserva_id>/atualizar_quarto', methods=['PUT'])  )
    return reserva_controller.atualizar_quarto_reserva(id)


quarto_bp = Blueprint('quarto_bp', __name__)

@quarto_bp.route('/quartos', methods=['GET'])
def listar_quartos():
    return quarto_controller.listar_quartos()

@quarto_bp.route('/quartos/<int:id>', methods=['GET'])
def obter_quarto(id):
    return quarto_controller.obter_quarto(id)

@quarto_bp.route('/quartos', methods=['POST'])
def criar_quarto():
    return quarto_controller.criar_quarto()

@quarto_bp.route('/quartos/<int:id>', methods=['PUT'])
def atualizar_quarto(id):
    return quarto_controller.atualizar_quarto(id)

@quarto_bp.route('/quartos/<int:id>', methods=['DELETE'])
def excluir_quarto(id):
    return quarto_controller.excluir_quarto(id)


servicos_adicionais_bp = Blueprint('servicos_adicionais_bp', __name__)

@servicos_adicionais_bp.route('/servicos_adicionais', methods=['GET'])
def listar_servicos_adicionais():
    return servicos_adicionais_controller.listar_servicos_adicionais()

@servicos_adicionais_bp.route('/servicos_adicionais/<int:id>', methods=['GET'])
def obter_servico_adicional(id):
    return servicos_adicionais_controller.obter_servico_adicional(id)

@servicos_adicionais_bp.route('/servicos_adicionais', methods=['POST'])
def criar_servico_adicional():
    return servicos_adicionais_controller.criar_servico_adicional()

@servicos_adicionais_bp.route('/servicos_adicionais/<int:id>', methods=['PUT'])
def atualizar_servico_adicional(id):
    return servicos_adicionais_controller.atualizar_servico_adicional(id)

@servicos_adicionais_bp.route('/servicos_adicionais/<int:id>', methods=['DELETE'])
def excluir_servico_adicional(id):
    return servicos_adicionais_controller.excluir_servico_adicional(id)


promocao_bp = Blueprint('promocao_bp', __name__)

@promocao_bp.route('/promocoes', methods=['GET'])
def listar_promocoes():
    return promocao_controller.listar_promocoes()

@promocao_bp.route('/promocoes/<int:id>', methods=['GET'])
def obter_promocao(id):
    return promocao_controller.obter_promocao(id)

@promocao_bp.route('/promocoes', methods=['POST'])
def criar_promocao():
    return promocao_controller.criar_promocao()

@promocao_bp.route('/promocoes/<int:id>', methods=['PUT'])
def atualizar_promocao(id):
    return promocao_controller.atualizar_promocao(id)

@promocao_bp.route('/promocoes/<int:id>', methods=['DELETE'])
def excluir_promocao(id):
    return promocao_controller.excluir_promocao(id)
    

tarifa_bp = Blueprint('tarifa_bp', __name__)

@tarifa_bp.route('/tarifas', methods=['GET'])
def listar_tarifas():
    return tarifa_controller.listar_tarifas()

@tarifa_bp.route('/tarifas/<int:id>', methods=['GET'])
def obter_tarifa(id):
    return tarifa_controller.obter_tarifa(id)

@tarifa_bp.route('/tarifas', methods=['POST'])
def criar_tarifa():
    return tarifa_controller.criar_tarifa()

@tarifa_bp.route('/tarifas/<int:id>', methods=['PUT'])
def atualizar_tarifa(id):
    return tarifa_controller.atualizar_tarifa(id)

@tarifa_bp.route('/tarifas/<int:id>', methods=['DELETE'])
def excluir_tarifa(id):
    return tarifa_controller.excluir_tarifa(id)


feedback_bp = Blueprint('feedback_bp', __name__)

@feedback_bp.route('/feedbacks', methods=['POST'])
def criar_novo_feedback():
    data = request.get_json()
    return feedback_controller.criar_feedback(data)

@feedback_bp.route('/feedbacks/<int:id>', methods=['PUT'])
def atualizar_feedback(id):
    return feedback_controller.atualizar_feedback(id)


@feedback_bp.route('/feedbacks/<int:feedback_id>', methods=['GET'])
def obter_um_feedback(feedback_id):
    return feedback_controller.obter_feedback(feedback_id)

@feedback_bp.route('/feedbacks', methods=['GET'])
def listar_todos_feedbacks():
    return feedback_controller.listar_feedbacks()

@feedback_bp.route('/feedbacks/<int:feedback_id>', methods=['DELETE'])
def excluir_um_feedback(feedback_id):
    return feedback_controller.excluir_feedback(feedback_id)
