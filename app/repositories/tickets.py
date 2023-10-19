from app.models.tickets import Tickets
from app.utils.base_repository import SQLAlchemyRepository


class TicketsRepository(SQLAlchemyRepository):
    model = Tickets
    pass
