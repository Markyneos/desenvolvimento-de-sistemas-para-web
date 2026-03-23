from flask import Blueprint, current_app, render_template

bp_main = Blueprint('main', __name__)

@bp_main.route("/")
@bp_main.route("/index")
def index():
    user = {'username': "Marco"}
    current_app.logger.info("O endpoint 'index' foi acessado!")
    return render_template('main/index.html', user=user)
@bp_main.route("/listaDeMaioresCones")
def listaDeMaioresCones():
    return f'''<h1>LISTA DE MAIORES CONES</h1>
                <h2>Altoe & Rubim</h2>
                <h2>Markingo :P</h2>
                <h2>NICOLAAAAAAAAS</h2>
                <h2>Rafa Lucas da Silva</h2>
                <h2>Gustavo Ozame Goat da Silva</h2>'''
