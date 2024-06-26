from flask import jsonify
from controllers import promocao_controller
from models.promocao import Promocao

class InfoQuartoController:
    def obter_informacoes_quartos(self):
        # Chamada ao controller para listar promoções
        promocoes = promocao_controller.listar_promocoes()

        # Construir o retorno JSON manualmente
        response = {
            'promocoes': [promocao.to_dict() for promocao in promocoes]
        }

        # Retornar a resposta JSON
        return jsonify(response), 200