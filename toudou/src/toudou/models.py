import os
import pickle
import uuid

import toudou.initdb as db

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

TODO_FOLDER = "db"


@dataclass
class Todo:
    id: int
    task: str
    complete: bool
    due: Optional[datetime]


def init_db() -> None:
    db.init_db()


def create_todo(task: str, complete: bool = False, due: Optional[datetime] = None) -> None:
    todo = Todo(uuid.uuid4().int, task=task, complete=complete, due=due)
    db.save(todo)


def get_todo(task: str) -> None:
    return db.select_todo(task)


def get_todos() -> list[Todo]:
    return db.select_all()


def update_todo(
        id: int,
        task: str,
        complete: bool,
        due: Optional[datetime]
) -> None:
    db.update(id, task, complete, due)


def delete_todo(id: int) -> None:
    db.remove(id)
