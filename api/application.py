# hack for harambe
from flask import Flask, Response, request, jsonify
application = Flask(__name__)


@application.route('/')
@application.route('/index')
def index():
    return "Welcome to EchoLock's RESTful API!"
'''
@application.route('/harambe/diagnosis', methods=['POST'])
def route_first():
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(Routes.diagnosis.respond(request.get_json()))
'''

if __name__ == "__main__":
    application.run(debug=True)