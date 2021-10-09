from flask import Flask, jsonify, request
from DoorManager import DoorManager
from Repository import Repository
from flask_httpauth import HTTPBasicAuth
import os

user = HTTPBasicAuth()
superuser = HTTPBasicAuth()
superuser_password = None
app = Flask(__name__)
door = None
repo = None


@superuser.verify_password
def verify_superuser(username, password):
    if superuser_password is not None:
        if superuser_password == password:
            return True
    return False


@user.verify_password
def verify_user(username, password):
    if verify_superuser(username, password):
        return True
    # FIXME: return repo.is_authorized(password)
    return True


@app.route("/favicon.ico", methods=['GET'])
def noFavicon():
    return ""


@app.route("/")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/unlock", methods=['POST'])
@user.login_required
def unlock():
    door.unlock()
    return jsonify({
        "status": "ok"
    })


@app.route("/is_unlocked", methods=['GET'])
@user.login_required
def isUnlocked():
    return jsonify({
        "status": "ok",
        "unlocked": door.isUnlocked()
    })


@app.route("/add_card", methods=['POST'])
@superuser.login_required
def add_card():
    data = request.get_json()
    repo.add_card(data.username, data.password)
    return jsonify({
        "status": "ok"
    })


def load_superuser_password():
    filename = "superuser_password.txt"
    if not os.path.isfile(filename):
        return None
    with open(filename) as f:
        content = f.read().splitlines()
    return content[0]


if __name__ == '__main__':
    superuser_password = load_superuser_password()
    repo = Repository("doors.db")
    door = DoorManager()
    door.start()
    app.run(debug=True)
