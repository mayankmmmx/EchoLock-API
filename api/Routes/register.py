from pymongo import MongoClient
import random
import string

def create_request(request):
    username = request.get("login_username")
    password = request.get("login_password")
    client = MongoClient()

    db = client.test
    users = db.users

    register_obj = {
        "api_key" : create_auth_token(),
        "login_username" : username,
        "login_password" : password,
        "sites" : [],
        "logged_in": [],
    }

    if(users.find_one({"login_username" : username}) == None):
        users.insert_one(register_obj)
        return ["0", register_obj["api_key"]]

    #This username already exists
    else:
        return ["-1", "ERROR: username already exists"]

def create_auth_token():
    auth_token = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(30))
    return auth_token

def respond(data):
	message = create_request(data)

	return {
        'status': message[0],
		'api_key': message[1]
	}
