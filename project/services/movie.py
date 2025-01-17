from project.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, page):
        return self.dao.get_all(page)

    def get_new(self, page):
        return self.dao.get_new(page)

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        return self.dao.update(movie_d)

    def partially_update(self, movie_d):
        movie = self.get_one(movie_d['id'])
        if 'title' in movie_d:
            movie.title = movie_d.get('title')
        if 'description' in movie_d:
            movie.description = movie_d.get('description')
        if 'trailer' in movie_d:
            movie.trailer = movie_d.get('trailer')
        if 'year' in movie_d:
            movie.year = movie_d.get('year')
        if 'rating' in movie_d:
            movie.rating = movie_d.get('rating')
        if 'genre_id' in movie_d:
            movie.genre_id = movie_d.get('genre_id')
        if 'director_id' in movie_d:
            movie.director_id = movie_d.get('director_id')
        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
