from flask import Flask, json, request
from flask_cors import cross_origin

app = Flask(__name__)

@app.route("/")
@cross_origin()
def hello():
    return "Hello World!"

@app.route("/quiz", methods=['POST'])
@cross_origin()
def new_quiz():
    print(request.get_json())
    return json.dumps({ 'msg': 'Created' })
