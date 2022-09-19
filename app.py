# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение


from flask import Flask
from flask_restx import Api

from config import Config
from constants import PUTH

from dao.data import migrate_from_http
from setup_db import db

from views.director import director_ns
from views.genre import genre_ns
from views.movie import movie_ns


def create_data(app, db):
    with app.app_context():
        db.create_all()
        migrate_from_http(PUTH)  # эта функция берет данные из url, можно воспользоваться и migrate_data из той же папки


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


app = create_app(Config())

if __name__ == '__main__':
    app.run(host="localhost", port=5000)
