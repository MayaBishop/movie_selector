import requests
import json


# need to be able to make enviroment pipenv
# x = 0
# w = 0
# s = 0xb5ad4eceda1ce2a9
#
#
# def randomNum():
#     nonlocal x, w, s
#     x *= x
#     w += s
#     x += w
#     x = x << 32 | x >> 32
#     return x

def getType(string):
    if string.lower() == "g":
        return "Genre"
    if string.lower() == "a":
        return "Actor/Actress"
    if string.lower() == "y":
        return "Year"
    return ""


def callAPI(call_type, add_ons):
    api_token = '2496fe73d7cabf4f2293e65f4af6b962'
    api_url_base = 'https://api.themoviedb.org/3/'
    api_url = '{}{}?api_key={}{}'.format(api_url_base, call_type, api_token,add_ons)
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    return None


#   https://api.themoviedb.org/3/genre/movie/list?api_key=2496fe73d7cabf4f2293e65f4af6b962&language=en-US
#   reverse engineer create dictionary with id as value and name as key
def getGenres():
    json = callAPI('genre/movie/list', '')
    genres = json
    return genres

def main():
    api_token = '2496fe73d7cabf4f2293e65f4af6b962'
    api_url_base = 'https://api.themoviedb.org/3/'
    discover = 'discover/movie'
    api_url = '{}{}?api_key={}&page=1'.format(api_url_base, discover, api_token)
    type = input("What way do you want to select a Movie?\n Genre(G), Actor/Actress(A), Year(Y): ")
    type = getType(type)
    if type != "":
        type.lower() == "g"
        value = input("What {} do you want to search for? : ".format(type))
        print(type, ":", value)
        print(callAPI('discover/movie',''))
        print(getGenres())


main()
