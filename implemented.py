# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.dao_director import DirectorDao
from dao.dao_genre import GenreDao
from dao.dao_movie import MovieDao
from service.director_service import DirectorService
from service.genre_service import GenreService
from service.movie_service import MovieService
from setup_db import db

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDao(db.session)
genre_service = GenreService(genre_dao)

