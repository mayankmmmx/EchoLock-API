from pymongo import MongoClient

def create_request(request):
    key = request.get("api_key")

    client = MongoClient()

    db = client.test
    users = db.users

    response = users.find_one({"api_key": key})

    if response["can_log_in"]:
        site = response["logged_in"][0]
        users.update(
            {"api_key": key},
            { "$set":
                {
                    "can_log_in": False,
                    "logged_in": []
                }
            }
        )
        return ["0", site["site_username"], site["site_password"]]
    

    return ["-1", "Sorry, not found!"]

def respond(data):
	message = create_request(data)
	return {
		'status': message[0],
        'username': message[1],
        'password': message[2]
	}