import sqlite3
from contextlib import contextmanager
from pathlib import Path

from . import FILE_NAME


@contextmanager
def generate(
    directory_path: Path,
):
    with sqlite3.connect(
        database=directory_path / FILE_NAME,
    ) as connection:
        yield connection
