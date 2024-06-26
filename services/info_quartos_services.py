from models.quarto import Quarto
from models.promocao import Promocao

class InfoQuartoService:
    def obter_informacoes_quartos(self):
        quartos_disponiveis = Quarto.query.filter_by(disponivel=True).all()
        promocoes = Promocao.query.all()

        info_quartos = []
        for quarto in quartos_disponiveis:
            promocao_quarto = self.encontrar_promocao(quarto.id, promocoes)
            info_quarto = {
                'id': quarto.id,
                'tipo': quarto.tipo,
                'preco_diaria': quarto.preco_diaria,
                'disponivel': quarto.disponivel,
                'promocao': promocao_quarto,
            }
            info_quartos.append(info_quarto)

        return info_quartos

    def encontrar_promocao(self, quarto_id, promocoes):
        for promocao in promocoes:
            if promocao.aplicavel_a(quarto_id):
                return {
                    'id': promocao.id,
                    'descricao': promocao.descricao,
                    'data_inicio': promocao.data_inicio,
                    'data_fim': promocao.data_fim,
                    'desconto': promocao.desconto,
                }
        return None
