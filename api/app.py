from flask import Flask, json, request, jsonify
from flask_cors import cross_origin
from quiz import Quiz, Question
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/", username="root", password="example", authSource="admin")
db = client["make_a_quiz"]
quizes = db[ "quiz"]

toJSON = lambda o: o.__dict__

@app.route("/quiz")
@cross_origin()
def all_quizes():
    result = list(map(Quiz.fromDict, quizes.find()))

    return app.response_class(
        response=json.dumps(result, default=toJSON),
        status=200,
        mimetype='application/json'
    )

@app.route("/quiz/<name>")
@cross_origin()
def one_quiz(name):
    result = Quiz.fromDict(quizes.find_one({ 'name': name }))

    return app.response_class(
        response=json.dumps(result, default=toJSON),
        status=200,
        mimetype='application/json'
    )

@app.route("/quiz/<name>/questions")
@cross_origin()
def ask_quiz(name):
    result = Quiz.fromDict(quizes.find_one({ 'name': name })).questions()

    return app.response_class(
        response=json.dumps(result, default=toJSON),
        status=200,
        mimetype='application/json'
    )

@app.route("/quiz", methods=['POST'])
@cross_origin()
def new_quiz():
    quiz = Quiz.fromDict(request.get_json())
    quizes.insert_one(json.loads(json.dumps(quiz, default=toJSON)))

    return app.response_class(
        status=201,
        headers=[('location', '/quiz/' + quiz.name)]
        )
