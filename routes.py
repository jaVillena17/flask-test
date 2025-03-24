from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/hello', endpoint='hello')
def helloWorld():
    return "Hello World!"

@app.route('/name', endpoint='name', methods=['GET'])
def helloWorld():
    name = request.args.get('name')
    return "Hola "+ str(name) + "!"

@app.route('/render', endpoint='render')
def index():
    nombre = request.args.get('name')
    return render_template('index.html', name=nombre)