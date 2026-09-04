#importe de biblioteca
from flask import Flask, render_template, request

#criar objeto flask "apelido - app"
app = Flask(__name__)
base_fake = []
#rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/atividades/criar', methods= ['GET', 'POST'])
def criar_atividades():
    if request.method == 'POST':
        nome_atividade = request.form.get('form_nome')
        data_atividade = request.form.get('form_data')
        prioridade_atividade = request.form.get('form_prioridade')
        categoria_atividade = request.form.getlist('form_categoria')
        descricao_atividade = request.form.get('form_descricao')

        dados = {
            'nome': nome_atividade,
            'data': data_atividade,
            'prioridade': prioridade_atividade,
            'categoria': categoria_atividade,
            'descricao': descricao_atividade,
        }

        print(f'dados cadastrados: {dados}')
        base_fake.append(dados)
        print(F'base_fake:{base_fake}')
        return render_template('criar_atividades.html', dados_atividade=base_fake)

    return render_template ('criar_atividades.html')
@app.route('/atividades/listar')
def listar_atividades():
    return render_template ('listar_atividades.html',dados_atividade=base_fake)

@app.route('/pessoa')
def pessoa():
    return render_template ('pessoa.html')

#iniciar aplicação web
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
#nada deve ser colocado abaixo