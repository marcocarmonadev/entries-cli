import datetime as dt
from enum import StrEnum
from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Status(StrEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    CLOSED = "closed"


class Model(Base):
    __tablename__ = "entries"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    concept: Mapped[str]
    amount: Mapped[float]
    creation_date: Mapped[dt.datetime] = mapped_column(
        default=dt.datetime.now,
    )
    due_date: Mapped[dt.date]
    uuid: Mapped[UUID] = mapped_column(
        default=uuid4,
    )
    status: Mapped[Status]
    repeat_forever: Mapped[bool]
    repeated: Mapped[bool | None] = mapped_column(
        default=None,
    )
    repeat_interval: Mapped[int | None] = mapped_column(
        default=None,
    )
