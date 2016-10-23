from pymongo import MongoClient

def create_request(request):
    key = request.get("api_key")
    name = request.get("site_name")

    client = MongoClient()

    db = client.test
    users = db.users

    response = users.find_one({"api_key": key})
    for site in response["logged_in"]:
        if site["site_name"] == name:
            return ["0", "Would you like to log into " + str(name)]

    return ["-1", "Site not found!"]

def respond(data):
	message = create_request(data)
	return {
		'status': message[0],
        'message': message[1]
	}