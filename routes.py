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


app.add_url_rule('/hello', view_func=HelloView.as_view('hello'))

'''@app.route('/name', endpoint='name', methods=['GET'])
def helloWorld():
    name = request.args.get('name')
    return "Hola "+ str(name) + "!"'''

class nameView(MethodView):
    def get(self):
        name = request.args.get('name')
        return "Bienvenido, " + name

app.add_url_rule('/name', view_func=nameView.as_view('name'))


'''@app.route('/render', endpoint='render')
def index():
    nombre = request.args.get('name')
    return render_template('index.html', name=nombre)'''

class renderView(MethodView):
    def get(self):
        nombre = request.args.get('name')

        lista = ["Patata", "Tomate", "Lechuga", "Pimiento", "Habichuela", "Manzana", "Brocoli"]

        palabra_a_buscar = request.args.get('search')

        diccionario = {
            'Nombre': nombre,
            'Apellido1': 'Villena',
            'Apellido2': 'Fernández',
            'Dirección': 'Calle tal',
            'Compra': lista,
            'dic' : {'telefono':'6634653456'},
            'search': palabra_a_buscar in lista
        }

        return render_template('index.html', **diccionario)
app.add_url_rule('/render', view_func=renderView.as_view('render'))
