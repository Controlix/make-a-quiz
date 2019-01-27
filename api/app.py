from flask import Flask, json, request, jsonify
from flask_cors import cross_origin, CORS
from flask_jwt_extended import create_access_token, create_refresh_token, JWTManager, jwt_required, jwt_refresh_token_required, get_jwt_identity
from flask_bcrypt import Bcrypt
from quiz import Quiz, Question
from user import User
from datetime import timedelta
import pymongo

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=1)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
CORS(app)

client = pymongo.MongoClient("mongodb://localhost:27017/", username="root", password="example", authSource="admin")
db = client["make_a_quiz"]
quizes = db[ "quiz"]
users = db["user"]

toJSON = lambda o: o.__dict__

@app.route("/quiz")
@jwt_required
def all_quizes():
    result = list(map(Quiz.fromDict, quizes.find()))

    return app.response_class(
        response=json.dumps(result, default=toJSON),
        status=200,
        mimetype='application/json'
    )

@app.route("/quiz/<name>")
def one_quiz(name):
    result = Quiz.fromDict(quizes.find_one({ 'name': name }))

    return app.response_class(
        response=json.dumps(result, default=toJSON),
        status=200,
        mimetype='application/json'
    )

@app.route("/quiz/<name>/questions")
def ask_quiz(name):
    result = Quiz.fromDict(quizes.find_one({ 'name': name })).questions()

    return app.response_class(
        response=json.dumps(result, default=toJSON),
        status=200,
        mimetype='application/json'
    )

@app.route("/quiz", methods=['POST'])
def new_quiz():
    quiz = Quiz.fromDict(request.get_json())
    quizes.insert_one(json.loads(json.dumps(quiz, default=toJSON)))

    return app.response_class(
        status=201,
        headers=[('location', '/quiz/' + quiz.name)]
        )

@app.route("/login", methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = users.find_one({ 'username': username })
    if not user:
        return jsonify({"msg": "Bad username or password"}), 401

    pwd = User.fromDict(user).password
    if not bcrypt.check_password_hash(pwd, password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    return jsonify(access_token=access_token, refresh_token=refresh_token), 200


@app.route("/refresh")
@jwt_refresh_token_required
def refresh():
    username = get_jwt_identity()
    print("Refresh token for " + username)
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route("/register", methods=['POST'])
def new_user():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = users.find_one({ 'username': username })
    if user:
        return jsonify({"msg": "Bad username or password"}), 400

    pwd = bcrypt.generate_password_hash(password).decode("utf-8")
    user = User(username, pwd)
    users.insert_one(json.loads(json.dumps(user, default=toJSON)))

    return app.response_class(
        status=201,
        headers=[('location', '/user/' + user.username)]
        )
