from contextlib import contextmanager
from pathlib import Path

from sqlalchemy.orm import Session

from . import engine


@contextmanager
def generate(
    file_path: Path,
):
    with Session(
        bind=engine.create(file_path),
    ) as session:
        with session.begin():
            yield session
