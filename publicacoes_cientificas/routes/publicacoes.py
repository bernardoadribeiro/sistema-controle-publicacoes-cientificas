from flask import Blueprint, render_template, request

publicacoes_bp = Blueprint(
    'publicacoes', __name__,
    template_folder='templates'
)


@publicacoes_bp.route('nova-publicacao/', methods=['GET', 'POST'])
def nova_publicacao():
    """ Formulario para insercao de nova publicacao """

    if request.method == 'POST':
        # insere nova publicacao [TO-DO]
        pass

    return render_template('publicacoes/nova-publicacao.html')
