from project.config import config
from run import create_app
from project.setup_db import db

if __name__ == '__main__':
    with create_app(config).app_context():
        db.create_all()
