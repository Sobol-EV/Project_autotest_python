import json
import signal
from flask import Flask, jsonify, request

from error_classes import ServerTerminationError
from settings import MOCK_HOST, MOCK_PORT

app = Flask(__name__)

user_data = {}


def exit_gracefully(signum, frame):
    print("Exit Gracefully called")
    raise ServerTerminationError()


signal.signal(signal.SIGINT, exit_gracefully)
# sigterm отправляется командой docker stop
signal.signal(signal.SIGTERM, exit_gracefully)


@app.route('/vk_id/add_user', methods=['POST'])
def add_user():
    username = json.loads(request.data)['username']
    vk_id = json.loads(request.data)['vk_id']
    if username not in user_data:
        user_data[username] = vk_id
        return jsonify({'user_id': user_data[username]}), 201
    else:
        return jsonify(f'User {username} already '
                       f'exists: id: {user_data[username]}'
                       ), 400


@app.route('/vk_id/<username>', methods=['GET'])
def get_vk_id(username):
    if user_id := user_data.get(username):
        payload = {'vk_id': str(user_id)}
        return jsonify(payload), 200
    else:
        return jsonify({}), 404


if __name__ == '__main__':
    try:
        app.run(MOCK_HOST, MOCK_PORT)
    except ServerTerminationError as e:
        print("Stopped Server")
