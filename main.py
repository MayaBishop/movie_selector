import requests
import json
import get_people_json
import random


types = {"g":"Genre", "a":"Actor/Actress", "y":"Year"}
previous_movies = {}

def getType(string):
    string = string.replace(" ","")
    type_list = []
    for s in string.split(","):
        if s.lower() in types:
            type_list.append(s.lower())
    return type_list


def callAPI(call_type, add_ons):
    api_token = '2496fe73d7cabf4f2293e65f4af6b962'
    api_url_base = 'https://api.themoviedb.org/3/'
    api_url = '{}{}?api_key={}&page=1&include_adult=false{}'.format(api_url_base, call_type, api_token,  add_ons)
    print(api_url)
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    return None


#   https://api.themoviedb.org/3/genre/movie/list?api_key=2496fe73d7cabf4f2293e65f4af6b962&language=en-US
#   reverse engineer api call create dictionary with id as value and name as key
def getGenres():
    apiResponse = callAPI('genre/movie/list', '')
    genres = {}
    listOfGenres = apiResponse['genres']
    for i in range(len(listOfGenres)):
        genres[listOfGenres[i]['name'].lower()] = listOfGenres[i]['id']
    return genres

def getMovie(discover, add_ons):
    while True:
        movies = callAPI(discover, add_ons)['results']
        if len(movies) > 0:
            global previous_movies
            num = random.randint(0, len(movies) - 1)
            while num in previous_movies and len(previous_movies) < len(movies):
                num = random.randint(0, len(movies) - 1)
            if len(previous_movies) >= len(movies):
                return "No movies left"
            previous_movies[num] = movies[num]['title']
            movie = movies[num]
            if movie == "No movies left":
                print(movie)
                break
            print(movie['title'], ":", movie['overview'])
        else:
            print("Search not available")
            break
        acceptable = input("Would you another movie?(is so type Y) ")
        if acceptable.lower() != "y":
            break



def getAddons(genre, actor, year):
    global previous_movies
    discover = 'discover/movie'
    genres_add_on_root = '&with_genres='
    years_add_on_root = '&primary_release_year='
    people_add_on_root = '&with_cast='
    people = {}
    input_value = input("What way do you want to select a Movie?\n Genre(G), Actor/Actress(A), Year(Y): ")
    while input_value != "q":
        type = getType(input_value)
        add_ons = ""
        for t in type:
            if t.lower() == "g":
                genres = getGenres()
                print(list(genres.keys()))
            value = input("What {} do you want to search for? : ".format(types[t]))
            print(types[t], ":", value)
            if t.lower() == "g":
                if value.lower() in genres:
                    #print(genres[value.lower()])
                    add_ons += genres_add_on_root + str(genres[value.lower()])
                else:
                    print("Genre not available")
            elif t.lower() == "y":#1874 lowest
                add_ons += years_add_on_root + value
            elif t.lower() == "a":
                if len(people) == 0:
                    people = get_people_json.get_people()
                if value in people:
                    add_ons += people_add_on_root + str(people[value])
                else:
                    print("Actor/Actress not available")
        #THING TO ADD CIRCLE THROUGH MOVIES ARE RANDOM
        getMovie(discover, add_ons)
        input_value = input("\nWhat way do you want to select a Movie?\n Genre(G), Actor/Actress(A), Year(Y): ")
        previous_movies = {}


