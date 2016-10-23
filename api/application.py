# hack for harambe
from flask import Flask, Response, request, jsonify
import Routes.register
import Routes.login
import Routes.add_site

application = Flask(__name__)

@application.route('/')
@application.route('/index')
@crossdomain(origin='*')
def index():
    return "Welcome to EchoLock's RESTful API!"

@application.route('/harambe/register', methods=['POST'])
@crossdomain(origin='*')
def register():
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(Routes.register.respond(request.get_json()))

@application.route('/harambe/login', methods=['POST'])
@crossdomain(origin='*')
def login():
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(Routes.login.respond(request.get_json()))

@application.route('/harambe/add_site', methods=['POST'])
@crossdomain(origin='*')
def add_site():
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(Routes.add_site.respond(request.get_json()))

if __name__ == "__main__":
    application.run(debug=True)