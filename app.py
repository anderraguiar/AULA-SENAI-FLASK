from flask import Flask, request

app = Flask(__name__)

# endpoint: buscar todos os alunos
@app.route('/buscaraluno/<int:id>', methods=['GET'])
def buscar_aluno(id):
    return f"aluno de codigo: {id}"

@app.route('/listaralunos', methods=['GET'])
def listar_alunos():
    return "todos alunos listados"

@app.route('/adicionaraluno', methods=['POST'])
def adicionar_aluno():
    id = request.args.get('id')
    nome = request.args.get('nome')
    return f"Aluno Cadastrado: {id} {nome}"


if __name__ == "__main__":
    app.run(debug=True)