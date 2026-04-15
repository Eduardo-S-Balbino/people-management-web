from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required
from .models import Pessoa
from app.services.pessoa_service import criar_pessoa, atualizar_pessoa, remover_pessoa

main = Blueprint("main", __name__)


def nome_valido(nome):
    return nome.strip() != ""


def idade_valida(idade):
    if not idade.isdigit():
        return False

    idade_numero = int(idade)
    return 0 < idade_numero <= 120


@main.route("/")
@login_required
def home():
    busca = request.args.get("busca", "").strip()
    pagina = request.args.get("pagina", 1, type=int)
    por_pagina = 5

    query = Pessoa.query

    if busca:
        query = query.filter(Pessoa.nome.ilike(f"%{busca}%"))

    paginacao = query.order_by(Pessoa.id.asc()).paginate(
        page=pagina,
        per_page=por_pagina,
        error_out=False
    )

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


@main.route("/api/pessoas", methods=["GET"])
@login_required
def listar_pessoas_api():
    pessoas = Pessoa.query.order_by(Pessoa.id.asc()).all()

    resultado = []
    for pessoa in pessoas:
        resultado.append({
            "id": pessoa.id,
            "nome": pessoa.nome,
            "idade": pessoa.idade
        })

    return jsonify(resultado), 200


@main.route("/api/pessoas/<int:id>", methods=["GET"])
@login_required
def buscar_pessoa_api(id):
    pessoa = Pessoa.query.get_or_404(id)

    resultado = {
        "id": pessoa.id,
        "nome": pessoa.nome,
        "idade": pessoa.idade
    }

    return jsonify(resultado), 200


@main.route("/adicionar", methods=["POST"])
@login_required
def adicionar():
    nome = request.form["nome"].strip()
    idade = request.form["idade"].strip()

    if not nome_valido(nome):
        flash("O nome não pode ficar vazio.", "erro")
        return redirect(url_for("main.home"))

    if not idade_valida(idade):
        flash("A idade deve ser um número entre 1 e 120.", "erro")
        return redirect(url_for("main.home"))

    pessoa_existente = Pessoa.query.filter(Pessoa.nome.ilike(nome)).first()
    if pessoa_existente:
        flash("Já existe uma pessoa cadastrada com esse nome.", "erro")
        return redirect(url_for("main.home"))

    criar_pessoa(nome, int(idade))

    flash("Pessoa adicionada com sucesso!", "sucesso")
    return redirect(url_for("main.home"))


@main.route("/editar/<int:id>")
@login_required
def editar(id):
    pessoa = Pessoa.query.get_or_404(id)
    busca = request.args.get("busca", "").strip()
    pagina = request.args.get("pagina", 1, type=int)
    por_pagina = 5

    query = Pessoa.query

    if busca:
        query = query.filter(Pessoa.nome.ilike(f"%{busca}%"))

    paginacao = query.order_by(Pessoa.id.asc()).paginate(
        page=pagina,
        per_page=por_pagina,
        error_out=False
    )

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


@main.route("/atualizar/<int:id>", methods=["POST"])
@login_required
def atualizar(id):
    pessoa = Pessoa.query.get_or_404(id)

    nome = request.form["nome"].strip()
    idade = request.form["idade"].strip()
    busca = request.args.get("busca", "").strip()
    pagina = request.args.get("pagina", 1, type=int)

    if not nome_valido(nome):
        flash("O nome não pode ficar vazio.", "erro")
        return redirect(url_for("main.editar", id=id, busca=busca, pagina=pagina))

    if not idade_valida(idade):
        flash("A idade deve ser um número entre 1 e 120.", "erro")
        return redirect(url_for("main.editar", id=id, busca=busca, pagina=pagina))

    pessoa_existente = Pessoa.query.filter(Pessoa.nome.ilike(nome), Pessoa.id != id).first()
    if pessoa_existente:
        flash("Já existe outra pessoa cadastrada com esse nome.", "erro")
        return redirect(url_for("main.editar", id=id, busca=busca, pagina=pagina))

    atualizar_pessoa(pessoa, nome, int(idade))

    flash("Pessoa atualizada com sucesso!", "sucesso")
    return redirect(url_for("main.home", busca=busca, pagina=pagina))


@main.route("/remover/<int:id>", methods=["POST"])
@login_required
def remover(id):
    pessoa = Pessoa.query.get_or_404(id)
    busca = request.args.get("busca", "").strip()
    pagina = request.args.get("pagina", 1, type=int)

    remover_pessoa(pessoa)

    flash("Pessoa removida com sucesso!", "sucesso")
    return redirect(url_for("main.home", busca=busca, pagina=pagina))