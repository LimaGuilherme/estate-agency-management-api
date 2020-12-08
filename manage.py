#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import sys

from src import initialize
from src.db_connections import get_sql_alchemy_instance

manager = Manager(initialize.web_app)

sql_alchemy = get_sql_alchemy_instance()


def register_migrate(manager):
    migrate = Migrate(initialize.web_app, sql_alchemy)
    manager.add_command('db', MigrateCommand)
    return migrate


if __name__ == '__main__':
    if 'db' in sys.argv:
        migrate = register_migrate(manager)
    manager.run()
