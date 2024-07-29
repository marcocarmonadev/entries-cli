from configparser import ConfigParser
from pathlib import Path

import typer

FILE_NAME = "config.ini"


def init(
    config_directory_path: Path = Path(
        typer.get_app_dir(
            app_name="entries-cli",
        )
    ),
):
    file_path = config_directory_path / FILE_NAME
    assert not file_path.exists(), f"{file_path} already exists!"
    config_parser = ConfigParser()
    config_parser["database"] = {"path": "~/./data.db"}
    with file_path.open(
        mode="w",
    ) as f:
        config_parser.write(f)
