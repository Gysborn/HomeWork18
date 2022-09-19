from dao.dao_director import DirectorDao


class DirectorService:
    def __init__(self, director_dao: DirectorDao):
        self.director_dao = director_dao

    def get_directors(self):
        result = self.director_dao.get_all()
        if not result:
            return False
        else:
            return result

    def get_director(self, mid):
        return self.director_dao.get_one(mid)

