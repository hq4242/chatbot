from flask import Flask

from flask import jsonify 
from flask import request

from chatbot.model_prediction import *

app = Flask(__name__)

@app.route("/conv", methods=["GET"])
def conv():
    sentence = request.args.get("sentence")
    response = jsonify(predict(sentence))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/status", methods=["GET"])
def status():
    return jsonify(True)

if("__main__" == __name__):
    app.run(host="0.0.0.0", port="80")
