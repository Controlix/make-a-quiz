from flask import Flask, json, request
from flask_cors import cross_origin
from mongoengine import *

app = Flask(__name__)
connect('make_a_quiz', username='root', password='example', authentication_source='admin')

class Quiz(Document):
    name = StringField(required = True)
    questions = ListField(StringField())

quizes = [Quiz(name = "A New Quiz"), Quiz(name = "The Return of the Chokotofs")]
toJSON = lambda o: o.__dict__

@app.route("/quiz")
@cross_origin()
def all_quizes():
    quizes = Quiz.objects
    for quiz in quizes:
        print('============================')
        print(quiz.id)
        print(quiz.name)
        print(quiz.questions)
    return quizes
    # return json.dumps(quizes, default=toJSON)

@app.route("/quiz", methods=['POST'])
@cross_origin()
def new_quiz():
    quiz = request.get_json()
    print(quiz)
    savedQuiz = Quiz(name=quiz['name']).save()
    print(savedQuiz.id)
    return json.dumps({ 'msg': 'Created' })
