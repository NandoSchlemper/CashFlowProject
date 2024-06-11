from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from source.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=Config):
    app = Flask(__name__, template_folder="../templates")

    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprint register with routes

    with app.app_context():
        db.create_all()

    return app