from flask import Flask, render_template, request
from flask.views import View
app = Flask(__name__)
'''
@app.route('/hello', endpoint='hello')
def helloWorld():
    return "Hello World!"
'''
class HelloView(View):
    def dispatch_request(self):
        return "Hola Mundo"

app.add_url_rule('/hello', view_func=HelloView.as_view('hello'))

'''@app.route('/name', endpoint='name', methods=['GET'])
def helloWorld():
    name = request.args.get('name')
    return "Hola "+ str(name) + "!"'''

class nameView(View):
    def dispatch_request(self):
        name = request.args.get('name')
        return "Bienvenido, " + name

app.add_url_rule('/name', view_func=nameView.as_view('name'))


'''@app.route('/render', endpoint='render')
def index():
    nombre = request.args.get('name')
    return render_template('index.html', name=nombre)'''

class renderView(View):
    def dispatch_request(self):
        nombre = request.args.get('name')
        return render_template('index.html', name=nombre)

app.add_url_rule('/render', view_func=renderView.as_view('render'))
