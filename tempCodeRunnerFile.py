from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sorteio')
def sorteio():
    numero_vencedor = str(random.randint(10000, 99999))
    return render_template('resultado.html', numero_vencedor=numero_vencedor)

if __name__ == '__main__':
    app.run(debug=True)
