from app import create_app, db
from app.models import Usuario
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.create_all()

    usuario = Usuario.query.filter_by(username="admin").first()

    if not usuario:
        novo = Usuario(
            username="admin",
            password=generate_password_hash("1234")
        )
        db.session.add(novo)
        db.session.commit()
    else:
        if not usuario.password.startswith("scrypt:") and not usuario.password.startswith("pbkdf2:"):
            usuario.password = generate_password_hash(usuario.password)
            db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)