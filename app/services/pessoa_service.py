from app.models import Pessoa
from app import db


def criar_pessoa(nome, idade):
    nova_pessoa = Pessoa(nome=nome, idade=idade)
    db.session.add(nova_pessoa)
    db.session.commit()
    return nova_pessoa


def atualizar_pessoa(pessoa, nome, idade):
    pessoa.nome = nome
    pessoa.idade = idade
    db.session.commit()
    return pessoa


def remover_pessoa(pessoa):
    db.session.delete(pessoa)
    db.session.commit()