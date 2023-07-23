from flask import Flask
from decouple import config

from .routes import index, publicacoes

app = Flask(__name__)

app.secret_key = config('SECRET_KEY')

# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}'
# app.config['SQLALCHEMY_ECHO'] = config('SQLALCHEMY_ECHO')


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
