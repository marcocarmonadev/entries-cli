from enum import Enum

import typer

app = typer.Typer()


class Environment(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


@app.callback()
def callback(
    environment: Environment = typer.Option(
        default=Environment.PRODUCTION,
        envvar="ENVIRONMENT",
    ),
):
    print(environment)


@app.command()
def init():
    ...
    # CURRENT_DIRECTORY_PATH = Path()
    # PYPROJECT_TOML_FILE_PATH = CURRENT_DIRECTORY_PATH / "pyproject.toml"
    # if PYPROJECT_TOML_FILE_PATH.exists():
    #     config.init(
    #         config_directory_path=CURRENT_DIRECTORY_PATH,
    #     )
    # else:
    #     config.init()
