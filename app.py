
from flask import Flask, render_template, redirect, session, url_for, request, flash
import dao as Banco


app = Flask(__name__)
app.secret_key = 'mateus'


@app.route("/")
def index():
    return render_template("landing_page.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/cadastro")
def cadastro():
    return render_template("a.html")


@app.route("/autenticar", methods=['POST'])
def autenticar():
    email = request.form['email']
    senha = request.form['senha']
    values = Banco.get_items(email)
    if values:
        nome = values['nome']
        senha_banco = values['senha']
        if senha == senha_banco:
            session['usuario_logado'] = nome
            return redirect(url_for('home'))
        else:
            flash("Senha incorreta")
            return redirect(url_for('login'))
    else:
        flash("Os dados inseridos podem estar incorretos")
        return redirect(url_for('login'))


@app.route("/criar", methods=['POST'])
def cria_user():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    
    if Banco.verify_items(email, telefone):
        Banco.save_user(nome, sobrenome, email, telefone, senha)
        return redirect(url_for('login'))
    else:
        flash("Os dados inseridos já estão em uso")
        return redirect(url_for('cadastro'))

@app.route("/home")
def home():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash("Página para usuários logados")
        return redirect(url_for('login'))
    return render_template('home.html')


@app.route("/logout",)
def logout():
    session['usuario_logado'] = None
    flash("Até mais")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)