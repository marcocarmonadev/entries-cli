from pathlib import Path

from source.entities import Base

from . import engine, session

FILE_NAME = "entries-cli.db"
DEFAULT_FILE_PATH = Path.home() / f".local/share/{FILE_NAME}"

file_path = DEFAULT_FILE_PATH


def set_file_path(
    debug: bool,
) -> None:
    if debug:
        global file_path
        file_path = Path() / "entries-cli.db"


def init():
    if file_path.exists():
        raise FileExistsError(f"{file_path} already exists!")
    file_path.touch()
    Base.metadata.create_all(
        bind=engine.create(file_path),
    )


__all__ = ["engine", "session"]
