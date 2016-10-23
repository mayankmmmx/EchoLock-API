from pymongo import MongoClient

def create_request(request):
    key = request.get("api_key")
    name = request.get("site_name")

    client = MongoClient()

    db = client.test
    users = db.users

    response = users.find_one({"api_key": key})
    for site in response["sites"]:
        if site["site_name"] == name:
            users.update_one(
                {"api_key": key},
                {"$push":
                    {"logged_in" : {
                        "site_name" : site["site_name"],
                        "site_username" : site["site_username"],
                        "site_password" : site["site_password"]
                        }
                    }
                }
            )
            return ["0", "Site found!"]

    return ["-1", "Site not found!"]

def respond(data):
	message = create_request(data)
	return {
		'status': message[0],
        'message': message[1]
	}