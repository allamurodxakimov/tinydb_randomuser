from tinydb import TinyDB
from tinydb.database import Document
from api import url
import json
db = TinyDB('data.json',indent = 9)
def update():
    data = url()
    if (len(data))!=0:
        return data['results'][0]
    return False
def get_user(data):
    data = update()
    if data!=False:
        users = {
            "gender":data['gender'],
            "first_name":data['name']['first'],
            "last_name":data['name']['last'],
            "age":data['dob']['age'],
            "phone":data['phone'],
            "country":data['location']['country'],
            "email":data['email'],

        }
        return users
    else:
        return False

def add_user(data, quantity,gender1,gender2):
    a = 0
    b = 0
    while quantity!=a:
        
        get_data = get_user(data)
        if get_data["gender"] == gender1:
            users = db.table("users_male")
            
            users.insert(get_data)
            a+=1
    while quantity!=b:
        get_data = get_user(data)
        if get_data['gender'] ==gender2:
            users = db.table("users_female")

            users.insert(get_data)
            b+=1
    users.all()


    return "Accept"
    
data = update()

print(add_user(data,30,gender1="male",gender2="female"))
