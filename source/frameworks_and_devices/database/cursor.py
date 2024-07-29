from contextlib import contextmanager

from . import connection


@contextmanager
def generate():
    with connection.generate() as _connection:
        cursor = _connection.cursor()
        try:
            yield cursor
        finally:
            cursor.close()
