from flask import Flask
#Extensão flask

def init_app(app: Flask):
    #Inicialização das extensões
    app.config['FOO'] = 'bar'

    # app.register_blueprint(foobar)
    # app.add_url_rule("/info")
    # admin = Admin(app)
    # admin.init_app(app)

    @app.before_request
    def before():
        pass

    @app.errorhandler(404)
    def not_found(error):
        return "Não encontrado", 404
    @app.route("/")
    def index():
        return "Ola, mundo!"
    @app.route("/contato")
    def contato():
        return "<form><input type='text'></form>"
