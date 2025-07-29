from sqlalchemy.exc import OperationalError

from ARZi.models import db


def is_database_mariadb():
    try:
        result = db.session.execute("SELECT version()").fetchone()[0]
        mariadb = "mariadb" in result.lower()
    except OperationalError:
        mariadb = False
    return mariadb
