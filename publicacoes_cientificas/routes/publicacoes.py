from flask import Blueprint, render_template, request, flash


publicacoes_bp = Blueprint(
    'publicacoes', __name__,
    template_folder='templates'
)


# @publicacoes_bp.route('/')
# def listar_publicacoes():
#     publicacoes = Publicacoes.query.all()
#     return render_template('listar_publicacoes.html', publicacoes=publicacoes)


@publicacoes_bp.route('nova-publicacao/', methods=['GET', 'POST'])
def nova_publicacao():
    """ Formulario para insercao de nova publicacao """

    if request.method == 'POST':
        # insere nova publicacao [TO-DO]
        titulo = request.form.get('titulo')
        autor_principal = request.form.get('autor_principal')
        orientador = request.form.get('orientador')
        coorientador = request.form.get('coorientador')
        citacao = request.form.get('citacao')
        url = request.form.get('url')
        resumo = request.form.get('resumo')
        abstract = request.form.get('abstract')
        assunto = request.form.get('assunto')
        lingua = request.form.get('lingua')
        pub_tipo = request.form.get('pub_tipo')
        colecao = request.form.get('colecao')
        ifnmg_campus = request.form.get('ifnmg_campus')
        curso = request.form.get('curso')
        qtd_paginas = request.form.get('qtd_paginas')

        from ..models.Publicacoes import Publicacoes, db
        nova_publicacao = Publicacoes(
            titulo=titulo,
            autor_principal=autor_principal,
            orientador=orientador,
            coorientador=coorientador,
            citacao=citacao,
            url=url,
            resumo=resumo,
            abstract=abstract,
            assunto=assunto,
            lingua=lingua,
            pub_tipo=pub_tipo,
            colecao=colecao,
            ifnmg_campus=ifnmg_campus,
            curso=curso,
            qtd_paginas=qtd_paginas
        )

        db.session.add(nova_publicacao)
        db.session.commit()

        flash('Publicação created!', category='success')

    return render_template('publicacoes/nova-publicacao.html')


# @publicacoes_bp.route('/publicacao/<int:publicacao_id>')
# def ver_publicacao(publicacao_id):
#     publicacao = Publicacoes.query.get_or_404(publicacao_id)

#     return render_template('ver_publicacao.html', publicacao=publicacao)


# @publicacoes_bp.route('/publicacao/<int:publicacao_id>/editar', methods=['GET', 'PATCH'])
# def editar_publicacao(publicacao_id):
#     publicacao = Publicacoes.query.get_or_404(publicacao_id)

#     if request.method == 'PATCH':
#         publicacao.titulo = request.form['titulo']
#         publicacao.autor_principal = request.form['autor_principal']
#         publicacao.orientador = request.form['orientador']
#         publicacao.coorientador = request.form['coorientador']
#         publicacao.citacao = request.form['citacao']
#         publicacao.url = request.form['url']
#         publicacao.resumo = request.form['resumo']
#         publicacao.abstract = request.form['abstract']
#         publicacao.assunto = request.form['assunto']
#         publicacao.lingua = request.form['lingua']
#         publicacao.pub_tipo = request.form['pub_tipo']
#         publicacao.colecao = request.form['colecao']
#         publicacao.ifnmg_campus = request.form['ifnmg_campus']
#         publicacao.curso = request.form['curso']
#         publicacao.qtd_paginas = request.form['qtd_paginas']

#         db.session.commit()

#     render_template('ver_publicacao.html', publicacao=publicacao)


# @publicacoes_bp.route('/publicacao/<int:publicacao_id>/excluir', methods=['POST'])
# def excluir_publicacao(publicacao_id):
#     publicacao = Publicacoes.query.get_or_404(publicacao_id)
#     db.session.delete(publicacao)
#     db.session.commit()

#     return render_template('publicacoes/index.html')
