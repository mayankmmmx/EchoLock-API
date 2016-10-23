from pymongo import MongoClient

def create_request(request):
    key = request.get("api_key")

    client = MongoClient()

    db = client.test
    users = db.users

    users.update(
            {"api_key": key},
            { "$set":
                {
                    "can_log_in": True,
                }
            }
        )
    

    return ["-1", "Authentication Failed!"]

def respond(data):
	message = create_request(data)
	return {
		'status': message[0],
        'message': message[1]
	}