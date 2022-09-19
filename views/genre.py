# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

from dao.model.mod_genre import genres_schema, genre_schema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        result = genre_service.get_genres()
        return genres_schema.dump(result)


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        result = genre_service.get_genre(gid)
        return genre_schema.dump(result)

