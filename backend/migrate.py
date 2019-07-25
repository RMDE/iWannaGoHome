# -*- coding: utf-8 -*-
from app import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.model.base import db

from app.model.user import User
from app.model.mock import Mock
from app.model.project import Project

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
