from flask import Flask, render_template, request
from flask.views import MethodView
app = Flask(__name__)
'''
@app.route('/hello', endpoint='hello')
def helloWorld():
    return "Hello World!"
'''
class HelloView(MethodView):
    def get(self):
        return "Hola Mundo!"
    def post(self):
        return "Hola Mundo!"
    def put(self):
        return "Hola Mundo!"
    def delete(self):
        return "Has borrado el Mundo! POR FIN!"

app.add_url_rule('/hello', view_func=HelloView.as_view('hello'))

'''@app.route('/name', endpoint='name', methods=['GET'])
def helloWorld():
    name = request.args.get('name')
    return "Hola "+ str(name) + "!"'''

class nameView(MethodView):
    def get(self):
        name = request.args.get('name')
        return "Bienvenido, " + name
    def post(self):
        return "Hola Mundo!"
    def put(self):
        return "Hola Mundo!"
    def delete(self):
        return "Te has borrado! POR FIN!"

app.add_url_rule('/name', view_func=nameView.as_view('name'))


'''@app.route('/render', endpoint='render')
def index():
    nombre = request.args.get('name')
    return render_template('index.html', name=nombre)'''

class renderView(MethodView):
    def get(self):
        nombre = request.args.get('name')
        diccionario = {
            'Clave1': 'Valor1',
            'Clave2': 'Valor2',
            'Clave3': 'Valor3',
            'Clave4': 'Valor4',
            'Clave5': 'Valor5',
            'Clave6': 'Valor6',
            'Clave7': 'Valor7',
        }
        return render_template('index.html', name=nombre, diccionario=diccionario)
    def post(self):
        return "Hola Mundo!"
    def put(self):
        return "Hola Mundo!"
    def delete(self):
        return "Te has borrado! POR FIN!"
app.add_url_rule('/render', view_func=renderView.as_view('render'))
