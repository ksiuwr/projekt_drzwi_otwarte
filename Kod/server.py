from flask import Flask, jsonify
from DoorManager import DoorManager
from Repository import Repository
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
door = None
repo = None


@app.route("/favicon.ico")
def noFavicon():
    return ""


@app.route("/")
def health():
    return jsonify({
        "status": "ok"
    })


@auth.verify_password
def verify_password(username, password):
    return True
    # return repo.is_authorized(password)


@app.route("/unlock")
@auth.login_required
def unlock():
    door.unlock()
    return jsonify({
        "status": "ok"
    })


@app.route("/is_unlocked")
@auth.login_required
def isUnlocked():
    return jsonify({
        "status": "ok",
        "unlocked": door.isUnlocked()
    })


if __name__ == '__main__':
    repo = Repository("doors.db")
    door = DoorManager()
    door.start()
    app.run(debug=True)
