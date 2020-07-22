import requests
import json
import get_people_json
import random

types = {"g": "Genre", "a": "Actor/Actress", "y": "Year"}
previous_movies = {}
genres = {}



def get_type(string):
    string = string.replace(" ", "")
    type_list = []
    for s in string.split(","):
        if s.lower() in types:
            type_list.append(s.lower())
    return type_list


def call_api(call_type, add_ons):
    api_token = '2496fe73d7cabf4f2293e65f4af6b962'
    api_url_base = 'https://api.themoviedb.org/3/'
    api_url = '{}{}?api_key={}&page=1&include_adult=false{}'.format(api_url_base, call_type, api_token, add_ons)
    print(api_url)
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    return None


#   https://api.themoviedb.org/3/genre/movie/list?api_key=2496fe73d7cabf4f2293e65f4af6b962&language=en-US
#   reverse engineer api call create dictionary with id as value and name as key
def get_genres():
    global genres
    apiResponse = call_api('genre/movie/list', '')
    genres = {}
    listOfGenres = apiResponse['genres']
    for i in range(len(listOfGenres)):
        genres[listOfGenres[i]['name'].lower()] = listOfGenres[i]['id']
    return genres


def get_movie(discover, add_ons):
    movies = call_api(discover, add_ons)['results']
    if len(movies) > 0:
        global previous_movies
        num = random.randint(0, len(movies) - 1)
        while num in previous_movies and len(previous_movies) < len(movies):
            num = random.randint(0, len(movies) - 1)
        if len(previous_movies) >= len(movies):
            return "No movies left"
        previous_movies[num] = movies[num]['title']
        movie = movies[num]
        return movie
    return ""


def reset_previous_movies():
    global previous_movies
    previous_movies = {}


def get_addons(genre, actor, year):
    global previous_movies
    discover = 'discover/movie'
    genres_add_on_root = '&with_genres='
    years_add_on_root = '&primary_release_year='
    people_add_on_root = '&with_cast='
    people = {}
    add_ons = ""
    print("genre:", genre)
    print("actor/actress:", actor)
    print("year:", year)
    if genre != "":
        if not bool(genres):
            get_genres()
        add_ons += genres_add_on_root + str(genres[genre.lower()])
    else:
        print("Genre not available")
    if year != "":  # 1874 lowest
        add_ons += years_add_on_root + year
    if actor != "":
        if len(people) == 0:
            people = get_people_json.get_people()
        if actor in people:
            add_ons += people_add_on_root + str(people[actor])
    else:
        print("Actor/Actress not available")
    return discover, add_ons
