# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from dao.dao_movie import MovieDao


class MovieService:
    def __init__(self, movie_dao: MovieDao):
        self.movie_dao = movie_dao

    def get_movies(self):
        return self.movie_dao.get_all()

    def get_movie(self, mid):
        return self.movie_dao.get_one(mid)

    def get_movies_by_dir(self, director_id):
        return self.movie_dao.get_all_by_dir(director_id)

    def get_movies_by_genre(self, genre_id):
        return self.movie_dao.get_all_by_gen(genre_id)

    def get_movies_by_year(self, year):
        return self.movie_dao.get_all_by_year(year)

    def add_movie(self, data):
        return self.movie_dao.create(data)

    def update_put(self, data, mid):
        movie = self.movie_dao.get_one(mid)
        [setattr(movie, k, v) for k, v in data.items()]
        return self.movie_dao.update(movie)

    def update_patch(self, data, mid):
        movie = self.movie_dao.get_one(mid)
        [setattr(movie, k, v) for k, v in data.items()]
        return self.movie_dao.update(movie)

    def delete(self, mid):
        return self.movie_dao.delete(mid)


