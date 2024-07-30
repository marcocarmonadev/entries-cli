import datetime as dt
from typing import Annotated
from uuid import UUID

import typer

from source.entities import entry
from source.frameworks_and_devices import database
from source.interface_adapters import controllers

app = typer.Typer()


@app.callback()
def callback(
    debug: Annotated[
        bool,
        typer.Option(
            "--debug",
            envvar="DEBUG",
            hidden=True,
        ),
    ] = False,
):
    database.set_file_path(debug)
    database.engine.set_echo(debug)


@app.command()
def init():
    try:
        database.init()
    except FileExistsError as exc:
        print(exc)
        raise typer.Abort()


@app.command()
def create(
    concept: Annotated[
        str,
        typer.Option(
            prompt=True,
        ),
    ],
    amount: Annotated[
        float,
        typer.Option(
            prompt=True,
        ),
    ],
    due_date: Annotated[
        dt.datetime,
        typer.Option(
            prompt=True,
        ),
    ],
    status: Annotated[
        entry.Status,
        typer.Option(
            prompt=True,
        ),
    ],
):
    controllers.entry.create()


@app.command()
def read(): ...


@app.command()
def update(
    uuid: UUID,
): ...


@app.command()
def delete(
    uuid: UUID,
): ...
