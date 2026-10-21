from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    prof = "Daniel"
    materia = "Programação Web"
    return render_template('index.html', prof=prof, materia=materia)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        matricula = request.form['matricula']
        # Aqui você pode adicionar lógica para salvar os dados do usuário no banco de dados
        return f"Usuário {nome} cadastrado com sucesso!"
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)