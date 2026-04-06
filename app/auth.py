from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from .models import Usuario
from . import login_manager

auth = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        if username == "" or password == "":
            flash("Preencha usuário e senha.", "erro")
            return redirect(url_for("auth.login"))

        usuario = Usuario.query.filter_by(username=username).first()

        if usuario and check_password_hash(usuario.password, password):
            login_user(usuario)
            flash("Login realizado com sucesso!", "sucesso")
            return redirect(url_for("main.home"))

        flash("Usuário ou senha inválidos.", "erro")
        return redirect(url_for("auth.login"))

    return render_template("login.html", mostrar_credenciais=True)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout realizado com sucesso!", "sucesso")
    return redirect(url_for("auth.login"))