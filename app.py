import random


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    ciudad = "AlberHouse"
    return render_template('index.html', lugar=ciudad)

@app.route('/hola')
def hola_mundo():
    # Generar numero aleatorio
    random_number = random.randint(1,10)
    return 'Hola mundo'+ '<br>'+str(random_number)

@app.route('/<int:numero>')
def numero_cualquiera(numero):
    multiplicado = numero*10
    return str(multiplicado)


if __name__ == '__main__':
    app.run()
