from project.config import config
from project.setup_db import db
from run import create_app

if __name__ == '__main__':
    with create_app(config).app_context():
        db.create_all()
