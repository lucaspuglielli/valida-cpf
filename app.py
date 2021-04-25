from flask import Flask, render_template, url_for, request, redirect
from static.python.valida import CPF

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        retorno = ""
        retorno = CPF(request.form['content']).retorno
        return render_template('index.html', retorno = retorno)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)