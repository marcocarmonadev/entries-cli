from pathlib import Path

from sqlalchemy import Engine, create_engine

DEFAULT_ECHO_VALUE = False

echo = DEFAULT_ECHO_VALUE


def set_echo(
    debug: bool,
):
    if debug:
        global echo
        echo = True


def create(
    file_path: Path,
) -> Engine:
    return create_engine(
        url=f"sqlite:///{file_path}",
        echo=echo,
    )
