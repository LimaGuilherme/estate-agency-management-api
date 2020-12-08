import pymysql

from flask_sqlalchemy import SQLAlchemy

from src.web_app import get_web_app

pymysql.install_as_MySQLdb()

sql_alchemy_instance = None


def get_sql_alchemy_instance() -> SQLAlchemy:
    global sql_alchemy_instance

    if not sql_alchemy_instance:
        web_app = get_web_app()
        sql_alchemy_instance = SQLAlchemy(web_app)

    return sql_alchemy_instance

