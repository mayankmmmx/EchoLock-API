from pymongo import MongoClient
import random
import string

def create_request(request):
    username = request.get("login_username")
    password = request.get("login_password")
    client = MongoClient()

    db = client.test
    users = db.users


    if(users.find_one({"login_username" : username}) == None):
        return ["-1", "Error: user does not exist"]

    elif(users.find_one({"login_username" : username, "login_password" : password}) == None):
        return ["-1", "Error: incorrect password"]

    else:
        result = users.find_one({"login_username" : username, "login_password" : password})
        return ["0", result["api_key"]]


def respond(data):
	message = create_request(data)

	return {
        'status': message[0],
		'api_key': message[1],
	}
