# APRESENTO... O  P I O R  CÓDIGO DO MUNDO, EM TODOS OS CRITÉRIOS, PORQUE O PROFESSOR TEM UMA METODOLOGIA RUIM DE ENSINO

from flask import Flask, Blueprint, current_app
from sqlalchemy import db

app = Flask(__name__)

#Fase de configuração
app.config['FOO'] = 'bar'
app.config['NAME_APP'] = 'delivery'
app.config['EXEMPLO'] = 'meu exemplo'

#Registro de rotas
app.route('/')
app.add_url_rule('/', 'teste')

#Registro dos blueprint
app.register_blueprint('name_blueprint')

#Registro dos métodos de autenticação
# admin = Admin(app)
admin.init_app(app)
db.init_app(app)

#Registro de hooks
@app.before_request
def before():
    pass

@app.errorhandler(404)
def not_found(error):
    return 'Nao encontrado', 404

#Registro de factories secundarias
views.init_app(app) #Ele está usando um objeto/modulo que não foi importado nem existe, como sempre
extension.init_app(app)

#Contexto de aplicação

#Criar uma extensão
from flask import current_app

def exemplo():
    valor = current_app.config['FOO']
    return valor

#Contexto de request
#cabecalhos http
#parametros URL
#validar dados de formularios
#sessoes (db, cliente)
#objeto request

from flask import request

@app.route('/')
def hello():
    name = request.args.get('nome')
    return f'Ola, {name}'
