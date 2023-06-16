from flask import Flask, Response, jsonify, request
from .errors import errors
from .functions import makeDict 

app = Flask(__name__)
app.register_blueprint(errors)

@app.route("/")
def index():
    return Response("Hello, world, word3!", status=200)


@app.route("/vowel_count", methods=["POST"])
def vowel_count():
    payload = request.get_json()
    dict_vowel_count = makeDict(payload)
    return dict_vowel_count


@app.route("/health")
def health():
    return Response("OK", status=200)
