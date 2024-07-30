import datetime as dt
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Status(Enum):
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

    due_date: Mapped[dt.date]
    status: Mapped[Status]
    repeat_forever: Mapped[bool]
    repeated: Mapped[bool | None]
    repeat_interval: Mapped[int | None]
    creation_date: Mapped[dt.datetime] = mapped_column(
        default=dt.datetime.now,
    )
    uuid: Mapped[UUID] = mapped_column(
        default=uuid4,
    )
