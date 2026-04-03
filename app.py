from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "chave-secreta"

# Configuração do banco
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pessoas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Modelo da tabela
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)


@app.route("/")
def home():
    busca = request.args.get("busca", "").lower()
    
    if busca:
        pessoas = Pessoa.query.filter(Pessoa.nome.ilike(f"%{busca}%")).all()
    else:
        pessoas = Pessoa.query.all()
    
    return render_template("index.html", pessoas=pessoas, busca=busca)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form["nome"]
    idade = request.form["idade"]

    if nome == "" or idade == "":
        flash("Preencha todos os campos!", "erro")
        return redirect(url_for("home"))

    nova_pessoa = Pessoa(nome=nome, idade=int(idade))
    db.session.add(nova_pessoa)
    db.session.commit()

    flash("Pessoa adicionada com sucesso!", "sucesso")
    return redirect(url_for("home"))


@app.route("/remover/<int:id>")
def remover(id):
    pessoa = Pessoa.query.get_or_404(id)
    db.session.delete(pessoa)
    db.session.commit()

    flash("Pessoa removida!", "sucesso")
    return redirect(url_for("home"))


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    pessoa = Pessoa.query.get_or_404(id)

    if request.method == "POST":
        pessoa.nome = request.form["nome"]
        pessoa.idade = int(request.form["idade"])
        db.session.commit()

        flash("Pessoa atualizada!", "sucesso")
        return redirect(url_for("home"))

    return render_template("editar.html", pessoa=pessoa)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # 🔥 cria banco automaticamente
    app.run(debug=True)