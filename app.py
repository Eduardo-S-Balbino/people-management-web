from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "chave-secreta"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pessoas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    busca = request.args.get("busca", "").strip()

    if busca:
        pessoas = Pessoa.query.filter(Pessoa.nome.ilike(f"%{busca}%")).all()
    else:
        pessoas = Pessoa.query.all()

    return render_template(
        "index.html",
        pessoas=pessoas,
        busca=busca,
        pessoa_em_edicao=None
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form["nome"].strip()
    idade = request.form["idade"].strip()

    if nome == "":
        flash("O nome não pode ficar vazio.", "erro")
        return redirect(url_for("home"))

    if not idade.isdigit():
        flash("A idade deve conter apenas números.", "erro")
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
def editar(id):
    pessoa = Pessoa.query.get_or_404(id)
    busca = request.args.get("busca", "").strip()

    if busca:
        pessoas = Pessoa.query.filter(Pessoa.nome.ilike(f"%{busca}%")).all()
    else:
        pessoas = Pessoa.query.all()

    return render_template(
        "index.html",
        pessoas=pessoas,
        busca=busca,
        pessoa_em_edicao=pessoa
    )


@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):
    pessoa = Pessoa.query.get_or_404(id)

    nome = request.form["nome"].strip()
    idade = request.form["idade"].strip()

    if nome == "":
        flash("O nome não pode ficar vazio.", "erro")
        return redirect(url_for("editar", id=id))

    if not idade.isdigit():
        flash("A idade deve conter apenas números.", "erro")
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
def remover(id):
    pessoa = Pessoa.query.get_or_404(id)
    db.session.delete(pessoa)
    db.session.commit()

    flash("Pessoa removida com sucesso!", "sucesso")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)