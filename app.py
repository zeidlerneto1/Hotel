from flask import Flask
from flask_restful import Api
from routes.routes import cliente_bp, hospede_bp, reserva_bp, quarto_bp, servicos_adicionais_bp, tarifa_bp, feedback_bp,promocao_bp
from models.base import db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/hotel'

    db.init_app(app)

    # Flask API
    api = Api(app)
    app.register_blueprint(cliente_bp, url_prefix='/api')
    app.register_blueprint(hospede_bp, url_prefix='/api')
    app.register_blueprint(reserva_bp, url_prefix='/api')
    app.register_blueprint(quarto_bp, url_prefix='/api')
    app.register_blueprint(servicos_adicionais_bp, url_prefix='/api')
    app.register_blueprint(tarifa_bp, url_prefix='/api')
    app.register_blueprint(feedback_bp, url_prefix='/api')
    app.register_blueprint(promocao_bp, url_prefix='/api')


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)