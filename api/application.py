# hack for harambe
from flask import Flask, Response, request, jsonify, Response
import Routes.register
import Routes.login
import Routes.add_site

application = Flask(__name__)

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
        resp = jsonify(Routes.login.respond(request.get_json()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

@application.route('/harambe/add_site', methods=['POST', ])
def add_site():
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(Routes.add_site.respond(request.get_json()))

if __name__ == "__main__":
    application.run(debug=True)