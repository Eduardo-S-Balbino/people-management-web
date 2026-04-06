import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")

    database_url = os.getenv("DATABASE_URL")

    if database_url:
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        SQLALCHEMY_DATABASE_URI = "sqlite:///pessoas.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False