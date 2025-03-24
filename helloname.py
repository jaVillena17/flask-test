from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/helloname', methods=['GET'])
def helloWorld():
    name = request.args.get('name')
    return "Hola "+ str(name) + "!"