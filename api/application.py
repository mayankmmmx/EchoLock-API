# hack for harambe
from flask import Flask, Response, request, jsonify
from flask_socketio import SocketIO, send, emit
import Routes.register
import Routes.login
import Routes.add_site
import eventlet

application = Flask(__name__)
socketio = SocketIO(application, async_mode='eventlet')
eventlet.monkey_patch()

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

@socketio.on('value changed')
def value_changed(message):
    print(message)
    emit('update value', "temp", broadcast=True)

if __name__ == "__main__":
    application.run(debug=True)
    socketio.run(application, debug=True)
