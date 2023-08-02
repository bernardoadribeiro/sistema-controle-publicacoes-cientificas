from datetime import datetime
from publicacoes_cientificas.app import db
from publicacoes_cientificas.database import tz


class Publicacoes(db.Model):
    """ Model para tabela de Publicacoes """
    id = db.Column(db.Integer, primary_key=True)
    criado_em = db.Column(db.DateTime(), default=datetime.now(tz))
    atualizado_em = db.Column(db.DateTime(), default=datetime.now(tz))
    titulo = db.Column(db.String(255),  nullable=False)
    autor_principal = db.Column(db.String(255),  nullable=False)  # TODO: transformar em FK
    orientador = db.Column(db.String(255), nullable=False)        # TODO: transformar em FK
    coorientador = db.Column(db.String(255), nullable=True)       # TODO: transformar em FK
    citacao = db.Column(db.String(255), nullable=True)
    url = db.Column(db.String(255), nullable=False)
    resumo = db.Column(db.Text(), nullable=True)
    abstract = db.Column(db.Text(), nullable=True)
    assunto = db.Column(db.String(20), nullable=False)            # TODO: transformar em FK
    lingua = db.Column(db.String(20), nullable=False)
    pub_tipo = db.Column(db.String(255), nullable=False)          # TODO: transformar em FK
    colecao = db.Column(db.String(255), nullable=True)            # TODO: transformar em FK
    ifnmg_campus = db.Column(db.String(255), nullable=False)      # TODO: transformar em FK
    curso = db.Column(db.String(255), nullable=False)             # TODO: transformar em FK
    qtd_paginas = db.Column(db.Integer(), nullable=True)
