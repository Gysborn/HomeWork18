# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace

from dao.model.mod_movie import movies_schema, movie_schema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        genre_id = request.args.get("genre_id")
        if genre_id:
            result = movie_service.get_movies_by_genre(genre_id)
            return movies_schema.dump(result)

        director_id = request.args.get("director_id")
        if director_id:
            result = movie_service.get_movies_by_dir(director_id)
            return movies_schema.dump(result)

        year = request.args.get("year")
        if year:
            result = movie_service.get_movies_by_year(year)
            return movies_schema.dump(result)

        else:
            movies = movie_service.get_movies()
            return movies_schema.dump(movies)

    def post(self):
        new_movie = request.json
        result = movie_service.add_movie(new_movie)
        if result:
            return 204
        else:
            return result


@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid):
        movie = movie_service.get_movie(mid)
        return movie_schema.dump(movie)

    def put(self, mid):
        up_movie = request.json
        result = movie_service.update_put(up_movie, mid)
        if result:
            return 204
        else:
            return result

    def patch(self, mid):
        up_movie = request.json
        result = movie_service.update_patch(up_movie, mid)
        if result:
            return 204
        else:
            return result

    def delete(self, mid):
        result = movie_service.delete(mid)
        if result:
            return 204
        else:
            return result

