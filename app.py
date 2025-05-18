from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html')

@app.route('/pets')
def rota_pets():
   return render_template('pets.html')

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

"""
@app.route('/quero-adotar')
def quero_adotar():
    listaDeAdocao = buscarNomesAnimais()
    
    return render_template('quero-adotar.html', lista = listaDeAdocao)

@app.route('/info-animal/<int:idAnimal>')
def info_do_animal(idAnimal):
    informacoesAdocao = infoAnimal(idAnimal)
    return render_template('info-animal.html', info = informacoesAdocao)
"""
