import logging

from flask import Flask

from app.config import Config
from app.extensions import scheduler, db, migrate


def get_application() -> Flask:
    application = Flask(__name__, static_url_path="/static", static_folder="static/")
    application.config.from_object(Config)

    scheduler.init_app(application)
    logging.getLogger("apscheduler").setLevel(logging.INFO)

    db.init_app(application)
    migrate.init_app(application, db, directory=Config.ALEMBIC_MIGRATE_DIRECTORY)

    with application.app_context():
        from app import tasks, models  # noqa: F401

        scheduler.start()

    from app.views import bp

    application.register_blueprint(bp)

    return application


app = get_application()
