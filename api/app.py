from flask import Flask, json, request
from flask_cors import cross_origin
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/", username="root", password="example", authSource="admin")
db = client["make_a_quiz"]

class Quiz:
    def __init__(self, name, questions=[]):
        self.name = name
        self.questions = questions

    def add(self, question):
        self.questions.append(question)

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

toJSON = lambda o: o.__dict__

q1 = Question("Where do pinguins live?", "On the south pole.")
quizes = [Quiz("A New Quiz", q1), Quiz("The Return of the Chokotofs")]


@app.route("/quiz")
@cross_origin()
def all_quizes():
    result = []
    print(db["quiz"].find())
    for quiz in db["quiz"].find():
        toAdd = Quiz(quiz['name'])
        for question in quiz['questions']:
            toAdd.add(Question(question['text'], question['answer']))
        result.append(toAdd)

    return json.dumps(result, default=toJSON)

@app.route("/quiz", methods=['POST'])
@cross_origin()
def new_quiz():
    print(request.get_json())
    return json.dumps({ 'msg': 'Created' })
