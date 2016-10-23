# hack for harambe
from flask import Flask, Response, request, jsonify
from flask_socketio import SocketIO, send, emit
application = Flask(__name__)
socketio = SocketIO(application)

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


@socketio.on('value changed')
def value_changed(message):
    print(message)
    emit('update value', "temp", broadcast=True)


if __name__ == "__main__":
    application.run(debug=True)
    socketio.run(application)