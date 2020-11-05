from flask import Flask
app = Flask(__name__)

@app.route('/sumar/<a>/<b>')
def sumar(a=1,b=1):
    a=int(a)
    b=int(b)
    c = a+b
    return str(c)

@app.route('/restar/<a>/<b>')
def restar(a=1,b=1):
    a=int(a)
    b=int(b)
    c = a-b
    return str(c)

@app.route('/multiplicar/<a>/<b>')
def multiplicar(a=1,b=1):
    a=int(a)
    b=int(b)
    c = a*b
    return str(c)

@app.route('/dividir/<a>/<b>')
def dividir(a=1,b=1):
    a=int(a)
    b=int(b)
    c = a/b
    return str(c)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
