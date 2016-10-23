from pymongo import MongoClient

def create_request(request):
    key = request.get("api_key")
    name = request.get("site_name")
    password = request.get("site_password")
    username = request.get("site_username")

    client = MongoClient()

    db = client.test
    users = db.users

    #account already added
    if (users.find_one({"api_key": key, "sites" : [{"site_name" : name}]})):
        return ["-1", "Error: this account is already added"]

    else:
        users.update_one(
            {"api_key": key},
            {"$push":
                {"sites" : {
                    "site_name" : name,
                    "site_username" : username,
                    "site_password" : password
                    }
                }
            }
        )

    return ["0", "Site added successfully!"]

def respond(data):
	message = create_request(data)
	return {
		'status': message[0],
        'message': message[1]
	}