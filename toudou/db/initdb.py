import datetime
from typing import Optional

from sqlalchemy import *

engine = create_engine("sqlite:///db/todos.db")
metadata_obj = MetaData()
todo_table = Table(
    "todos",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("task", String(1000), nullable=False),
    Column("complete", Boolean, nullable=True),
    Column("due", DateTime, nullable=True)
)


def init_db():
    metadata_obj.create_all(engine)


def save(todo) -> None:
    stmt = insert(todo_table).values(
        task=todo.task,
        complete=todo.complete,
        due=todo.due
    )
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()


def select_all():
    stmt = select(todo_table)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        return result.all()


def select_todo(todo) -> None:
    stmt = (
        select(todo_table).
        where(todo_table.c.task == todo)
    )
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


def remove(todo) -> None:
    stmt = (
        delete(todo_table).
        where(todo_table.c.task == todo)
    )
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

