import requests
from tinydb import TinyDB

base_url = "https://randomuser.me/api/"
db = TinyDB("data.json",indent = 4)
def get_users(gender: str, n: int):
    payload = {
        "results":n,
        "gender":gender,
    }
    respons = requests.get(base_url, params=payload)

    if respons.status_code==200:
        users = []
        for i in respons.json()['results']:
            users.append({
                "first_name":i['name']['first'],
                "last_name":i['name']['last'],
                "age":i['dob']['age'],
                "phone":i['phone'],
                "country":i['location']['country'],
                "email":i['email'],
            })
        
        return users
    else:
        return []
    
male = db.table("males")
female = db.table("females")
male.insert_multiple(get_users('male',3000))
female.insert_multiple(get_users('female',3000))

