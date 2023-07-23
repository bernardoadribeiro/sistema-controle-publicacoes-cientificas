# Sistema de Controle de Publicações Científicas

Este projeto consiste em uma proposta de sistema para Controle de publicações científicas para o IFNMG Campus Januária, como meio para facilitar o acesso às publicações científicas produzidas por discentes e docentes do campus.

Além disso, o sistema busca facilitar a obteção de insights sobre as publicações por meio de relatórios que serão criados para as diferentes partes interessadas.

### Como rodar a aplicação
> Rode os seguintes comandos na pasta raiz do projeto para rodar a aplicação.

Antes de prosseguir, é preciso que você tenha o servidor MySQL instalado e configurado na sua máquina. 

> Caso esteja usando Windows, recomendo utilizar o [XAMPP](https://www.apachefriends.org/pt_br/download.html).

> Caso esteja usando Linux, instale o MySQL Server na sua máquina. [Aqui um tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04-pt) de como fazer isso.

**Commands:**
- Criar `.env` baseado no `.env.dist`: `cp .env.dist .env`
- Rodar as migrations: `flask db upgrade`
- Iniciar a aplicação: `flask run`

**Migrations**
> Use os comandos abaixo quando precisar gerenciar as migrations:

> Formato do comando: `flask db [OPTIONS] COMMAND [ARGS]...`
- `flask db init`: inicia diretorio de migrations do app e faz o setup do alembic
- `flask db migrate -m "<message>"`: gera uma nova migration com base nas alterações nos `models``.
- `flask db [upgrade|downgrade]`: para up/down mudanças das migrations geradas.
- `flask db --help`: Mostra mensagem de ajuda.


### **URLs**
- Flask App: http://localhost:8000/

### Referências
- [Flask doc](https://flask.palletsprojects.com/en/2.2.x/)
- [About Flask app environment configuration](https://flask.palletsprojects.com/en/2.2.x/config/)
- [Flask SQLAlchemy doc](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)

---

_* ℹ️ INFO: Este Projeto foi desenvolvido durante a disciplina de Gerência de Projetos, ofertada no Curso de Bacharelado de Sistemas de Informação do IFNMG Campus Januária. O projeto tem como objetivo a aplicação prática da gerência de projeto em uma equipe de desenvolvimento composta por um Scrum Master e quatro desenvolvedores._

_* ⚠️ AVISO: Este projeto está em desenvolvimento, então pode conter bugs e/ou não conter todas as funcionalidades especificadas._

