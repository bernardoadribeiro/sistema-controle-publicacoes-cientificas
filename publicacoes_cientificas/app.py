from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from decouple import config

from .routes import index, publicacoes


app = Flask(__name__)

app.secret_key = config('SECRET_KEY')

# Inicializa o Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}/{config('DB_NAME')}"
app.config['SQLALCHEMY_ECHO'] = config('SQLALCHEMY_ECHO')

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db, directory='./publicacoes_cientificas/migrations')


# Start app
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=config('FLASK_RUN_PORT'),
        use_reloader=True,
        debug=config('FLASK_DEBUG'),
    )


app.register_blueprint(index.index_bp, url_prefix='/')
app.register_blueprint(publicacoes.publicacoes_bp, url_prefix='/publicacoes')


from .models import Publicacoes
