from flask import Flask, render_template, request, redirect, flash
import json

app = Flask(__name__)
app.secret_key = "chave-secreta-simples"


def carregar_pessoas():
    try:
        with open("pessoas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except:
        return []


def salvar_pessoas(pessoas):
    with open("pessoas.json", "w", encoding="utf-8") as arquivo:
        json.dump(pessoas, arquivo, ensure_ascii=False, indent=4)


def nome_ja_existe(pessoas, nome, ignorar_indice=None):
    for i, pessoa in enumerate(pessoas):
        if ignorar_indice is not None and i == ignorar_indice:
            continue

        if pessoa["nome"].strip().lower() == nome.strip().lower():
            return True

    return False


pessoas = carregar_pessoas()


@app.route("/")
def home():
    busca = request.args.get("busca", "").strip()
    editar_indice = request.args.get("editar")

    pessoa_em_edicao = None
    indice_em_edicao = None

    if editar_indice is not None and editar_indice.isdigit():
        indice = int(editar_indice)

        if 0 <= indice < len(pessoas):
            pessoa_em_edicao = pessoas[indice]
            indice_em_edicao = indice

    pessoas_filtradas = []

    for i, pessoa in enumerate(pessoas):
        if busca == "" or busca.lower() in pessoa["nome"].lower():
            pessoas_filtradas.append({
                "indice": i,
                "nome": pessoa["nome"],
                "idade": pessoa["idade"]
            })

    return render_template(
        "index.html",
        pessoas=pessoas_filtradas,
        busca=busca,
        pessoa_em_edicao=pessoa_em_edicao,
        indice_em_edicao=indice_em_edicao
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form["nome"].strip()
    idade = request.form["idade"].strip()

    if nome == "":
        flash("O nome não pode ficar vazio.", "erro")
        return redirect("/")

    if not idade.isdigit():
        flash("A idade deve conter apenas números.", "erro")
        return redirect("/")

    if nome_ja_existe(pessoas, nome):
        flash("Já existe uma pessoa cadastrada com esse nome.", "erro")
        return redirect("/")

    pessoas.append({
        "nome": nome,
        "idade": int(idade)
    })

    salvar_pessoas(pessoas)
    flash("Pessoa adicionada com sucesso!", "sucesso")
    return redirect("/")


@app.route("/atualizar/<int:indice>", methods=["POST"])
def atualizar(indice):
    if not (0 <= indice < len(pessoas)):
        flash("Pessoa não encontrada.", "erro")
        return redirect("/")

    nome = request.form["nome"].strip()
    idade = request.form["idade"].strip()

    if nome == "":
        flash("O nome não pode ficar vazio.", "erro")
        return redirect(f"/?editar={indice}")

    if not idade.isdigit():
        flash("A idade deve conter apenas números.", "erro")
        return redirect(f"/?editar={indice}")

    if nome_ja_existe(pessoas, nome, ignorar_indice=indice):
        flash("Já existe outra pessoa cadastrada com esse nome.", "erro")
        return redirect(f"/?editar={indice}")

    pessoas[indice]["nome"] = nome
    pessoas[indice]["idade"] = int(idade)

    salvar_pessoas(pessoas)
    flash("Pessoa atualizada com sucesso!", "sucesso")
    return redirect("/")


@app.route("/remover/<int:indice>", methods=["POST"])
def remover(indice):
    if 0 <= indice < len(pessoas):
        nome_removido = pessoas[indice]["nome"]
        pessoas.pop(indice)
        salvar_pessoas(pessoas)
        flash(f"{nome_removido} foi removido com sucesso!", "sucesso")
    else:
        flash("Pessoa não encontrada.", "erro")

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)