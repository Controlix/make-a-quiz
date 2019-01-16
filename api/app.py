from flask import Flask, json, request
from flask_cors import cross_origin

app = Flask(__name__)

class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []

@app.route("/quiz")
@cross_origin()
def quizes():
    quizes = [Quiz("A New Quiz"), Quiz("The Return of the Chokotofs")]
    return json.dumps(quizes, default=lambda o: o.__dict__)

@app.route("/quiz", methods=['POST'])
@cross_origin()
def new_quiz():
    print(request.get_json())
    return json.dumps({ 'msg': 'Created' })
