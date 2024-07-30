from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase): ...


from .entry import Model as EntryModel  # noqa: E402

__all__ = ["EntryModel"]
