from random import randint


PATH_TO_INPUT_FILMS = "input_1.txt"
PATH_TO_INPUT_USERS = "input_2.txt"


class User(list):
    def __init__(self, user_films):
        super().__init__()
        self.films = user_films


class Film:
    def __init__(self, film_title):
        self.title = film_title


class User_DB(list):
    def __init__(self, users_path):
        super().__init__()
        self.users = self.__load_users(users_path)

    def __load_users(self, users_path):
        users = []
        with open(users_path, "r", encoding="UTF-8") as f:
            for line in f:
                users.append(User([int(film_id) for film_id in line.strip().split(",")]))
        return users

    def get_all(self):
        return self.users


class Film_DB(dict):
    def __init__(self, films_path):
        super().__init__()
        self.films = self.__load_films(films_path)

    def __load_films(self, films_path):
        films = {}
        with open(films_path, "r", encoding="UTF-8") as f:
            for line in f:
                film_id, film_title = line.strip().split(",")
                films[int(film_id)] = Film(film_title)
        return films

    def get_all(self):
        return self.films


def recommend_film(films, persons, current_user):
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


film_db = Film_DB(PATH_TO_INPUT_FILMS)
user_db = User_DB(PATH_TO_INPUT_USERS)

current_user = User([int(film_id) for film_id in input().split(",")])

recommended_movie = recommend_film(film_db.get_all(), user_db.get_all(), current_user)
print(recommended_movie)