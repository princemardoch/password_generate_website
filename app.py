from flask import Flask, request, render_template
from passwordgen import *

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def passw():
    mdp = ''
    longeur = '12'
    if request.method == 'POST':
        if ('numbers' in request.form and 'symbols' in request.form and request.form.get('lgp') != '') :
            longeur = request.form['lgp']
            mdp = passwAll(int(longeur))

        elif 'numbers' in request.form and 'symbols' in request.form:
            mdp = passwAll(int(longeur))

        elif 'numbers' in request.form and request.form.get('lgp') != '':
            longeur = request.form['lgp']
            mdp = passwLd(int(longeur))

        elif request.form.get('lgp') != '':
            longeur = request.form['lgp']
            mdp = passwL(int(longeur))

        elif request.form.get('lgp') != '':
            longeur = request.form['lgp']
            mdp = passP(int(longeur))

        elif 'symbols' in request.form:
            mdp = passP(int(longeur))

        elif 'numbers' in request.form:
            mdp = mdp = passwLd(int(longeur))

        else:
            mdp = passwL(int(longeur))
            
    return render_template('index.html', mdp=mdp)

if __name__ == '__main__':
    app.run(debug=True)