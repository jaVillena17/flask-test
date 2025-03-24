from flask import Flask
app = Flask(__name__)
@app.route('/', endpoint='helloworld')
def helloWorld():
    return "Hello World!"