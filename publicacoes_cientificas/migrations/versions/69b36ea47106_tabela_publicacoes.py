"""tabela_publicacoes

Revision ID: 69b36ea47106
Revises: ae18fb0936c0
Create Date: 2023-07-26 14:40:23.881424

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '69b36ea47106'
down_revision = 'ae18fb0936c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('publicacoes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('criado_em', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('atualizado_em', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('titulo', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('autor_principal', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('orientador', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('coorientador', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('citacao', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('url', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('resumo', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('abstract', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('assunto', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('lingua', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('pub_tipo', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('colecao', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('ifnmg_campus', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('curso', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('qtd_paginas', sa.Integer(), nullable=True))
        batch_op.drop_column('title')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('publicacoes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', mysql.VARCHAR(length=255), nullable=False))
        batch_op.drop_column('qtd_paginas')
        batch_op.drop_column('curso')
        batch_op.drop_column('ifnmg_campus')
        batch_op.drop_column('colecao')
        batch_op.drop_column('pub_tipo')
        batch_op.drop_column('lingua')
        batch_op.drop_column('assunto')
        batch_op.drop_column('abstract')
        batch_op.drop_column('resumo')
        batch_op.drop_column('url')
        batch_op.drop_column('citacao')
        batch_op.drop_column('coorientador')
        batch_op.drop_column('orientador')
        batch_op.drop_column('autor_principal')
        batch_op.drop_column('titulo')
        batch_op.drop_column('atualizado_em')
        batch_op.drop_column('criado_em')

    # ### end Alembic commands ###