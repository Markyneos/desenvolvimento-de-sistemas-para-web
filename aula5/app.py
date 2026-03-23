from flask import Flask
from views import init_app as init_main

def create_app():
    app = Flask(__name__)

    init_main(app)

    return app
