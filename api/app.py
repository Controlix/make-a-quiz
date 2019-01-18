from flask import Flask, json, request, jsonify
from flask_cors import cross_origin
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/", username="root", password="example", authSource="admin")
db = client["make_a_quiz"]
quizes = db[ "quiz"]

class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add(self, question):
        self.questions.append(question)

    def __repr__(self):
        return str(self.__dict__)

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __repr__(self):
        return str(self.__dict__)

toJSON = lambda o: o.__dict__

@app.route("/quiz")
@cross_origin()
def all_quizes():
    result = []
    for quiz in quizes.find():
        result.append(quizFrom(quiz))

    return app.response_class(
        response=json.dumps(result, default=toJSON),
        status=200,
        mimetype='application/json'
    )

@app.route("/quiz", methods=['POST'])
@cross_origin()
def new_quiz():
    quiz = quizFrom(request.get_json())
    quizes.insert_one(json.loads(json.dumps(quiz, default=toJSON)))

    return json.dumps({ 'msg': 'Created' })

def quizFrom(source):
    quiz = Quiz(source['name'])

    for question in source['questions']:
        quiz.add(Question(question['text'], question['answer']))

    return quiz
