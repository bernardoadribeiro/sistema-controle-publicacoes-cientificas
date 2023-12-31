from flask_sqlalchemy import SQLAlchemy

from decouple import config
import pytz


# Default DB Timezone
tz = pytz.timezone('America/Sao_Paulo')


def init_database(app):
    """ Configura a conexao com o banco de dados e sua inicializacao
    """

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}/{config('DB_NAME')}"
    app.config['SQLALCHEMY_ECHO'] = config('SQLALCHEMY_ECHO')

    db = SQLAlchemy()
    db.init_app(app)

    return db
