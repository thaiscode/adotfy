from flask import Flask, render_template, url_for
from models.queryFunctions import buscarAnimais

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
   listaDeAdocao = buscarAnimais()

   return render_template('index.html', lista = listaDeAdocao)

@app.route('/pets')
def rota_pets():
   listaDeAdocao = buscarAnimais()

   return render_template('pets.html', lista = listaDeAdocao)

@app.route('/sobre-adotfy')
def rota_sobre():
   return render_template('sobre.html')

@app.route('/cadastro-ong')
def rota_cadastro():
   return render_template('cadastro-ong.html')

@app.route('/formulario')
def rota_formulario():
   return render_template('formulario.html')

if __name__ == '__main__':
   app.run(debug = True)
