# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

from dao.model.mod_director import directors_schema, director_schema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        result = director_service.get_directors()
        if not result:
            return "Ничего не найдено", 404
        else:
            return directors_schema.dump(result)


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        result = director_service.get_director(did)
        if not result:
            return "Ничего не найдено",404
        else:
            return director_schema.dump(result)
