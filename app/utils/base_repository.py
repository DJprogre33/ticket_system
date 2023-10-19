from abc import ABC, abstractmethod

from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session


class AbstractRepository(ABC):
    @abstractmethod
    def __init__(self, session: Session):
        raise NotImplementedError

    @abstractmethod
    def find_one_or_none(self, **filter_by):
        raise NotImplementedError

    # @abstractmethod
    # async def find_all(self, **filter_by):
    #     raise NotImplementedError

    @abstractmethod
    async def insert_data(self, **data):
        raise NotImplementedError

    # @abstractmethod
    # async def update_fields_by_id(self, entity_id, **data):
    #     raise NotImplementedError
    #
    # @abstractmethod
    # async def delete(self, **filter_by):
    #     raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: Session):
        self.session = session

    def find_one_or_none(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = self.session.execute(query)
        return result.scalars().one_or_none()

    def insert_data(self, **data):
        query = insert(self.model).values(**data).returning(self.model)
        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().one()

    def update_fields_by_id(self, entity_id, **data):
        query = (
            update(self.model)
            .where(self.model.id == entity_id)
            .values(**data)
            .returning(self.model)
        )
        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().one()
