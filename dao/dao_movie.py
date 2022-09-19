# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой, с базой мы работает в классе DAO)
from dao.model.mod_movie import Movie


class MovieDao:
    def __init__(self, session):
        self.session = session
        
    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all_by_dir(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id)

    def get_all_by_gen(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id)

    def get_all_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def update(self, movie):
        try:
            self.session.add(movie)
            self.session.commit()
        except Exception as e:
            return e
        return True

    def create(self, data):
        try:
            movie = Movie(**data)
            self.session.add(movie)
            self.session.commit()
        except Exception as e:
            return e
        return True

    def delete(self, mid):
        try:
            movie = self.get_one(mid)
            self.session.delete(movie)
            self.session.commit()
        except Exception as e:
            return e
        return True


