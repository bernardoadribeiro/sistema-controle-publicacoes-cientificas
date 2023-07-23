from publicacoes_cientificas.app import db


class Publicacoes(db.Model):
    """ Model para tabela de Publicacoes """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255),  nullable=False)
