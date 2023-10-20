from abc import ABC, abstractmethod
from typing import Any, Optional, Type, TypeVar

from sqlalchemy import insert, select, update
from sqlalchemy.orm import Session

from app.db import Base


class AbstractRepository(ABC):
    @abstractmethod
    def __init__(self, session: Session):
        raise NotImplementedError

    @abstractmethod
    def find_one_or_none(self, **filter_by):
        raise NotImplementedError

    @abstractmethod
    async def insert_data(self, **data):
        raise NotImplementedError

    @abstractmethod
    async def update_fields_by_id(self, entity_id, **data):
        raise NotImplementedError


SQLAlchemy = TypeVar("SQLAlchemy", bound=Base)


class SQLAlchemyRepository(AbstractRepository):
    model: SQLAlchemy

    def __init__(self, session: Session):
        self.session = session

    def find_one_or_none(self, **filter_by: Any) -> Optional[SQLAlchemy]:
        query = select(self.model).filter_by(**filter_by)
        result = self.session.execute(query)
        return result.scalars().one_or_none()

    def insert_data(self, **data: Any) -> SQLAlchemy:
        query = insert(self.model).values(**data).returning(self.model)
        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().one()

    def update_fields_by_id(self, entity_id: int, **data: Any) -> SQLAlchemy:
        query = (
            update(self.model)
            .where(self.model.id == entity_id)
            .values(**data)
            .returning(self.model)
        )
        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().one()
