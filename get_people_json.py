import json
#http://files.tmdb.org/p/exports/person_ids_MM_DD_YYYY.json.gz
def get_people():
    date = "07-06-2020"
    file = open('person_ids_07_06_2020.json')
    people = {}
    jsondata = json.load(file)["data"]
    for i in jsondata:
        people[i["name"]] = i["id"]
    file.close()
    return people