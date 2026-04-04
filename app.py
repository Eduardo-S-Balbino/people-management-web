from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os

app = Flask(__name__)
app.secret_key = "chave-secreta"

database_url = os.getenv("DATABASE_URL")

if database_url:
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pessoas.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


with app.app_context():
    db.create_all()

    usuario_existente = Usuario.query.filter_by(username="admin").first()
    if not usuario_existente:
        usuario_padrao = Usuario(username="admin", password="1234")
        db.session.add(usuario_padrao)
        db.session.commit()


def nome_valido(nome):
    return nome.strip() != ""


def idade_valida(idade):
    if not idade.isdigit():
        return False

    idade_numero = int(idade)
    return 0 < idade_numero <= 120


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        if username == "" or password == "":
            flash("Preencha usuário e senha.", "erro")
            return redirect(url_for("login"))

        usuario = Usuario.query.filter_by(username=username, password=password).first()

        if usuario:
            login_user(usuario)
            flash("Login realizado com sucesso!", "sucesso")
            return redirect(url_for("home"))
        else:
            flash("Usuário ou senha inválidos.", "erro")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout realizado com sucesso!", "sucesso")
    return redirect(url_for("login"))


@app.route("/")
@login_required
def home():
    busca = request.args.get("busca", "").strip()
    pagina = request.args.get("pagina", 1, type=int)
    por_pagina = 5

    query = Pessoa.query

    if busca:
        query = query.filter(Pessoa.nome.ilike(f"%{busca}%"))

    paginacao = query.order_by(Pessoa.id.asc()).paginate(page=pagina, per_page=por_pagina, error_out=False)
    pessoas = paginacao.items

    return render_template(
        "index.html",
        pessoas=pessoas,
        busca=busca,
        pessoa_em_edicao=None,
        form_nome="",
        form_idade="",
        paginacao=paginacao
    )


@app.route("/adicionar", methods=["POST"])
@login_required
def adicionar():
    nome = request.form["nome"].strip()
    idade = request.form["idade"].strip()

    if not nome_valido(nome):
        flash("O nome não pode ficar vazio.", "erro")
        return redirect(url_for("home"))

    if not idade_valida(idade):
        flash("A idade deve ser um número entre 1 e 120.", "erro")
        return redirect(url_for("home"))

    pessoa_existente = Pessoa.query.filter(Pessoa.nome.ilike(nome)).first()
    if pessoa_existente:
        flash("Já existe uma pessoa cadastrada com esse nome.", "erro")
        return redirect(url_for("home"))

    nova_pessoa = Pessoa(nome=nome, idade=int(idade))
    db.session.add(nova_pessoa)
    db.session.commit()

    flash("Pessoa adicionada com sucesso!", "sucesso")
    return redirect(url_for("home"))


@app.route("/editar/<int:id>")
@login_required
def editar(id):
    pessoa = Pessoa.query.get_or_404(id)
    busca = request.args.get("busca", "").strip()
    pagina = request.args.get("pagina", 1, type=int)
    por_pagina = 5

    query = Pessoa.query

    if busca:
        query = query.filter(Pessoa.nome.ilike(f"%{busca}%"))

    paginacao = query.order_by(Pessoa.id.asc()).paginate(page=pagina, per_page=por_pagina, error_out=False)
    pessoas = paginacao.items

    return render_template(
        "index.html",
        pessoas=pessoas,
        busca=busca,
        pessoa_em_edicao=pessoa,
        form_nome=pessoa.nome,
        form_idade=pessoa.idade,
        paginacao=paginacao
    )


@app.route("/atualizar/<int:id>", methods=["POST"])
@login_required
def atualizar(id):
    pessoa = Pessoa.query.get_or_404(id)

    nome = request.form["nome"].strip()
    idade = request.form["idade"].strip()

    if not nome_valido(nome):
        flash("O nome não pode ficar vazio.", "erro")
        return redirect(url_for("editar", id=id))

    if not idade_valida(idade):
        flash("A idade deve ser um número entre 1 e 120.", "erro")
        return redirect(url_for("editar", id=id))

    pessoa_existente = Pessoa.query.filter(Pessoa.nome.ilike(nome), Pessoa.id != id).first()
    if pessoa_existente:
        flash("Já existe outra pessoa cadastrada com esse nome.", "erro")
        return redirect(url_for("editar", id=id))

    pessoa.nome = nome
    pessoa.idade = int(idade)
    db.session.commit()

    flash("Pessoa atualizada com sucesso!", "sucesso")
    return redirect(url_for("home"))


@app.route("/remover/<int:id>", methods=["POST"])
@login_required
def remover(id):
    pessoa = Pessoa.query.get_or_404(id)
    db.session.delete(pessoa)
    db.session.commit()

    flash("Pessoa removida com sucesso!", "sucesso")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)