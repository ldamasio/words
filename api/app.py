from flask import Flask, Response, request, render_template
from .errors import errors
from .functions import makeDict, makeArray 
import json

app = Flask(__name__, template_folder='static')
app.register_blueprint(errors)

class JsonResponse(Response):
    def __init__(self, json_dict, status=200):
        super().__init__(response=json.dumps(json_dict), status=status, mimetype="application/json")

@app.route("/")
def index():
    return Response("Consulte a rota /docs para documentação e rota /health para simples ping de monitoramento da API", status=200)

@app.route("/vowel_count", methods=["POST"])
def vowel_count():
    payload = request.get_json()
    dict_vowel_count = makeDict(payload)
    return JsonResponse(dict_vowel_count)

@app.route("/sort", methods=["POST"])
def sort():
    payload = request.get_json()
    dict_vowel_count = makeArray(payload)
    return JsonResponse(dict_vowel_count)

@app.route("/health")
def health():
    return Response("OK", status=200)

@app.route("/docs")
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')
