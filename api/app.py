from flask import Flask, json, request
from flask_cors import cross_origin
import pymongo

app = Flask(__name__)

class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add(self, question):
        self.questions.append(question)

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

toJSON = lambda o: o.__dict__

quizes = [Quiz("A New Quiz"), Quiz("The Return of the Chokotofs")]
q1 = Question("Where do pinguins live?", "On the south pole.")
quizes[0].add(q1)


@app.route("/quiz")
@cross_origin()
def all_quizes():
    return json.dumps(quizes, default=toJSON)

@app.route("/quiz", methods=['POST'])
@cross_origin()
def new_quiz():
    print(request.get_json())
    return json.dumps({ 'msg': 'Created' })
