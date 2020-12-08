from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import sys

from src.db_connections import get_sql_alchemy_instance
from src.web_app import get_web_app


if __name__ == '__main__':
    web_app = get_web_app()
    sql_alchemy = get_sql_alchemy_instance()

    flask_manager = Manager(web_app)

    if 'db' in sys.argv:
        migrate = Migrate(web_app, sql_alchemy)
        flask_manager.add_command('db', MigrateCommand)

    flask_manager.run()
