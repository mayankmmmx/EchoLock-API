# hack for harambe
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import Routes.register
import Routes.login
import Routes.add_site
import Routes.initiate_login
import Routes.poll_logged_in
import Routes.authorize
import Routes.receive_credentials

application = Flask(__name__)
CORS(application)

@application.route('/')
@application.route('/index')
def index():
    return "Welcome to EchoLock's RESTful API!"

@application.route('/harambe/register', methods=['POST'])
def register():
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(Routes.register.respond(request.get_json()))

@application.route('/harambe/login', methods=['POST'])
def login():
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(Routes.login.respond(request.get_json()))

@application.route('/harambe/add_site', methods=['POST'])
def add_site():
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(Routes.add_site.respond(request.get_json()))

@application.route('/harambe/initiate_login', methods=['POST'])
def initiate_login():
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(Routes.initiate_login.respond(request.get_json()))

@application.route('/harambe/poll_logged_in', methods=['POST'])
def poll_logged_in():
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(Routes.poll_logged_in.respond(request.get_json()))

@application.route('/harambe/authorize', methods=['POST'])
def authorize():
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(Routes.authorize.respond(request.get_json()))

@application.route('/harambe/receive_credentials', methods=['POST'])
def receive_credentials():
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(Routes.receive_credentials.respond(request.get_json()))


if __name__ == "__main__":
    application.run(debug=True)