from abc import abstractmethod
from typing import NoReturn

from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine

from tg_bot.logger import LogMixin


class DbTable(LogMixin):

    def __init__(self, db_string: str):
        self.db: Engine = create_engine(db_string)
        self.meta: MetaData = MetaData(self.db)

    @abstractmethod
    def create_table(self) -> NoReturn:
        raise NotImplementedError("Subclasses must override method create table")

    @abstractmethod
    def insert_record(self, record) -> NoReturn:
        raise NotImplementedError("Subclasses must override method insert record")

    @abstractmethod
    def update_record(self, id, updated_dict) -> NoReturn:
        raise NotImplementedError("Subclasses must override method update record")
