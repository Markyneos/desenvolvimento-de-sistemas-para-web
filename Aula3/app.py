import views
from flask import Flask

def create_app():
    #Factory principal
    app = Flask(__name__)
    views.init_app(app)
    return app

if __name__ == "__main__":
    create_app()
