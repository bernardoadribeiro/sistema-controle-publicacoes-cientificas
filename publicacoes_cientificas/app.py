from flask import Flask
from flask_migrate import Migrate

from decouple import config
import pytz

from publicacoes_cientificas import database
from publicacoes_cientificas.routes import index, publicacoes


app = Flask(__name__)

app.secret_key = config('SECRET_KEY')

# Inicializa o Banco de Dados
db = database.init_database(app)
database.load_models()
migrate = Migrate(app, db, directory='./publicacoes_cientificas/migrations')

# Default Timezone
tz = pytz.timezone('America/Sao_Paulo')


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
