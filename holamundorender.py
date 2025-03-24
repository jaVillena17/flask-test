from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/render')
def index():
    nombre = request.args.get('name')
    return render_template('index.html', name=nombre)