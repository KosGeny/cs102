import os

from random import randint


file_dir = os.path.dirname(os.path.realpath("__file__"))
PATH_TO_INPUT_FILMS = os.path.join(file_dir, "films.txt")

file_dir = os.path.dirname(os.path.realpath("__file__"))
PATH_TO_INPUT_USERS = os.path.join(file_dir, "users.txt")


class User(list):
    def __init__(self, user_films):
        super().__init__()
        self.films = user_films


class Film:
    def __init__(self, film_title):
        self.title = film_title


class User_DB(list):
    def __init__(self):
        super().__init__()
        self.users = self.__load_users()

    def __load_users(self):
        users = []
        with open(PATH_TO_INPUT_USERS, "r", encoding="UTF-8") as f:
            for line in f:
                users.append(User([int(film_id) for film_id in line.strip().split(",")]))
        return users

    def get_all(self):
        """Функция возвращает список пользователей с их просмотренными фильмами"""
        return self.users


class Film_DB(dict):
    def __init__(self):
        super().__init__()
        self.films = self.__load_films()

    def __load_films(self):
        films = {}
        with open(PATH_TO_INPUT_FILMS, "r", encoding="UTF-8") as f:
            for line in f:
                film_id, film_title = line.strip().split(",")
                films[int(film_id)] = Film(film_title)
        return films

    def get_all(self):
        """Функция возвращает список всех id фильмов"""
        return self.films


def recommend_film(films, persons, current_user):
    """Функция возвращает название рекомендованного фильма или сообщение об отсутствии рекомендаций"""
    film_views_count = {}

    user_films = set(current_user.films)

    for person in persons:
        person_films = set(person.films)
        if 2 * len(person_films & user_films) >= len(user_films):
            for film_id in person_films:
                if film_id not in user_films:
                    if film_id in film_views_count:
                        film_views_count[film_id] += 1
                    else:
                        film_views_count[film_id] = 1

    if not film_views_count:
        return "No recommendations found."

    max_views = max(film_views_count.values())
    top_movies = [movie_id for movie_id, count in film_views_count.items() if count == max_views]
    recommended_movie_id = top_movies[randint(0, len(top_movies) - 1)]
    return films[recommended_movie_id].title

if __name__ == "__main__":
    film_db = Film_DB()
    user_db = User_DB()

    current_user = User([int(film_id) for film_id in input().split(",")])

    recommended_movie = recommend_film(film_db.get_all(), user_db.get_all(), current_user)
    print(recommended_movie)